class DecisionEngine:
    MIN_CONFIDENCE=0.65

    @classmethod
    def decide(cls, brain_output: dict):
        signal=brain_output.get('signal','HOLD')
        confidence=float(brain_output.get('confidence',0.0))
        risk=brain_output.get('risk','HIGH')

        if risk=='HIGH':
            return {'action':'NO_TRADE','reason':'high_risk',**brain_output}

        if confidence<cls.MIN_CONFIDENCE:
            return {'action':'WAIT','reason':'low_confidence',**brain_output}

        action={'BUY':'LONG','SELL':'SHORT','HOLD':'WAIT'}.get(signal,'WAIT')
        return {'action':action,'reason':'validated',**brain_output}
