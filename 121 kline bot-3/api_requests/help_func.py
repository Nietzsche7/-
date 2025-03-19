import math
from config import api_key,api_secret
import binance_api
from settings import deposit_part

client = binance_api.Futures(api_key=api_key, secret_key=api_secret)


def round_s(value, round_size, round_direction=''):
    if round_direction.lower() == 'up':
        value = math.ceil(float(value) / float(round_size)) * float(round_size)
    elif round_direction.lower() == 'down':
        value = math.floor(float(value) / float(round_size)) * float(round_size)
    else:
        value = round(float(value) / float(round_size)) * float(round_size)
    return float(format(value, f".{int(round(-math.log(round_size, 10)))}f"))

def get_tick_size(symbol):
    futures_info = client.exchange_info()
    for x in range(0, len(futures_info['symbols'])):
        symbol_info = futures_info['symbols'][x]['symbol']
        if symbol_info == symbol:
            size_step = float(futures_info['symbols'][x]['filters'][0]['tickSize'])
            return size_step

def getPrecision(symbol,spot_info):
    for x in range(0, len(spot_info['symbols'])):
        symbol_info = spot_info['symbols'][x]['symbol']
        if symbol_info == symbol:
            limit_precision = spot_info['symbols'][x]['filters'][0]['minPrice']
            order_ava = spot_info['symbols'][x]['orderTypes']
            #print(datetime.now(),spot_info['symbols'][x])
            qty = spot_info['symbols'][x]['filters'][1]['minQty']
            limit_precision = cut_zeros(limit_precision)
            qty = cut_zeros(qty)
            qty = count(qty)
            limit_precision = count(limit_precision)
            return qty, limit_precision
def cut_zeros(n):
    n = str(n)
    dec_part = n.rstrip('0')
    return dec_part
def count(n):
    num_str = str(n)
    try:
        decimal_count = len(num_str.split('.')[1])
    except IndexError:
        decimal_count = 0
    return decimal_count

def part_balance_converter_to_usdt(balance,part):
    return round(float(float(balance) * part/100),2)

async def get_depo():
    client = binance_api.Futures(api_key=api_key, secret_key=api_secret, asynced=True)
    balance = await client.balance()

    for coin in balance:
        if float(coin['availableBalance']) != 0 and coin['asset'] == "BNFCR":
            depo = float(coin['availableBalance'])
            await client.close()
            return part_balance_converter_to_usdt(depo,deposit_part)


