from settings import symbols
import asyncio
from datetime import datetime

class TradingPairs:
    def __init__(self):
        self.trading_symbols = {
            "stop_count": 0,
            "pairs_in_pos": 0,
            "short_only": False,
            "long_only": False,
        }
        self.test_trading_symbol = {

        }

        self.trading_status = "on"

        for symbol in symbols:
            self.trading_symbols[symbol] = {"in_pos": False,
                                            "side": None,
                                            "signals": None,
                                            "take": None,
                                            "stop": None,
                                            "enter": None}

            self.test_trading_symbol[symbol] = {"in_pos": False,
                                            "side": None,
                                            "signals": None,
                                            "take": None,
                                            "stop": None,
                                            "enter": None}


async def data_checker():
    while True:
        current_time = datetime.now()
        if current_time.hour == 0 and current_time.minute == 0:
            # Если время 00:00, обнуляем stop_count
            trading_pairs.trading_symbols['stop_count'] = 0
            print("00:00 - Новые сутки начались, stop_count обнулён")

        # Проверяем раз в минуту
        await asyncio.sleep(60)

trading_pairs = TradingPairs()

