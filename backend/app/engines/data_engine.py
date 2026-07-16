from app.services.mexc_client import MEXCClient
from app.core.config import settings


class DataEngine:
    def __init__(self):
        self.client = MEXCClient()

    async def fetch_top_gainers(self):
        tickers = await self.client.get_ticker_24h()

        usdt = [t for t in tickers if t.get('symbol', '').endswith('USDT')]
        usdt.sort(key=lambda x: float(x.get('priceChangePercent', 0)), reverse=True)

        return usdt[: settings.MAX_GAINERS]

    async def load_market_data(self):
        result = []
        gainers = await self.fetch_top_gainers()

        for coin in gainers:
            symbol = coin['symbol']
            candles = await self.client.get_klines(symbol)
            depth = await self.client.get_depth(symbol)

            result.append({
                'symbol': symbol,
                'ticker': coin,
                'candles': candles,
                'orderbook': depth,
            })

        return result
