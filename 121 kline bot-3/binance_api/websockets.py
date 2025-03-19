from .error import WebsocketError
import threading
import websocket
import requests
import asyncio
import aiohttp
import ujson
import time


class WebsocketSync:
    base_url: str
    reconnect_timeout = 30
    listen_key_update_timer = 10
    streams_limit = 200

    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None):
        self.stream = stream
        if not api_key:
            if not self.stream:
                self.stream = []
            elif isinstance(self.stream, list) and len(self.stream) > self.streams_limit:
                raise WebsocketError(f'Слишком много потоков (максимум {self.streams_limit})')
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error
        self.api_key = api_key
        self.testnet = testnet
        self.listen_key_url = listen_key_url
        self.working = True
        self.connected = False
        self.listen_key = None
        self.ws = None
        if self.api_key:
            self.headers = {
                'Accept': 'application/json',
                'X-MBX-APIKEY': api_key
            }
        threading.Thread(target=self.listen_key_update_service, daemon=True).start()
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        while self.working:
            self.connected = False
            try:
                if self.api_key:
                    self.listen_key = self.get_listen_key()
                    url = f"{self.base_url}/ws/{self.listen_key}"
                elif isinstance(self.stream, list):
                    url = f"{self.base_url}/stream?streams={'/'.join(self.stream[:self.streams_limit])}"
                else:
                    url = f"{self.base_url}/ws/{self.stream}"
                self.ws = websocket.WebSocketApp(url, on_open=self._on_open, on_message=self._on_message,
                                                 on_error=self.on_error, on_close=self.on_close)
                self.ws_thread = threading.Thread(target=self.ws.run_forever, daemon=True)
                self.ws_thread.start()
                self.ws_thread.join()
            except Exception as e:
                if self.on_error:
                    try:
                        self.on_error(self.ws, e)
                    except:
                        pass
            finally:
                if not self.connected:
                    time.sleep(self.reconnect_timeout)

    def _on_open(self, ws):
        self.connected = True
        if self.on_open:
            self.on_open(ws)

    def _on_message(self, ws, message):
        try:
            message = ujson.loads(message)
        except ujson.JSONDecodeError:
            return
        if self.on_message:
            self.on_message(ws, message)
        if message.get('e') == 'listenKeyExpired':
            self.listen_key = None
            self.ws.close()

    def close(self):
        self.working = False
        if self.ws:
            self.ws.close()

    def subscribe(self, streams: list, msg_id=None):
        if not isinstance(self.stream, list):
            raise WebsocketError('Websocket является однопоточным')
        if isinstance(streams, str):
            streams = [streams]
        if len(self.stream) + len(streams) > self.streams_limit:
            raise WebsocketError(f'Слишком много потоков (максимум {self.streams_limit})')
        self.stream.extend(streams)
        msg = {
            "method": "SUBSCRIBE",
            "params": streams,
            "id": msg_id or int(time.time() * 1000)
        }
        self.ws.send(ujson.dumps(msg))

    def unsubscribe(self, streams: list, msg_id=None):
        if not isinstance(self.stream, list):
            raise WebsocketError('Websocket является однопоточным')
        if isinstance(streams, str):
            streams = [streams]
        self.stream = [stream for stream in self.stream if stream not in streams]
        msg = {
            "method": "UNSUBSCRIBE",
            "params": streams,
            "id": msg_id or int(time.time() * 1000)
        }
        self.ws.send(ujson.dumps(msg))

    def listen_key_update_service(self):
        while self.working:
            try:
                time.sleep(self.listen_key_update_timer * 60)
                self.update_listen_key()
            except Exception as e:
                if self.on_error:
                    try:
                        self.on_error(self.ws, e)
                    except:
                        pass

    def get_listen_key(self, params=None):
        with requests.post(self.listen_key_url, params=params, headers=self.headers) as response:
            if response.status_code >= 400:
                raise WebsocketError(response.text)
            try:
                data = response.json()
                return data['listenKey']
            except ValueError:
                raise WebsocketError(f'Некорректный ответ: {response.text}')

    def update_listen_key(self, params=None):
        requests.put(self.listen_key_url, data=params, headers=self.headers)

class WebsocketAsync:
    base_url: str
    reconnect_timeout = 30
    listen_key_update_timer = 10
    streams_limit = 200

    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None):
        self.stream = stream
        if not api_key:
            if not self.stream:
                self.stream = []
            elif isinstance(self.stream, list) and len(self.stream) > self.streams_limit:
                raise WebsocketError(f'Слишком много потоков (максимум {self.streams_limit})')
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error
        self.api_key = api_key
        self.testnet = testnet
        self.listen_key_url = listen_key_url
        self.working = True
        self.connected = False
        self.listen_key = None
        self.ws = None
        if self.api_key:
            self.headers = {
                'Accept': 'application/json',
                'X-MBX-APIKEY': self.api_key
            }
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def run(self):
        asyncio.create_task(self._run())
        if self.api_key:
            asyncio.create_task(self.listen_key_update_service())

    async def _run(self):
        while self.working:
            self.connected = False
            try:
                if self.api_key:
                    self.listen_key = await self.get_listen_key()
                    url = f"{self.base_url}/ws/{self.listen_key}"
                elif isinstance(self.stream, list):
                    url = f"{self.base_url}/stream?streams={'/'.join(self.stream)}"
                else:
                    url = f"{self.base_url}/ws/{self.stream}"
                while True:
                    try:
                        async with aiohttp.ClientSession() as session:
                            async with session.ws_connect(url) as self.ws:
                                self.connected = True
                                if self.on_open:
                                    await self.on_open(self.ws)
                                async for msg in self.ws:
                                    if msg.type == aiohttp.WSMsgType.TEXT:
                                        data = msg.data
                                        try:
                                            data = ujson.loads(data)
                                        except ujson.JSONDecodeError:
                                            pass
                                        try:
                                            if self.on_message:
                                                await self.on_message(self.ws, data)
                                            if data.get('e') == 'listenKeyExpired':
                                                self.listen_key = None
                                                await self.ws.close()
                                                break
                                        except Exception as e:
                                            if self.on_error:
                                                try:
                                                    await self.on_error(self.ws, e)
                                                except:
                                                    pass
                                    elif msg.type == aiohttp.WSMsgType.ERROR:
                                        if self.on_error:
                                            try:
                                                await self.on_error(self.ws, msg)
                                            except:
                                                pass
                                        break
                    except aiohttp.ClientConnectionError as e:
                        if self.on_error:
                            try:
                                await self.on_error(self.ws, e)
                            except:
                                pass
                    except asyncio.CancelledError:
                        break
            except Exception as e:
                if self.on_error:
                    try:
                        await self.on_error(self.ws, e)
                    except:
                        pass
            finally:
                if not self.connected:
                    await asyncio.sleep(self.reconnect_timeout)

    async def close(self):
        self.working = False
        if self.ws:
            await self.ws.close()

    async def subscribe(self, streams: list, msg_id=None):
        if not isinstance(self.stream, list):
            raise WebsocketError('Websocket является однопоточным')
        if isinstance(streams, str):
            streams = [streams]
        if len(self.stream) + len(streams) > self.streams_limit:
            raise WebsocketError(f'Слишком много потоков (максимум {self.streams_limit})')
        self.stream.extend(streams)
        msg = {
            "method": "SUBSCRIBE",
            "params": streams,
            "id": msg_id or int(time.time() * 1000)
        }
        await self.ws.send_str(ujson.dumps(msg))

    async def unsubscribe(self, streams: list, msg_id=None):
        if not isinstance(self.stream, list):
            raise WebsocketError('Websocket является однопоточным')
        if isinstance(streams, str):
            streams = [streams]
        self.stream = [stream for stream in self.stream if stream not in streams]
        msg = {
            "method": "UNSUBSCRIBE",
            "params": streams,
            "id": msg_id or int(time.time() * 1000)
        }
        await self.ws.send_str(ujson.dumps(msg))

    async def listen_key_update_service(self):
        while self.working:
            try:
                await asyncio.sleep(self.listen_key_update_timer * 60)
                await self.update_listen_key()
            except Exception as e:
                if self.on_error:
                    try:
                        await self.on_error(self.ws, e)
                    except:
                        pass

    async def get_listen_key(self, params=None):
        async with self.session.post(self.listen_key_url, params=params) as response:
            if response.status >= 400:
                raise WebsocketError(response.text)
            try:
                data = await response.json()
                return data['listenKey']
            except ValueError:
                raise WebsocketError(f'Некорректный ответ: {response.text}')

    async def update_listen_key(self, params=None):
        await self.session.put(self.listen_key_url, data=params)