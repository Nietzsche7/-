import binance_api
from api_requests.help_func import getPrecision,get_tick_size,get_depo
from config import api_key,api_secret
from settings import deposit_part,stop,take,symbols,tradingPairsLimit
import asyncio
from data.sender import trading_pairs
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from config import tg_token_main,admin_id,tg_token_test
from stream.user_stream import format_exit_signal,format_trade_signal

bot_main = Bot(tg_token_main, default=DefaultBotProperties(parse_mode='HTML'))
bot_test = Bot(tg_token_test, default=DefaultBotProperties(parse_mode='HTML'))
async def place_market_order(symbol,side,price):
    client = binance_api.Futures(api_key=api_key, secret_key=api_secret,asynced=True)

    futures_info = await client.exchange_info()
    qty_p,limit = getPrecision(symbol,futures_info)
    deposit = await get_depo()
    qty = round(deposit / price, qty_p)

    if side == "BUY":
        take_profit_price = round(price * (1 + take / 100), limit)  # Увеличение для лонга
        stop_market_price = round(price * (1 - stop / 100), limit)  # Уменьшение для лонга
    elif side == "SELL":
        take_profit_price = round(price * (1 - take / 100), limit)  # Уменьшение для шорта
        stop_market_price = round(price * (1 + stop / 100), limit)  # Увеличение для шорта

    if trading_pairs.test_trading_symbol[symbol]['in_pos'] is False:
        trading_pairs.test_trading_symbol[symbol]['take'] = take_profit_price
        trading_pairs.test_trading_symbol[symbol]['stop'] = stop_market_price
        trading_pairs.test_trading_symbol[symbol]['enter'] = price
        trading_pairs.test_trading_symbol[symbol]['side'] = side
        trading_pairs.test_trading_symbol[symbol]['in_pos'] = True
        msg = format_trade_signal(symbol,side,price,take_profit_price,stop_market_price,"Binance")
        msg_id = await bot_test.send_message(chat_id=admin_id,text=msg)
        trading_pairs.test_trading_symbol[symbol]['signals'] = msg_id


    if trading_pairs.trading_status == "on" and\
            trading_pairs.trading_symbols[symbol]['in_pos'] is False and\
            trading_pairs.trading_symbols['pairs_in_pos'] < tradingPairsLimit:

        if side == "BUY" and trading_pairs.trading_symbols['short_only'] is True:
            await client.close()
            return

        if side == "SELL" and trading_pairs.trading_symbols['long_only'] is True:
            await client.close()
            return

        market_order = await client.new_order(symbol=symbol,side=side,quantity=qty,type="MARKET")

        opposite_side = "SELL" if side == "BUY" else "BUY"

        take_order = await client.new_order(symbol=symbol, side=opposite_side,stopPrice=take_profit_price, closePosition="true",type="TAKE_PROFIT_MARKET")
        stop_order = await client.new_order(symbol=symbol, side=opposite_side, stopPrice=stop_market_price, closePosition="true",type="STOP_MARKET")

        trading_pairs.trading_symbols[symbol]['take'] = take_profit_price
        trading_pairs.trading_symbols[symbol]['stop'] = stop_market_price
        signal_message = format_trade_signal(symbol,side, price, take_profit_price, stop_market_price,"Binance")
        msg = await bot_main.send_message(chat_id=admin_id, text=signal_message)
        trading_pairs.trading_symbols[symbol]['signals'] = msg
        trading_pairs.trading_symbols[symbol]['in_pos'] = True
        trading_pairs.trading_symbols[symbol]['side'] = side
        trading_pairs.trading_symbols['pairs_in_pos'] += 1

    await client.close()


if __name__ == '__main__':
    asyncio.run(place_market_order("XRPUSDT","BUY",0.5402))
