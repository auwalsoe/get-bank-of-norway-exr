"""Module showing how to get the latest currency rates from
the Bank of Norway."""
import requests
from bs4 import BeautifulSoup
from currency import BonCurrency

EXR_RESPONSE = requests.get('https://data.norges-bank.no/api/data/EXR/B..NOK.SP?lastNObservations=1')
EXR_SOUP = BeautifulSoup(EXR_RESPONSE.text, 'lxml-xml')
CURRENCIES = []
for  serie in EXR_SOUP.find_all('Series'):

    CURRENCIES.append(BonCurrency(freq=serie.get('FREQ'),
                                  base_cur=serie.get('BASE_CUR'),
                                  tenor=serie.get('TENOR'),
                                  decimals=serie.get('DECIMALS'),
                                  calculated=serie.get('CALCULATED'),
                                  unit_mult=serie.get('UNIT_MULT'),
                                  collection=serie.get('COLLECTION'),
                                  time_period=serie.Obs.get('TIME_PERIOD'),
                                  obs_value=serie.Obs.get('OBS_VALUE')))

for currency in CURRENCIES:
    currency.simple_print()