class Endpoints:
    def ping(self):
        return self.request('get', '/dapi/v1/ping', locals())

    def time(self):
        return self.request('get', '/dapi/v1/time', locals())

    def exchange_info(self):
        return self.request('get', '/dapi/v1/exchangeInfo', locals())

    def depth(self, symbol:str, limit:int=None):
        return self.request('get', '/dapi/v1/depth', locals())

    def trades(self, symbol:str, limit:int=None):
        return self.request('get', '/dapi/v1/trades', locals())

    def historical_trades(self, symbol:str, limit:int=None, fromId:int=None):
        return self.request('get', '/dapi/v1/historicalTrades', locals())

    def agg_trades(self, symbol:str, fromId:int=None, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/aggTrades', locals())

    def mark_price(self, symbol:str=None, pair:str=None):
        return self.request('get', '/dapi/v1/premiumIndex', locals())

    def funding_rate(self, symbol:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/fundingRate', locals())

    def klines(self, symbol:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/klines', locals())

    def continuous_klines(self, pair:str, contractType:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/continuousKlines', locals())

    def index_price_klines(self, pair:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/indexPriceKlines', locals())

    def mark_price_klines(self, symbol:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/dapi/v1/markPriceKlines', locals())

    def ticker_24hr_price_change(self, symbol:str=None, pair:str=None):
        return self.request('get', '/dapi/v1/ticker/24hr', locals())

    def ticker_price(self, symbol:str=None, pair:str=None):
        return self.request('get', '/dapi/v1/ticker/price', locals())

    def book_ticker(self, symbol:str=None, pair:str=None):
        return self.request('get', '/dapi/v1/ticker/bookTicker', locals())

    def open_interest(self, symbol:str):
        return self.request('get', '/dapi/v1/openInterest', locals())

    def open_interest_hist(self, pair:str, contractType:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/openInterestHist', locals())

    def top_long_short_account_ratio(self, pair:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/topLongShortAccountRatio', locals())

    def top_long_short_position_ratio(self, pair:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/topLongShortPositionRatio', locals())

    def long_short_account_ratio(self, pair:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/globalLongShortAccountRatio', locals())

    def taker_long_short_ratio(self, pair:str, contractType:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/takerBuySellVol', locals())

    def basis(self, pair:str, contractType:str, period:str, limit:int=None, startTime:int=None, endTime:int=None):
        return self.request('get', '/futures/data/basis', locals())

    def change_position_mode(self, dualSidePosition:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/positionSide/dual', locals(), sign=True)

    def get_position_mode(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/positionSide/dual', locals(), sign=True)

    def modify_order(self, symbol:str, side:str, type:str, positionSide:str=None, timeInForce:str=None, quantity:float=None, reduceOnly:str=None, price:float=None, newClientOrderId:str=None, stopPrice:float=None, closePosition:str=None, activationPrice:float=None, callbackRate:float=None, workingType:str=None, priceProtect:str=None, newOrderRespType:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/order', locals(), sign=True)

    def new_batch_order(self, batchOrders:list, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/batchOrders', locals(), sign=True)

    def modify_batch_order(self, batchOrders:list, recvWindow:int=None, timestamp:int=None):
        return self.request('put', '/dapi/v1/batchOrders', locals(), sign=True)

    def order_modify_history(self, symbol:str, orderId:int=None, origClientOrderId:str=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/orderAmendment', locals(), sign=True)

    def query_order(self, symbol:str, orderId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/order', locals(), sign=True)

    def cancel_order(self, symbol:str, orderId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/dapi/v1/order', locals(), sign=True)

    def cancel_open_orders(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/dapi/v1/allOpenOrders', locals(), sign=True)

    def cancel_batch_order(self, symbol:str, orderIdList:list=None, origClientOrderIdList:list=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/dapi/v1/batchOrders', locals(), sign=True)

    def countdown_cancel_order(self, symbol:str, countdownTime:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/countdownCancelAll', locals(), sign=True)

    def get_open_orders(self, symbol:str, orderId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/openOrder', locals(), sign=True)

    def get_orders(self, symbol:str=None, pair:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/openOrders', locals(), sign=True)

    def get_all_orders(self, symbol:str=None, pair:str=None, orderId:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/allOrders', locals(), sign=True)

    def balance(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/balance', locals(), sign=True)

    def account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/account', locals(), sign=True)

    def change_leverage(self, symbol:str, leverage:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/leverage', locals(), sign=True)

    def change_margin_type(self, symbol:str, marginType:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/marginType', locals(), sign=True)

    def modify_isolated_position_margin(self, symbol:str, amount:float, type:int, positionSide:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/dapi/v1/positionMargin', locals(), sign=True)

    def get_position_margin_history(self, symbol:str, type:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/positionMargin/history', locals(), sign=True)

    def get_position_risk(self, marginAsset:str=None, pair:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/positionRisk', locals(), sign=True)

    def get_account_trades(self, symbol:str=None, pair:str=None, orderId:str=None, startTime:int=None, endTime:int=None, fromId:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/userTrades', locals(), sign=True)

    def get_income_history(self, symbol:str=None, incomeType:str=None, startTime:int=None, endTime:int=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/income', locals(), sign=True)

    def leverage_brackets(self, pair:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/leverageBracket', locals(), sign=True)

    def leverage_brackets(self, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v2/leverageBracket', locals(), sign=True)

    def force_orders(self, symbol:str=None, autoCloseType:str=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/forceOrders', locals(), sign=True)

    def adl_quantile(self, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/adlQuantile', locals(), sign=True)

    def commission_rate(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/dapi/v1/commissionRate', locals(), sign=True)

    def new_listen_key(self):
        return self.request('post', '/dapi/v1/listenKey', locals())

    def renew_listen_key(self):
        return self.request('put', '/dapi/v1/listenKey', locals())

    def close_listen_key(self):
        return self.request('delete', '/dapi/v1/listenKey', locals())

    def pm_exchange_info(self, symbol:str=None, pair:str=None):
        return self.request('get', '/dapi/v1/pmExchangeInfo', locals())

