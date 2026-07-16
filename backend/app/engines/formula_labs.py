import numpy as np


class FormulaLabs:
    @staticmethod
    def log_returns(close):
        prices = np.asarray(close, dtype=float)
        return np.diff(np.log(prices))

    @staticmethod
    def volatility(close):
        returns = FormulaLabs.log_returns(close)
        return float(np.std(returns)) if len(returns) else 0.0

    @staticmethod
    def momentum(close, period=14):
        prices = np.asarray(close, dtype=float)
        if len(prices) <= period:
            return 0.0
        return float((prices[-1] - prices[-period]) / prices[-period])

    @staticmethod
    def max_drawdown(close):
        prices = np.asarray(close, dtype=float)
        peak = np.maximum.accumulate(prices)
        drawdown = (prices - peak) / peak
        return float(drawdown.min())

    @staticmethod
    def feature_vector(close):
        return {
            'volatility': FormulaLabs.volatility(close),
            'momentum': FormulaLabs.momentum(close),
            'max_drawdown': FormulaLabs.max_drawdown(close),
        }
