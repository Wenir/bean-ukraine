"""A source fetching cryptocurrency prices from Coinbase.
Valid tickers are in the form "XXX-YYY", such as "BTC-USD".
Here is the API documentation:
https://developers.coinbase.com/api/v2
For example:
https://api.coinbase.com/v2/prices/BTC-GBP/spot
Timezone information: Input and output datetimes are specified via UTC
timestamps.
"""

import datetime
from decimal import Decimal

import requests
from dateutil.tz import tz

from beanprice import source


class CoinbaseError(ValueError):
    "An error from the Coinbase API."


def fetch_quote(ticker, time=None):
    """Fetch a quote from Coinbase."""
    if time:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}&date={}&json".format(ticker, time.strftime("%Y%m%d"))
    else:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}&json".format(ticker)

    options = {}

    response = requests.get(url, options)
    if response.status_code != requests.codes.ok:
        raise CoinbaseError("Invalid response ({}): {}".format(response.status_code,
                                                               response.text))
    result = response.json()

    price = round( Decimal(result[0]['rate']), 4 )
    time = datetime.datetime.strptime(result[0]['exchangedate'], "%d.%m.%Y").replace(tzinfo=datetime.timezone.utc)
    currency = result[0]['cc']

    return source.SourcePrice(price, time, currency)


class Source(source.Source):
    "Coinbase API price extractor."

    def get_latest_price(self, ticker):
        """See contract in beanprice.source.Source."""
        return fetch_quote(ticker)

    def get_historical_price(self, ticker, time):
        """See contract in beanprice.source.Source."""
        return fetch_quote(ticker, time)
