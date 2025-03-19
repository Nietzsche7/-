from .client import Client
from .websockets import WebsocketSync, WebsocketAsync
from .endpoints.spot import Endpoints
from .symbols import SymbolSpot


class Spot(Client, Endpoints):
    _symbol_class = SymbolSpot

    def __init__(self, api_key=None, secret_key=None, testnet=False, asynced=False):
        self.base_url = 'https://testnet.binance.vision' if testnet else 'https://api.binance.com'
        super().__init__(api_key, secret_key, testnet=testnet, asynced=asynced)

    def load_symbols(self) -> dict[str, SymbolSpot]:
        return super().load_symbols()

    def websocket(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None):
        if self.asynced:
            return self._websocket_async(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                         on_error=on_error)
        else:
            return SpotWebsocketSync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                     on_error=on_error, testnet=self.testnet)

    async def _websocket_async(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None):
        ws = SpotWebsocketAsync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                on_error=on_error, testnet=self.testnet)
        await ws.run()
        return ws

    def websocket_userdata(self, on_message=None, on_open=None, on_close=None, on_error=None):
        listen_key_url = f'{self.base_url}/api/v3/userDataStream'
        if self.asynced:
            return self._websocket_userdata_async(on_message=on_message, on_open=on_open, on_close=on_close,
                                                  on_error=on_error, listen_key_url=listen_key_url)
        else:
            return SpotWebsocketSync(on_message=on_message, on_open=on_open, on_close=on_close,
                                     on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                     listen_key_url=listen_key_url)

    async def _websocket_userdata_async(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None,
                                        listen_key_url=None):
        ws = SpotWebsocketAsync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                listen_key_url=listen_key_url)
        await ws.run()
        return ws

    def websocket_userdata_margin(self, on_message=None, on_open=None, on_close=None, on_error=None):
        listen_key_url = f'{self.base_url}/sapi/v1/userDataStream'
        if self.asynced:
            return self._websocket_userdata_async(on_message=on_message, on_open=on_open, on_close=on_close,
                                                  on_error=on_error, listen_key_url=listen_key_url)
        else:
            return SpotWebsocketSync(on_message=on_message, on_open=on_open, on_close=on_close,
                                     on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                     listen_key_url=listen_key_url)

    def websocket_userdata_margin_isolated(self, symbol, on_message=None, on_open=None, on_close=None, on_error=None):
        listen_key_url = f'{self.base_url}/sapi/v1/userDataStream/isolated'
        if self.asynced:
            return self._websocket_userdata_margin_isolated_async(
                on_message=on_message, on_open=on_open, on_close=on_close, on_error=on_error,
                listen_key_url=listen_key_url, listen_key_symbol=symbol
            )
        else:
            return SpotWebsocketSync(on_message=on_message, on_open=on_open, on_close=on_close,
                                     on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                     listen_key_url=listen_key_url, listen_key_symbol=symbol)

    async def _websocket_userdata_margin_isolated_async(self, stream=None, on_message=None, on_open=None, on_close=None,
                                                        on_error=None, listen_key_url=None, listen_key_symbol=None):
        ws = SpotWebsocketAsync(stream=stream, on_message=on_message, on_open=on_open, on_close=on_close,
                                on_error=on_error, testnet=self.testnet, api_key=self.api_key,
                                listen_key_url=listen_key_url, listen_key_symbol=listen_key_symbol)
        await ws.run()
        return ws


class SpotWebsocketSync(WebsocketSync):
    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None, listen_key_symbol=None):
        self.base_url = 'wss://testnet.binance.vision' if testnet else 'wss://stream.binance.com'
        self.listen_key_symbol = listen_key_symbol
        super().__init__(stream, on_message, on_open, on_close, on_error, testnet, api_key, listen_key_url)

    def get_listen_key(self, params=None):
        params = {'symbol': self.listen_key_symbol} if self.listen_key_symbol else None
        return super().get_listen_key(params)

    def update_listen_key(self, params=None):
        params = {
            'listenKey': self.listen_key
        }
        if self.listen_key_symbol:
            params['symbol'] = self.listen_key_symbol
        return super().update_listen_key(params)


class SpotWebsocketAsync(WebsocketAsync):
    def __init__(self, stream=None, on_message=None, on_open=None, on_close=None, on_error=None, testnet=False,
                 api_key=None, listen_key_url=None, listen_key_symbol=None):
        self.base_url = 'wss://testnet.binance.vision' if testnet else 'wss://stream.binance.com'
        self.listen_key_symbol = listen_key_symbol
        super().__init__(stream, on_message, on_open, on_close, on_error, testnet, api_key, listen_key_url)

    async def get_listen_key(self, params=None):
        params = {'symbol': self.listen_key_symbol} if self.listen_key_symbol else None
        return await super().get_listen_key(params)

    async def update_listen_key(self, params=None):
        params = {
            'listenKey': self.listen_key
        }
        if self.listen_key_symbol:
            params['symbol'] = self.listen_key_symbol
        return await super().update_listen_key(params)