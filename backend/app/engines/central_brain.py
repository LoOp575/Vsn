class CentralBrain:
    def evaluate(self, regime: dict, transition: dict, bayesian: dict, anomaly_flags: list[bool]):
        risk='LOW'
        if regime.get('regime')=='HIGH_VOLATILITY' or any(anomaly_flags):
            risk='HIGH'
        confidence=bayesian.get('confidence',0.0)
        signal=bayesian.get('signal','HOLD')
        if risk=='HIGH' and signal=='BUY':
            signal='HOLD'
        return {
            'signal':signal,
            'confidence':confidence,
            'risk':risk,
            'transition':transition,
            'regime':regime.get('regime')
        }
