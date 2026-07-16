from app.utils.candle_parser import CandleParser
from app.engines.formula_labs import FormulaLabs
from app.engines.entropy_engine import EntropyEngine
from app.engines.anomaly_engine import AnomalyEngine
from app.engines.regime_engine import RegimeEngine
from app.engines.monte_carlo_engine import MonteCarloEngine
from app.engines.bayesian_brain import BayesianBrain
from app.engines.central_brain import CentralBrain
from app.engines.decision_engine import DecisionEngine

class EngineRunner:
    async def analyze(self, symbol:str, klines:list):
        closes=CandleParser.close_prices(klines)
        features=FormulaLabs.feature_vector(closes)
        entropy=EntropyEngine.shannon_entropy(closes)
        anomalies=AnomalyEngine.detect(closes)
        sims=MonteCarloEngine.simulate(closes)
        drop=MonteCarloEngine.probability_of_drop(sims)
        regime=RegimeEngine.summarize(features)
        bayes=BayesianBrain.posterior(features['momentum'],features['volatility'],entropy,drop)
        central=CentralBrain().evaluate(regime,{},bayes,anomalies)
        decision=DecisionEngine.decide(central)
        return {'symbol':symbol,'features':features,'entropy':entropy,'drop_probability':drop,'decision':decision}