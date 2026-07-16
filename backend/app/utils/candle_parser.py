from typing import List

class CandleParser:
    @staticmethod
    def close_prices(klines: List[list]) -> list[float]:
        return [float(k[4]) for k in klines if len(k) > 4]

    @staticmethod
    def volumes(klines: List[list]) -> list[float]:
        return [float(k[5]) for k in klines if len(k) > 5]
