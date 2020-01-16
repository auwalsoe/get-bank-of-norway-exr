"""Module containing a collection of classes useful for interacting with
the apis of the Bank Of Norway"""

class BonCurrency():
    """Class for currency series provided by The Bank of Norway"""
    QUOTE_CUR = 'NOR'
    def __init__(self, freq, base_cur, tenor, decimals,
                 calculated, unit_mult, collection, time_period, obs_value):
        self.freq = freq
        self.base_cur = base_cur
        self.tenor = tenor
        self.decimals = decimals
        self.calculated = calculated
        self.unit_mult = unit_mult
        self.collection = collection
        self.time_period = time_period
        self.obs_value = obs_value
    def simple_print(self):
        """Method for printing currency and currency value."""
        print('{} : {}'.format(self.base_cur, self.obs_value))
