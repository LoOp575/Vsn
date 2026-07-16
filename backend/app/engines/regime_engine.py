import numpy as np

class RegimeEngine:
    @staticmethod
    def classify(volatility: float, momentum: float):
        if volatility > 0.08:
            return 'HIGH_VOLATILITY'
        if momentum > 0.05:
            return 'BULLISH'
        if momentum < -0.05:
            return 'BEARISH'
        return 'RANGING'

    @staticmethod
    def summarize(features: dict):
        return {
            'regime': RegimeEngine.classify(features.get('volatility',0.0), features.get('momentum',0.0)),
            'volatility': features.get('volatility',0.0),
            'momentum': features.get('momentum',0.0),
            'drawdown': features.get('max_drawdown',0.0)
        }
