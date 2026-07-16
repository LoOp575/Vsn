import numpy as np

class EntropyEngine:
    @staticmethod
    def shannon_entropy(values, bins=20):
        data=np.asarray(values,dtype=float)
        if len(data)==0:
            return 0.0
        hist,_=np.histogram(data,bins=bins,density=True)
        hist=hist[hist>0]
        p=hist/hist.sum()
        return float(-np.sum(p*np.log2(p)))

    @staticmethod
    def market_state(close):
        e=EntropyEngine.shannon_entropy(close)
        if e<1.5:
            return "TRENDING"
        if e<2.5:
            return "TRANSITION"
        return "CHAOTIC"
