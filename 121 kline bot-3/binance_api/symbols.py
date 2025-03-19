import math


class Symbol:
    symbol: str

    def __init__(self, symbol):
        for key, value in symbol.items():
            if key == 'filters':
                for f in value:
                    for key_f, value_f in f.items():
                        if key_f != 'filterType':
                            value_f = self.str_to_float(value_f)
                            key_f = self.name_format(key_f)
                            if key_f == 'limit':
                                key_f = f['filterType'].lower()
                            if hasattr(self, key_f) and getattr(self, key_f) is not None:
                                key_f += f"_{f['filterType'].split('_')[0].lower()}"
                            if key_f.endswith('_size'):
                                value_f = -int(math.log10(value_f))
                            setattr(self, key_f, value_f)
            else:
                setattr(self, self.name_format(key), self.str_to_float(value))

    @staticmethod
    def str_to_float(value):
        if isinstance(value, str):
            try:
                value = float(value)
            except:
                pass
        return value

    @staticmethod
    def name_format(value):
        result = [value[0].lower()]
        for char in value[1:]:
            if char.isupper():
                result.extend(['_', char.lower()])
            else:
                result.append(char)
        return ''.join(result)


class SymbolSpot(Symbol):
    symbol: str
    status: str
    base_asset: str
    base_asset_precision: int
    quote_asset: str
    quote_precision: int
    quote_asset_precision: int
    base_commission_precision: int
    quote_commission_precision: int
    order_types: list
    iceberg_allowed: bool
    oco_allowed: bool
    quote_order_qty_market_allowed: bool
    allow_trailing_stop: bool
    cancel_replace_allowed: bool
    is_spot_trading_allowed: bool
    is_margin_trading_allowed: bool
    min_price: float
    max_price: float
    tick_size: int
    min_qty: float
    max_qty: float
    step_size: int
    iceberg_parts: int
    min_qty_market: float
    max_qty_market: float
    step_size_market: float
    min_trailing_above_delta: int
    max_trailing_above_delta: int
    min_trailing_below_delta: int
    max_trailing_below_delta: int
    bid_multiplier_up: float
    bid_multiplier_down: float
    ask_multiplier_up: float
    ask_multiplier_down: float
    avg_price_mins: int
    min_notional: float
    apply_min_to_market: bool
    max_notional: float
    apply_max_to_market: bool
    avg_price_mins_notional: int
    max_num_orders: int
    max_num_algo_orders: int
    permissions: list
    default_self_trade_prevention_mode: str
    allowed_self_trade_prevention_modes: list


class SymbolFutures(Symbol):
    symbol: str
    pair: str
    contract_type: str
    delivery_date: int
    onboard_date: int
    status: str
    maint_margin_percent: str
    required_margin_percent: str
    base_asset: str
    quote_asset: str
    margin_asset: str
    price_precision: int
    quantity_precision: int
    base_asset_precision: int
    quote_precision: int
    underlying_type: str
    underlying_sub_type: list
    settle_plan: int
    trigger_protect: str
    liquidation_fee: str
    market_take_bound: str
    max_move_order_limit: int
    max_price: float
    min_price: float
    tick_size: int
    step_size: int
    max_qty: float
    min_qty: float
    min_qty_market: float
    step_size_market: float
    max_qty_market: float
    max_num_orders: int
    max_num_algo_orders: int
    notional: float
    multiplier_decimal: float
    multiplier_up: float
    multiplier_down: float
    order_types: list
    time_in_force: list


class SymbolDelivery(Symbol):
    symbol: str
    pair: str
    contract_type: str
    delivery_date: int
    onboard_date: int
    contract_status: str
    contract_size: int
    margin_asset: str
    maint_margin_percent: str
    required_margin_percent: str
    base_asset: str
    quote_asset: str
    price_precision: int
    quantity_precision: int
    base_asset_precision: int
    quote_precision: int
    equal_qty_precision: int
    max_move_order_limit: int
    trigger_protect: str
    underlying_type: str
    underlying_sub_type: list
    min_price: float
    max_price: float
    tick_size: int
    step_size: int
    max_qty: float
    min_qty: float
    step_size_market: float
    max_qty_market: float
    min_qty_market: float
    max_num_orders: int
    max_num_algo_orders: int
    multiplier_down: float
    multiplier_up: float
    multiplier_decimal: float
    order_types: list
    time_in_force: list
    liquidation_fee: str
    market_take_bound: str