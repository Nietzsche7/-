from .error import ClientException, ServerException
from .symbols import Symbol
import requests
import aiohttp
import ujson
import time
import hmac
import hashlib
from urllib.parse import urlencode


class Client:
    base_url: str
    _symbol_class = Symbol

    def __init__(self, api_key=None, secret_key=None, testnet=False, asynced=False):
        self.api_key = api_key
        self.secret_key = secret_key
        self.testnet = testnet
        self.asynced = False
        self.headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        if api_key and secret_key:
            self.headers["X-MBX-APIKEY"] = api_key
        if asynced:
            self._set_async()
        else:
            self.session = requests.Session()
            self.session.headers.update(self.headers)

    def _set_async(self):
        if not self.asynced:
            self.asynced = True
            self.session = aiohttp.ClientSession(headers=self.headers)
            self.close = self._close_async

    def close(self):
        if self.session:
            self.session.close()

    async def _close_async(self):
        if self.session:
            await self.session.close()

    async def __aenter__(self):
        self._set_async()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._close_async()

    def _get_signature(self, query):
        return hmac.new(self.secret_key.encode('utf-8'), query.encode('utf-8'), hashlib.sha256).hexdigest()

    def _prepare_data(self, data, sign):
        new_data = {}
        for key, value in sorted(data.items()):
            if value and key not in ('self', 'signature', 'timestamp'):
                if key.startswith('_'):
                    key = key[1:]
                if isinstance(value, list):
                    new_data[key] = ujson.dumps(value)
                else:
                    new_data[key] = str(value)
        if sign:
            new_data['timestamp'] = str(int(time.time() * 1000))
            new_data = urlencode(new_data)
            new_data += '&signature=' + self._get_signature(new_data)
        else:
            new_data = urlencode(new_data)
        return new_data

    def request(self, method, url, data=None, sign=False):
        if self.asynced:
            return self._request_async(method, url, data, sign)
        else:
            return self._request_sync(method, url, data, sign)

    def _request_sync(self, method, url, data, sign):
        data = self._prepare_data(data, sign)
        with getattr(self.session, method.lower())(self.base_url + url, params=data) as response:
            return self._response(response.status_code, response.headers, response.text)

    async def _request_async(self, method, url, data, sign):
        data = self._prepare_data(data, sign)
        method = method.lower()
        kwargs = {'data': data} if method != 'get' else {'params': data}
        async with getattr(self.session, method)(self.base_url + url, **kwargs) as response:
            return self._response(response.status, dict(response.headers), await response.text())

    @staticmethod
    def _response(code, headers, text):
        if 400 <= code < 500:
            try:
                error = ujson.loads(text)
            except ujson.JSONDecodeError:
                raise ClientException(code, text, headers)
            raise ClientException(code, text, headers, error['code'], error['msg'])
        elif code >= 500:
            raise ServerException(code, text)
        try:
            data = ujson.loads(text)
        except ujson.JSONDecodeError:
            data = text
        return data

    def load_symbols(self):
        if self.asynced:
            return self._load_symbols_async()
        else:
            return self._parse_symbols(self.exchange_info()['symbols'])

    async def _load_symbols_async(self):
        return self._parse_symbols(((await self.exchange_info())['symbols']))

    def _parse_symbols(self, symbols):
        result = {}
        for symbol in symbols:
            symbol = self._symbol_class(symbol)
            result[symbol.symbol] = symbol
        return result


