import httpx

from app.core.config import settings


class MEXCClient:
    def __init__(self):
        self.base_url = settings.MEXC_BASE_URL
        self.timeout = settings.REQUEST_TIMEOUT

    async def _get(self, endpoint: str, params: dict | None = None):
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}{endpoint}", params=params)
            response.raise_for_status()
            return response.json()

    async def get_ticker_24h(self):
        return await self._get("/api/v3/ticker/24hr")

    async def get_klines(self, symbol: str, interval: str = None, limit: int = None):
        return await self._get("/api/v3/klines", {
            "symbol": symbol,
            "interval": interval or settings.DEFAULT_INTERVAL,
            "limit": limit or settings.DEFAULT_LIMIT,
        })

    async def get_depth(self, symbol: str, limit: int = 100):
        return await self._get("/api/v3/depth", {
            "symbol": symbol,
            "limit": limit,
        })
