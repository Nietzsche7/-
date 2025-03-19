from .client import Client
from .websockets import WebsocketSync, WebsocketAsync
from .endpoints.futures import Endpoints
from .symbols import SymbolFutures


class Futures(Client, Endpoints):
    _symbol_class = SymbolFutures

    def __init__(self, api_key=None, secret_key=None, testnet=False, asynced=False):
        self.base_url = 'https://testnet.binancefuture.com' if testnet else 'https://fapi.binance.com'
        super().__init__(api_key, secret_key, testnet=testnet, asynced=asynced)

    def load_symbols(self) -> dict[str, SymbolFutures]:
        return super().load_symbols()

    def websocket(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None):
        if self.asynced:
            return self._websocket_async(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                         on_error=on_error)
        else:
            return FuturesWebsocketSync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                        on_error=on_error, testnet=self.testnet)

    async def _websocket_async(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None):
        ws = FuturesWebsocketAsync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                   on_error=on_error, testnet=self.testnet)
        await ws.run()
        return ws

    def websocket_userdata(self, on_message=None, on_open=None, on_close=None, on_error=None):
        listen_key_url = f'{self.base_url}/fapi/v1/listenKey'
        if self.asynced:
            return self._websocket_userdata_async(on_message=on_message, on_open=on_open, on_close=on_close,
                                                  on_error=on_error, listen_key_url=listen_key_url)
        else:
            return FuturesWebsocketSync(on_message=on_message, on_open=on_open, on_close=on_close,
                                        on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                        listen_key_url=listen_key_url)

    async def _websocket_userdata_async(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None,
                                        listen_key_url=None):
        ws = FuturesWebsocketAsync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                   on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                   listen_key_url=listen_key_url)
        await ws.run()
        return ws


class FuturesWebsocketSync(WebsocketSync):
    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None):
        self.base_url = 'wss://stream.binancefuture.com' if testnet else 'wss://fstream.binance.com'
        super().__init__(stream, on_message, on_open, on_close, on_error, testnet, api_key, listen_key_url)


class FuturesWebsocketAsync(WebsocketAsync):
    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None):
        self.base_url = 'wss://stream.binancefuture.com' if testnet else 'wss://fstream.binance.com'
        super().__init__(stream, on_message, on_open, on_close, on_error, testnet, api_key, listen_key_url)

