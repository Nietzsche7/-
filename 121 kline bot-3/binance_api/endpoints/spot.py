class Endpoints:
    def system_status(self):
        return self.request('get', '/sapi/v1/system/status', locals())

    def coin_info(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/capital/config/getall', locals(), sign=True)

    def account_snapshot(self, type:str, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/accountSnapshot', locals(), sign=True)

    def disable_fast_withdraw(self, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/account/disableFastWithdrawSwitch', locals(), sign=True)

    def enable_fast_withdraw(self, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/account/enableFastWithdrawSwitch', locals(), sign=True)

    def withdraw(self, coin:str, address:str, amount:float, withdrawOrderId:str=None, network:str=None, addressTag:str=None, transactionFeeFlag:bool=False, name:str=None, walletType:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/capital/withdraw/apply', locals(), sign=True)

    def deposit_history(self, includeSource:bool=False, coin:str=None, status:int=None, startTime:int=None, endTime:int=None, offset:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None, txId:str=None):
        return self.request('get', '/sapi/v1/capital/deposit/hisrec', locals(), sign=True)

    def withdraw_history(self, coin:str=None, withdrawOrderId:str=None, status:int=None, offset:int=None, limit:int=None, startTime:int=None, endTime:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/capital/withdraw/history', locals(), sign=True)

    def deposit_address(self, coin:str, network:str=None, amount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/capital/deposit/address', locals(), sign=True)

    def account_status(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/account/status', locals(), sign=True)

    def api_trading_status(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/account/apiTradingStatus', locals(), sign=True)

    def dust_log(self, startTime:int=None, endTime:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/dribblet', locals(), sign=True)

    def bnb_convertible_assets(self, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/asset/dust-btc', locals(), sign=True)

    def transfer_dust(self, asset:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/asset/dust', locals(), sign=True)

    def asset_dividend_record(self, asset:str=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/assetDividend', locals(), sign=True)

    def asset_detail(self, asset:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/assetDetail', locals(), sign=True)

    def trade_fee(self, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/tradeFee', locals(), sign=True)

    def user_universal_transfer(self, type:str, asset:str, amount:float, fromSymbol:str=None, toSymbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/asset/transfer', locals(), sign=True)

    def user_universal_transfer_history(self, type:str, startTime:int=None, endTime:int=None, current:int=None, size:int=None, fromSymbol:str=None, toSymbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/transfer', locals(), sign=True)

    def funding_wallet(self, asset:str=None, needBtcValuation:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/asset/get-funding-asset', locals(), sign=True)

    def user_asset(self, asset:str=None, needBtcValuation:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v3/asset/getUserAsset', locals(), sign=True)

    def convert_transfer(self, clientTranId:str, asset:str, amount:float, targetAsset:str, accountType:str=None):
        return self.request('post', '/sapi/v1/asset/convert-transfer', locals(), sign=True)

    def convert_history(self, startTime:int, endTime:int, tranId:int=None, clientTranId:str=None, asset:str=None, accountType:str=None, current:int=None, size:int=None):
        return self.request('get', '/sapi/v1/asset/convert-transfer/queryByPage', locals(), sign=True)

    def cloud_mining_trans_history(self, startTime:int, endTime:int, tranId:int=None, clientTranId:str=None, asset:str=None, current:int=None, size:int=None):
        return self.request('get', '/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage', locals(), sign=True)

    def api_key_permissions(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/account/apiRestrictions', locals(), sign=True)

    def convertible_coins(self):
        return self.request('get', '/sapi/v1/capital/contract/convertible-coins', locals(), sign=True)

    def toggle_auto_convertion(self, coin:str, enable:bool):
        return self.request('post', '/sapi/v1/capital/contract/convertible-coins', locals(), sign=True)

    def one_click_arrival_deposit_apply(self, depositId:int=None, txId:str=None, subAccountId:int=None, subUserId:int=None):
        return self.request('post', '/sapi/v1/capital/deposit/credit-apply', locals(), sign=True)

    def balance(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/asset/wallet/balance', locals(), sign=True)

    def sub_account_create(self, subAccountString:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/virtualSubAccount', locals(), sign=True)

    def sub_account_list(self, email:str=None, isFreeze:str=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/list', locals(), sign=True)

    def sub_account_spot_transfer_history(self, fromEmail:str=None, toEmail:str=None, startTime:int=None, endTime:int=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/sub/transfer/history', locals(), sign=True)

    def sub_account_futures_asset_transfer_history(self, email:str, futuresType:int, startTime:int=None, endTime:int=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/futures/internalTransfer', locals(), sign=True)

    def sub_account_futures_asset_transfer(self, fromEmail:str, toEmail:str, futuresType:int, asset:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/futures/internalTransfer', locals(), sign=True)

    def query_sub_account_assets(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v3/sub-account/assets', locals(), sign=True)

    def sub_account_spot_summary(self, email:str=None, page:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/spotSummary', locals(), sign=True)

    def sub_account_deposit_address(self, email:str, coin:str, network:str=None, amount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/capital/deposit/subAddress', locals(), sign=True)

    def sub_account_deposit_history(self, email:str, coin:str=None, status:int=None, startTime:int=None, endTime:int=None, limit:int=None, offset:int=None, recvWindow:int=None, timestamp:int=None, txId:str=None):
        return self.request('get', '/sapi/v1/capital/deposit/subHisrec', locals(), sign=True)

    def sub_account_status(self, email:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/status', locals(), sign=True)

    def sub_account_enable_margin(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/margin/enable', locals(), sign=True)

    def sub_account_margin_account(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/margin/account', locals(), sign=True)

    def sub_account_margin_account_summary(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/margin/accountSummary', locals(), sign=True)

    def sub_account_enable_futures(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/futures/enable', locals(), sign=True)

    def detail_on_sub_account_s_futures_account(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/futures/account', locals(), sign=True)

    def summary_of_sub_account_s_futures_account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/futures/accountSummary', locals(), sign=True)

    def futures_position_risk_of_sub_account(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/futures/positionRisk', locals(), sign=True)

    def sub_account_futures_transfer(self, email:str, asset:str, amount:float, type:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/futures/transfer', locals(), sign=True)

    def sub_account_margin_transfer(self, email:str, asset:str, amount:float, type:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/margin/transfer', locals(), sign=True)

    def sub_account_transfer_to_sub(self, toEmail:str, asset:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/transfer/subToSub', locals(), sign=True)

    def sub_account_transfer_to_master(self, asset:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/transfer/subToMaster', locals(), sign=True)

    def sub_account_transfer_sub_account_history(self, asset:str=None, type:int=None, startTime:int=None, endTime:int=None, limit:int=None, returnFailHistory:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/transfer/subUserHistory', locals(), sign=True)

    def sub_account_universal_transfer(self, fromAccountType:str, toAccountType:str, asset:str, amount:float, fromEmail:str=None, toEmail:str=None, clientTranId:str=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/universalTransfer', locals(), sign=True)

    def sub_account_universal_transfer_history(self, fromEmail:str=None, toEmail:str=None, clientTranId:str=None, startTime:int=None, endTime:int=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/universalTransfer', locals(), sign=True)

    def detail_on_sub_account_s_futures_account(self, email:str, futuresType:int, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v2/sub-account/futures/account', locals(), sign=True)

    def summary_of_sub_account_s_futures_account(self, futuresType:int, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v2/sub-account/futures/accountSummary', locals(), sign=True)

    def futures_position_risk_of_sub_account(self, email:str, futuresType:int, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v2/sub-account/futures/positionRisk', locals(), sign=True)

    def sub_account_enable_leverage_token(self, email:str, enableBlvt:bool, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/blvt/enable', locals(), sign=True)

    def sub_account_api_get_ip_restriction(self, email:str, subAccountApiKey:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/subAccountApi/ipRestriction', locals(), sign=True)

    def sub_account_api_delete_ip(self, email:str, subAccountApiKey:str, ipAddress:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList', locals(), sign=True)

    def sub_account_update_ip_restriction(self, email:str, subAccountApiKey:str, status:str, ipAddress:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v2/sub-account/subAccountApi/ipRestriction', locals(), sign=True)

    def managed_sub_account_deposit(self, toEmail:str, asset:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/managed-subaccount/deposit', locals(), sign=True)

    def managed_sub_account_assets(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/managed-subaccount/asset', locals(), sign=True)

    def managed_sub_account_withdraw(self, fromEmail:str, asset:str, amount:float, transferDate:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/managed-subaccount/withdraw', locals(), sign=True)

    def managed_sub_account_get_snapshot(self, email:str, type:str, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/managed-subaccount/accountSnapshot', locals(), sign=True)

    def managed_sub_account_trading_trans_log(self, email:str, startTime:int, endTime:int, page:int, limit:int, transfers:str=None, transferFunctionAccountType:str=None):
        return self.request('get', '/sapi/v1/managed-subaccount/queryTransLogForTradeParent', locals(), sign=True)

    def query_managed_sub_account_futures_asset_details(self, email:str):
        return self.request('get', '/sapi/v1/managed-subaccount/fetch-future-asset', locals(), sign=True)

    def query_managed_sub_account_margin_asset_details(self, email:str):
        return self.request('get', '/sapi/v1/managed-subaccount/marginAsset', locals(), sign=True)

    def query_sub_account_assets(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v4/sub-account/assets', locals(), sign=True)

    def query_managed_sub_account_list(self, email:str=None, page:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/managed-subaccount/info', locals(), sign=True)

    def query_sub_account_transaction_statistics(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/sub-account/transaction-statistics', locals(), sign=True)

    def managed_sub_account_deposit_address(self, email:str, coin:str, network:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/managed-subaccount/deposit/address', locals(), sign=True)

    def enable_options_for_sub_account(self, email:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/sub-account/eoptions/enable', locals(), sign=True)

    def query_managed_sub_account_transfer_log(self, startTime:int, endTime:int, page:int, limit:int, transfers:str=None, transferFunctionAccountType:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/managed-subaccount/query-trans-log', locals(), sign=True)

    def ping(self):
        return self.request('get', '/api/v3/ping', locals())

    def time(self):
        return self.request('get', '/api/v3/time', locals())

    def exchange_info(self):
        return self.request('get', '/api/v3/exchangeInfo', locals())

    def depth(self, symbol:str, limit:int=None):
        return self.request('get', '/api/v3/depth', locals())

    def trades(self, symbol:str, limit:int=None):
        return self.request('get', '/api/v3/trades', locals())

    def historical_trades(self, symbol:str, limit:int=None, fromId:int=None):
        return self.request('get', '/api/v3/historicalTrades', locals())

    def agg_trades(self, symbol:str, fromId:int=None, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/api/v3/aggTrades', locals())

    def klines(self, symbol:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/api/v3/klines', locals())

    def ui_klines(self, symbol:str, interval:str, startTime:int=None, endTime:int=None, limit:int=None):
        return self.request('get', '/api/v3/uiKlines', locals())

    def avg_price(self, symbol:str):
        return self.request('get', '/api/v3/avgPrice', locals())

    def ticker_24hr(self, symbol:str=None, symbols:str=None, type:str=None):
        return self.request('get', '/api/v3/ticker/24hr', locals())

    def ticker_price(self, symbol:str=None, symbols:str=None):
        return self.request('get', '/api/v3/ticker/price', locals())

    def book_ticker(self, symbol:str=None, symbols:str=None):
        return self.request('get', '/api/v3/ticker/bookTicker', locals())

    def rolling_window_ticker(self, symbol:str, windowSize:str=None, type:str=None):
        return self.request('get', '/api/v3/ticker', locals())

    def new_order_test(self, symbol:str, side:str, type:str, timeInForce:str=None, quantity:float=None, quoteOrderQty:float=None, price:float=None, newClientOrderId:str=None, strategyId:int=None, strategyType:int=None, stopPrice:float=None, trailingDelta:int=None, icebergQty:float=None, newOrderRespType:str=None, selfTradePreventionMode:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/api/v3/order/test', locals(), sign=True)

    def new_order(self, symbol:str, side:str, type:str, timeInForce:str=None, quantity:float=None, quoteOrderQty:float=None, price:float=None, newClientOrderId:str=None, strategyId:int=None, strategyType:int=None, stopPrice:float=None, trailingDelta:int=None, icebergQty:float=None, newOrderRespType:str=None, selfTradePreventionMode:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/api/v3/order', locals(), sign=True)

    def cancel_order(self, symbol:str, orderId:int=None, origClientOrderId:str=None, newClientOrderId:str=None, cancelRestrictions:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/api/v3/order', locals(), sign=True)

    def cancel_open_orders(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/api/v3/openOrders', locals(), sign=True)

    def get_order(self, symbol:str, orderId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/order', locals(), sign=True)

    def cancel_and_replace(self, symbol:str, side:str, type:str, cancelReplaceMode:str, timeInForce:str=None, quantity:float=None, quoteOrderQty:float=None, price:float=None, cancelNewClientOrderId:str=None, cancelOrigClientOrderId:str=None, cancelOrderId:int=None, newClientOrderId:str=None, strategyId:int=None, strategyType:int=None, stopPrice:float=None, trailingDelta:int=None, icebergQty:float=None, newOrderRespType:str=None, selfTradePreventionMode:str=None, cancelRestrictions:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/api/v3/order/cancelReplace', locals(), sign=True)

    def get_open_orders(self, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/openOrders', locals(), sign=True)

    def get_orders(self, symbol:str, orderId:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/allOrders', locals(), sign=True)

    def new_oco_order(self, symbol:str, side:str, quantity:float, price:float, stopPrice:float, listClientOrderId:str=None, limitClientOrderId:str=None, limitStrategyId:int=None, limitStrategyType:int=None, limitIcebergQty:float=None, trailingDelta:int=None, stopClientOrderId:str=None, stopStrategyId:int=None, stopStrategyType:int=None, stopLimitPrice:float=None, stopIcebergQty:float=None, stopLimitTimeInForce:str=None, newOrderRespType:str=None, selfTradePreventionMode:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/api/v3/order/oco', locals(), sign=True)

    def cancel_oco_order(self, symbol:str, orderListId:int=None, listClientOrderId:str=None, newClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/api/v3/orderList', locals(), sign=True)

    def get_oco_order(self, orderListId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/orderList', locals(), sign=True)

    def get_oco_orders(self, fromId:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/allOrderList', locals(), sign=True)

    def get_oco_open_orders(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/openOrderList', locals(), sign=True)

    def account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/account', locals(), sign=True)

    def my_trades(self, symbol:str, orderId:int=None, startTime:int=None, endTime:int=None, fromId:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/myTrades', locals(), sign=True)

    def get_order_rate_limit(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/rateLimit/order', locals(), sign=True)

    def query_prevented_matches(self, symbol:str, preventedMatchId:int=None, orderId:int=None, fromPreventedMatchId:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/api/v3/myPreventedMatches', locals(), sign=True)

    def margin_transfer(self, asset:str, amount:float, type:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/transfer', locals(), sign=True)

    def margin_borrow(self, asset:str, amount:float, isIsolated:str=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/loan', locals(), sign=True)

    def margin_repay(self, asset:str, amount:float, isIsolated:str=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/repay', locals(), sign=True)

    def margin_asset(self, asset:str):
        return self.request('get', '/sapi/v1/margin/asset', locals())

    def margin_pair(self, symbol:str):
        return self.request('get', '/sapi/v1/margin/pair', locals())

    def margin_all_assets(self):
        return self.request('get', '/sapi/v1/margin/allAssets', locals())

    def margin_all_pairs(self):
        return self.request('get', '/sapi/v1/margin/allPairs', locals())

    def margin_pair_index(self, symbol:str):
        return self.request('get', '/sapi/v1/margin/priceIndex', locals())

    def new_margin_order(self, symbol:str, side:str, type:str, isIsolated:str=None, quantity:float=None, quoteOrderQty:float=None, price:float=None, stopPrice:float=None, newClientOrderId:str=None, icebergQty:float=None, newOrderRespType:str=None, sideEffectType:str=None, timeInForce:str=None, selfTradePreventionMode:str=None, autoRepayAtCancel:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/order', locals(), sign=True)

    def cancel_margin_order(self, symbol:str, isIsolated:str=None, orderId:int=None, origClientOrderId:str=None, newClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/sapi/v1/margin/order', locals(), sign=True)

    def margin_open_orders_cancellation(self, symbol:str, isIsolated:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/sapi/v1/margin/openOrders', locals(), sign=True)

    def adjust_cross_margin_max_leverage(self, maxLeverage:int):
        return self.request('post', '/sapi/v1/margin/max-leverage', locals(), sign=True)

    def margin_transfer_history(self, asset:str=None, type:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/transfer', locals(), sign=True)

    def margin_load_record(self, asset:str=None, isolatedSymbol:str=None, txId:int=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/loan', locals(), sign=True)

    def margin_repay_record(self, asset:str=None, isolatedSymbol:str=None, txId:int=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/repay', locals(), sign=True)

    def margin_interest_history(self, asset:str=None, isolatedSymbol:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/interestHistory', locals(), sign=True)

    def margin_force_liquidation_record(self, startTime:int=None, endTime:int=None, isolatedSymbol:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/forceLiquidationRec', locals(), sign=True)

    def margin_account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/account', locals(), sign=True)

    def margin_order(self, symbol:str, isIsolated:str=None, orderId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/order', locals(), sign=True)

    def margin_open_orders(self, symbol:str=None, isIsolated:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/openOrders', locals(), sign=True)

    def margin_all_orders(self, symbol:str, isIsolated:str=None, orderId:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/allOrders', locals(), sign=True)

    def new_margin_oco_order(self, symbol:str, side:str, quantity:float, price:float, stopPrice:float, isIsolated:str=None, listClientOrderId:str=None, limitClientOrderId:str=None, limitIcebergQty:float=None, stopClientOrderId:str=None, stopLimitPrice:float=None, stopIcebergQty:float=None, stopLimitTimeInForce:str=None, newOrderRespType:str=None, sideEffectType:str=None, selfTradePreventionMode:str=None, autoRepayAtCancel:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/order/oco', locals(), sign=True)

    def cancel_margin_oco_order(self, symbol:str, isIsolated:str=None, orderListId:int=None, listClientOrderId:str=None, newClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/sapi/v1/margin/orderList', locals(), sign=True)

    def get_margin_oco_order(self, isIsolated:str=None, symbol:str=None, orderListId:int=None, origClientOrderId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/orderList', locals(), sign=True)

    def get_margin_oco_orders(self, isIsolated:str=None, symbol:str=None, fromId:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/allOrderList', locals(), sign=True)

    def get_margin_open_oco_orders(self, isIsolated:str=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/openOrderList', locals(), sign=True)

    def margin_my_trades(self, symbol:str, isIsolated:str=None, orderId:int=None, startTime:int=None, endTime:int=None, fromId:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/myTrades', locals(), sign=True)

    def margin_max_borrowable(self, asset:str, isolatedSymbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/maxBorrowable', locals(), sign=True)

    def margin_max_transferable(self, asset:str, isolatedSymbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/maxTransferable', locals(), sign=True)

    def summary_of_margin_account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/tradeCoeff', locals(), sign=True)

    def isolated_margin_transfer(self, asset:str, symbol:str, transFrom:str, transTo:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/isolated/transfer', locals(), sign=True)

    def isolated_margin_transfer_history(self, symbol:str, asset:str=None, type:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolated/transfer', locals(), sign=True)

    def isolated_margin_account(self, symbols:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolated/account', locals(), sign=True)

    def cancel_isolated_margin_account(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('delete', '/sapi/v1/margin/isolated/account', locals(), sign=True)

    def enable_isolated_margin_account(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/isolated/account', locals(), sign=True)

    def isolated_margin_account_limit(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolated/accountLimit', locals(), sign=True)

    def isolated_margin_pair(self, symbol:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolated/pair', locals(), sign=True)

    def isolated_margin_all_pairs(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolated/allPairs', locals(), sign=True)

    def toggle_bnbBurn(self, spotBNBBurn:str=None, interestBNBBurn:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/bnbBurn', locals(), sign=True)

    def bnbBurn_status(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bnbBurn', locals(), sign=True)

    def margin_interest_rate_history(self, asset:str, vipLevel:int=None, startTime:int=None, endTime:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/interestRateHistory', locals(), sign=True)

    def margin_fee(self, vipLevel:int=None, coin:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/crossMarginData', locals(), sign=True)

    def isolated_margin_fee(self, vipLevel:int=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolatedMarginData', locals(), sign=True)

    def isolated_margin_tier(self, symbol:str, tier:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/isolatedMarginTier', locals(), sign=True)

    def margin_order_usage(self, isIsolated:str=None, symbol:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/rateLimit/order', locals(), sign=True)

    def margin_dust_log(self, startTime:int=None, endTime:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/dribblet', locals(), sign=True)

    def get_assets_that_can_be_converted_into_bnb(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/dust', locals(), sign=True)

    def dust_transfer(self, asset:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/margin/dust', locals(), sign=True)

    def cross_margin_collateral_ratio(self):
        return self.request('get', '/sapi/v1/margin/crossMarginCollateralRatio', locals())

    def get_small_liability_exchange_coin_list(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/exchange-small-liability', locals(), sign=True)

    def get_small_liability_exchange_history(self, current:int, size:int, startTime:int=None, endTime:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/margin/exchange-small-liability-history', locals(), sign=True)

    def get_a_future_hourly_interest_rate(self, assets:str, isIsolated:bool):
        return self.request('get', '/sapi/v1/margin/next-hourly-interest-rate', locals(), sign=True)

    def new_listen_key(self):
        return self.request('post', '/api/v3/userDataStream', locals())

    def renew_listen_key(self, listenKey:str):
        return self.request('put', '/api/v3/userDataStream', locals())

    def close_listen_key(self, listenKey:str):
        return self.request('delete', '/api/v3/userDataStream', locals())

    def new_margin_listen_key(self):
        return self.request('post', '/sapi/v1/userDataStream', locals())

    def renew_margin_listen_key(self, listenKey:str):
        return self.request('put', '/sapi/v1/userDataStream', locals())

    def close_margin_listen_key(self, listenKey:str):
        return self.request('delete', '/sapi/v1/userDataStream', locals())

    def new_isolated_margin_listen_key(self, symbol:str):
        return self.request('post', '/sapi/v1/userDataStream/isolated', locals())

    def renew_isolated_margin_listen_key(self, symbol:str, listenKey:str):
        return self.request('put', '/sapi/v1/userDataStream/isolated', locals())

    def close_isolated_margin_listen_key(self, symbol:str, listenKey:str):
        return self.request('delete', '/sapi/v1/userDataStream/isolated', locals())

    def get_simple_earn_flexible_product_list(self, asset:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/list', locals(), sign=True)

    def get_simple_earn_locked_product_list(self, asset:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/list', locals(), sign=True)

    def subscribe_flexible_product(self, productId:str, amount:float, autoSubscribe:bool=False, sourceAccount:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/flexible/subscribe', locals(), sign=True)

    def subscribe_locked_product(self, projectId:str, amount:float, autoSubscribe:bool=False, sourceAccount:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/locked/subscribe', locals(), sign=True)

    def redeem_flexible_product(self, productId:str, redeemAll:bool=False, amount:float=None, destAccount:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/flexible/redeem', locals(), sign=True)

    def redeem_locked_product(self, positionId:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/locked/redeem', locals(), sign=True)

    def get_flexible_product_position(self, asset:str=None, productId:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/position', locals(), sign=True)

    def get_locked_product_position(self, asset:str=None, positionId:str=None, projectId:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/position', locals(), sign=True)

    def simple_account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/account', locals(), sign=True)

    def get_flexible_subscription_record(self, productId:str=None, purchaseId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/history/subscriptionRecord', locals(), sign=True)

    def get_locked_subscription_record(self, purchaseId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/history/subscriptionRecord', locals(), sign=True)

    def get_flexible_redemption_record(self, productId:str=None, redeemId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/history/redemptionRecord', locals(), sign=True)

    def get_locked_redemption_record(self, positionId:str=None, redeemId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/history/redemptionRecord', locals(), sign=True)

    def get_flexible_rewards_history(self, type:str, productId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/history/rewardsRecord', locals(), sign=True)

    def get_locked_rewards_history(self, positionId:str=None, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/history/rewardsRecord', locals(), sign=True)

    def set_flexible_auto_subscribe(self, productId:str, autoSubscribe:bool, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/flexible/setAutoSubscribe', locals(), sign=True)

    def set_locked_auto_subscribe(self, positionId:str, autoSubscribe:bool, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/simple-earn/locked/setAutoSubscribe', locals(), sign=True)

    def get_flexible_personal_left_quota(self, productId:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/personalLeftQuota', locals(), sign=True)

    def get_locked_personal_left_quota(self, projectId:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/personalLeftQuota', locals(), sign=True)

    def get_flexible_subscription_preview(self, productId:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/subscriptionPreview', locals(), sign=True)

    def get_locked_subscription_preview(self, projectId:str, amount:float, autoSubscribe:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/locked/subscriptionPreview', locals(), sign=True)

    def get_rate_history(self, productId:str, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/simple-earn/flexible/history/rateHistory', locals(), sign=True)

    def get_collateral_record(self):
        return self.request('get', '/sapi/v1/simple-earn/flexible/history/collateralRecord', locals(), sign=True)

    def get_target_asset_list(self, targetAsset:str=None, size:int=None, current:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/target-asset/list', locals(), sign=True)

    def get_target_asset_roi_data(self, targetAsset:str, hisRoiType:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/target-asset/roi/list', locals(), sign=True)

    def query_all_source_asset_and_target_asset(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/all/asset', locals(), sign=True)

    def query_source_asset_list(self, usageType:str, targetAsset:str=None, indexId:int=None, flexibleAllowedToUse:bool=False, sourceType:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/source-asset/list', locals(), sign=True)

    def change_plan_status(self, planId:int, status:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/lending/auto-invest/plan/edit-status', locals(), sign=True)

    def get_list_of_plans(self, planType:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/plan/list', locals(), sign=True)

    def query_holding_details_of_the_plan(self, planId:int=None, requestId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/plan/id', locals(), sign=True)

    def query_subscription_transaction_history(self, planId:int=None, startTime:int=None, endTime:int=None, targetAsset:int=None, planType:int=None, size:int=None, current:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/history/list', locals(), sign=True)

    def query_index_details(self, indexId:int, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/index/info', locals(), sign=True)

    def query_index_linked_plan_position_details(self, indexId:int, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/index/user-summary', locals(), sign=True)

    def one_time_transaction(self, sourceType:str, subscriptionAmount:float, sourceAsset:str, requestId:str=None, flexibleAllowedToUse:bool=False, planId:int=None, indexId:int=None, details:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/lending/auto-invest/one-off', locals(), sign=True)

    def query_one_time_transaction_status(self, transactionId:int, requestId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/one-off/status', locals(), sign=True)

    def index_linked_plan_redemption(self, indexId:int, redemptionPercentage:int, requestId:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/lending/auto-invest/redeem', locals(), sign=True)

    def get_index_linked_plan_redemption_history(self, requestId:int, startTime:int=None, endTime:int=None, current:int=None, asset:str=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/redeem/history', locals(), sign=True)

    def index_linked_plan_rebalance_details(self, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/lending/auto-invest/rebalance/history', locals(), sign=True)

    def staking_product_list(self, product:str, asset:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/staking/productList', locals(), sign=True)

    def staking_purchase_product(self, product:str, productId:str, amount:float, renewable:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/staking/purchase', locals(), sign=True)

    def staking_redeem_product(self, product:str, productId:str, positionId:str=None, amount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/staking/redeem', locals(), sign=True)

    def staking_product_position(self, product:str, productId:str=None, asset:str=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/staking/position', locals(), sign=True)

    def staking_history(self, product:str, txnType:str, asset:str=None, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/staking/stakingRecord', locals(), sign=True)

    def staking_set_auto_staking(self, product:str, positionId:str, renewable:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/staking/setAutoStaking', locals(), sign=True)

    def staking_product_quota(self, product:str, productId:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/staking/personalLeftQuota', locals(), sign=True)

    def mining_algo_list(self):
        return self.request('get', '/sapi/v1/mining/pub/algoList', locals())

    def mining_coin_list(self):
        return self.request('get', '/sapi/v1/mining/pub/coinList', locals())

    def mining_worker(self, algo:str, userName:str, workerName:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/worker/detail', locals(), sign=True)

    def mining_worker_list(self, algo:str, userName:str, pageIndex:int=None, sort:int=None, sortColumn:int=None, workerStatus:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/worker/list', locals(), sign=True)

    def mining_earnings_list(self, algo:str, userName:str, coin:str=None, startDate:int=None, endDate:int=None, pageIndex:int=None, pageSize:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/payment/list', locals(), sign=True)

    def mining_bonus_list(self, algo:str, userName:str, coin:str=None, startDate:int=None, endDate:int=None, pageIndex:int=None, pageSize:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/payment/other', locals(), sign=True)

    def mining_hashrate_resale_list(self, pageIndex:int=None, pageSize:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/hash-transfer/config/details/list', locals(), sign=True)

    def mining_hashrate_resale_details(self, configId:int, userName:str, pageIndex:int=None, pageSize:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/hash-transfer/profit/details', locals(), sign=True)

    def mining_hashrate_resale_request(self, userName:str, algo:str, endDate:int, startDate:int, toPoolUser:str, hashRate:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/mining/hash-transfer/config', locals(), sign=True)

    def mining_hashrate_resale_cancellation(self, configId:int, userName:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/mining/hash-transfer/config/cancel', locals(), sign=True)

    def mining_statistics_list(self, algo:str, userName:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/statistics/user/status', locals(), sign=True)

    def mining_account_list(self, algo:str, userName:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/statistics/user/list', locals(), sign=True)

    def mining_account_earning(self, algo:str, startDate:int=None, endDate:int=None, pageIndex:int=None, pageSize:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/mining/payment/uid', locals(), sign=True)

    def futures_transfer(self, asset:str, amount:float, type:int, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/futures/transfer', locals(), sign=True)

    def futures_transfer_history(self, startTime:int, asset:str=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/futures/transfer', locals(), sign=True)

    def portfolio_margin_account(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/portfolio/account', locals(), sign=True)

    def portfolio_margin_collateral_rate(self):
        return self.request('get', '/sapi/v1/portfolio/collateralRate', locals(), sign=True)

    def portfolio_margin_bankruptcy_loan_amount(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/portfolio/pmLoan', locals(), sign=True)

    def portfolio_margin_bankruptcy_loan_repay(self, _from:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/repay', locals(), sign=True)

    def query_classic_portfolio_margin_negative_balance_interest_history(self, asset:str=None, startTime:int=None, endTime:int=None, size:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/portfolio/interest-history', locals(), sign=True)

    def query_portfolio_margin_asset_index_price(self, asset:str=None):
        return self.request('get', '/sapi/v1/portfolio/asset-index-price', locals())

    def fund_auto_collection(self, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/auto-collection', locals(), sign=True)

    def fund_collection_by_asset(self, asset:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/asset-collection', locals(), sign=True)

    def bnb_transfer(self, amount:float, transferSide:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/bnb-transfer', locals(), sign=True)

    def change_auto_repay_futures_status(self, autoRepay:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/repay-futures-switch', locals(), sign=True)

    def get_auto_repay_futures_status(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/portfolio/repay-futures-switch', locals(), sign=True)

    def repay_futures_negative_balance(self, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/portfolio/repay-futures-negative-balance', locals(), sign=True)

    def blvt_info(self, tokenName:str=None):
        return self.request('get', '/sapi/v1/blvt/tokenInfo', locals())

    def subscribe_blvt(self, tokenName:str, cost:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/blvt/subscribe', locals(), sign=True)

    def subscription_record(self, tokenName:str=None, id:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/blvt/subscribe/record', locals(), sign=True)

    def redeem_blvt(self, tokenName:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/blvt/redeem', locals(), sign=True)

    def redemption_record(self, tokenName:str=None, id:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/blvt/redeem/record', locals(), sign=True)

    def user_limit_info(self, tokenName:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/blvt/userLimit', locals(), sign=True)

    def bswap_pools(self):
        return self.request('get', '/sapi/v1/bswap/pools', locals())

    def bswap_liquidity(self, poolId:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/liquidity', locals(), sign=True)

    def bswap_liquidity_add(self, poolId:int, asset:str, quantity:float, type:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/bswap/liquidityAdd', locals(), sign=True)

    def bswap_liquidity_remove(self, poolId:int, type:str, shareAmount:float, asset:list=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/bswap/liquidityRemove', locals(), sign=True)

    def bswap_liquidity_operation_record(self, operationId:int=None, poolId:int=None, operation:str=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/liquidityOps', locals(), sign=True)

    def bswap_request_quote(self, quoteAsset:str, baseAsset:str, quoteQty:float, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/quote', locals(), sign=True)

    def bswap_swap(self, quoteAsset:str, baseAsset:str, quoteQty:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/bswap/swap', locals(), sign=True)

    def bswap_swap_history(self, swapId:int=None, startTime:int=None, endTime:int=None, status:int=None, quoteAsset:str=None, baseAsset:str=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/swap', locals(), sign=True)

    def bswap_pool_configure(self, poolId:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/poolConfigure', locals(), sign=True)

    def bswap_add_liquidity_preview(self, poolId:int, type:str, quoteAsset:str, quoteQty:float, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/addLiquidityPreview', locals(), sign=True)

    def bswap_remove_liquidity_preview(self, poolId:int, type:str, quoteAsset:str, shareAmount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/removeLiquidityPreview', locals(), sign=True)

    def bswap_unclaimed_rewards(self, type:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/unclaimedRewards', locals(), sign=True)

    def bswap_claim_rewards(self, type:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/bswap/claimRewards', locals(), sign=True)

    def bswap_claimed_rewards(self, poolId:int=None, assetRewards:str=None, type:int=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/bswap/claimedHistory', locals(), sign=True)

    def fiat_order_history(self, transactionType:str, beginTime:int=None, endTime:int=None, page:int=None, rows:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/fiat/orders', locals(), sign=True)

    def fiat_payment_history(self, transactionType:str, beginTime:int=None, endTime:int=None, page:int=None, rows:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/fiat/payments', locals(), sign=True)

    def c2c_trade_history(self, tradeType:str, startTimestamp:int=None, endTimestamp:int=None, page:int=None, rows:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/c2c/orderMatch/listUserOrderHistory', locals(), sign=True)

    def loan_vip_ongoing_orders(self, orderId:int=None, collateralAccountId:int=None, loanCoin:str=None, collateralCoin:str=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/vip/ongoing/orders', locals(), sign=True)

    def loan_vip_repay(self, orderId:int, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/vip/repay', locals(), sign=True)

    def loan_vip_repay_history(self, orderId:int=None, loanCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/vip/repay/history', locals(), sign=True)

    def loan_vip_collateral_account(self, orderId:int=None, collateralAccountId:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/vip/collateral/account', locals(), sign=True)

    def loan_history(self, asset:str=None, type:str=None, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/income', locals(), sign=True)

    def loan_borrow(self, loanCoin:str, collateralCoin:str, loanTerm:int, loanAmount:float=None, collateralAmount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/borrow', locals(), sign=True)

    def loan_borrow_history(self, orderId:int=None, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/borrow/history', locals(), sign=True)

    def loan_ongoing_orders(self, orderId:int=None, loanCoin:str=None, collateralCoin:str=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/ongoing/orders', locals(), sign=True)

    def loan_repay(self, orderId:int, amount:float, type:int=None, collateralReturn:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/repay', locals(), sign=True)

    def loan_repay_history(self, orderId:int=None, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/repay/history', locals(), sign=True)

    def loan_adjust_ltv(self, orderId:int, amount:float, direction:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/adjust/ltv', locals(), sign=True)

    def loan_adjust_ltv_history(self, orderId:int=None, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/ltv/adjustment/history', locals(), sign=True)

    def loan_loanable_data(self, loanCoin:str=None, vipLevel:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/loanable/data', locals(), sign=True)

    def loan_collateral_data(self, collateralCoin:str=None, vipLevel:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/collateral/data', locals(), sign=True)

    def loan_collateral_rate(self, loanCoin:str, collateralCoin:str, repayAmount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/repay/collateral/rate', locals(), sign=True)

    def loan_customize_margin_call(self, marginCall:float, orderId:int=None, collateralCoin:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/customize/margin_call', locals(), sign=True)

    def flexible_loan_borrow(self, loanCoin:str, collateralCoin:str, loanAmount:float=None, collateralAmount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/flexible/borrow', locals(), sign=True)

    def flexible_loan_ongoing_orders(self, loanCoin:str=None, collateralCoin:str=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/ongoing/orders', locals(), sign=True)

    def flexible_loan_borrow_history(self, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/borrow/history', locals(), sign=True)

    def flexible_loan_repay(self, loanCoin:str, collateralCoin:float, repayAmount:float, collateralReturn:bool=False, fullRepayment:bool=False, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/flexible/repay', locals(), sign=True)

    def flexible_loan_repayment_history(self, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/repay/history', locals(), sign=True)

    def flexible_loan_adjust_ltv(self, loanCoin:str, collateralCoin:str, adjustmentAmount:float, direction:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/loan/flexible/adjust/ltv', locals(), sign=True)

    def flexible_loan_ltv_adjustment_history(self, loanCoin:str=None, collateralCoin:str=None, startTime:int=None, endTime:int=None, current:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/ltv/adjustment/history', locals(), sign=True)

    def flexible_loan_assets_data(self, loanCoin:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/loanable/data', locals(), sign=True)

    def flexible_loan_collateral_assets_data(self, collateralCoin:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/loan/flexible/collateral/data', locals(), sign=True)

    def pay_history(self, startTime:int=None, endTime:int=None, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/pay/transactions', locals(), sign=True)

    def list_all_convert_pairs(self, fromAsset:str=None, toAsset:str=None):
        return self.request('get', '/sapi/v1/convert/exchangeInfo', locals())

    def query_order_quantity_precision_per_asset(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/convert/assetInfo', locals(), sign=True)

    def send_quote_request(self, fromAsset:str, toAsset:str, fromAmount:float=None, toAmount:float=None, walletType:str=None, validTime:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/convert/getQuote', locals(), sign=True)

    def accept_quote(self, quoteId:str, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/convert/acceptQuote', locals(), sign=True)

    def order_status(self, orderId:str=None, quoteId:str=None):
        return self.request('get', '/sapi/v1/convert/orderStatus', locals(), sign=True)

    def get_convert_trade_history(self, startTime:int, endTime:int, limit:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/convert/tradeFlow', locals(), sign=True)

    def rebate_spot_history(self, startTime:int=None, endTime:int=None, page:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/rebate/taxQuery', locals(), sign=True)

    def nft_transaction_history(self, orderType:int, startTime:int=None, endTime:int=None, limit:int=None, page:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/nft/history/transactions', locals(), sign=True)

    def nft_deposit_history(self, startTime:int=None, endTime:int=None, limit:int=None, page:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/nft/history/deposit', locals(), sign=True)

    def nft_withdraw_history(self, startTime:int=None, endTime:int=None, limit:int=None, page:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/nft/history/withdraw', locals(), sign=True)

    def nft_asset(self, limit:int=None, page:int=None, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/nft/user/getAsset', locals(), sign=True)

    def gift_card_create_code(self, token:str, amount:float, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/giftcard/createCode', locals(), sign=True)

    def gift_card_buy_code(self, baseToken:str, faceToken:str, baseTokenAmount:float, discount:float=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/giftcard/buyCode', locals(), sign=True)

    def gift_card_redeem_code(self, code:str, externalUid:str=None, recvWindow:int=None, timestamp:int=None):
        return self.request('post', '/sapi/v1/giftcard/redeemCode', locals(), sign=True)

    def gift_card_verify_code(self, referenceNo:str, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/giftcard/verify', locals(), sign=True)

    def gift_card_rsa_public_key(self, recvWindow:int=None, timestamp:int=None):
        return self.request('get', '/sapi/v1/giftcard/cryptography/rsa-public-key', locals(), sign=True)

