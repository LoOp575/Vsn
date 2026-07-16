import math

class BayesianBrain:
    @staticmethod
    def sigmoid(x: float) -> float:
        return 1.0/(1.0+math.exp(-x))

    @staticmethod
    def posterior(momentum: float, volatility: float, entropy: float, drop_probability: float) -> dict:
        score=(momentum*4.0)-(volatility*2.0)-(entropy*0.5)-(drop_probability*3.0)
        confidence=BayesianBrain.sigmoid(score)
        return {
            'score': score,
            'confidence': confidence,
            'signal': 'BUY' if confidence>0.7 else 'SELL' if confidence<0.3 else 'HOLD'
        }
