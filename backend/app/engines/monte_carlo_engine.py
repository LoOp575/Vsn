import numpy as np

class MonteCarloEngine:
    @staticmethod
    def simulate(close, paths=1000, horizon=30):
        prices=np.asarray(close,dtype=float)
        if len(prices)<2:
            return []
        returns=np.diff(np.log(prices))
        mu=float(np.mean(returns))
        sigma=float(np.std(returns))
        last=prices[-1]
        sims=[]
        for _ in range(paths):
            shocks=np.random.normal(mu,sigma,horizon)
            sims.append((last*np.exp(np.cumsum(shocks))).tolist())
        return sims

    @staticmethod
    def probability_of_drop(simulations,threshold=-0.05):
        if not simulations:
            return 0.0
        hits=sum(((p[-1]-p[0])/p[0])<=threshold for p in simulations)
        return hits/len(simulations)
