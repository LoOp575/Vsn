from datetime import datetime, timezone

from app.engines.data_engine import DataEngine
from app.pipeline.engine_runner import EngineRunner
from app.models.signal_response import SignalResponse


class FormulaPipeline:
    def __init__(self):
        self.data_engine = DataEngine()
        self.engine_runner = EngineRunner()

    async def run(self):
        market = await self.data_engine.load_market_data()
        signals = []

        for item in market:
            symbol = item["symbol"]
            klines = item["candles"]
            analysis = await self.engine_runner.analyze(symbol, klines)
            decision = analysis["decision"]
            signals.append(
                SignalResponse(
                    symbol=symbol,
                    action=decision.get("action", "WAIT"),
                    signal=decision.get("signal", "HOLD"),
                    confidence=float(decision.get("confidence", 0.0)),
                    risk=decision.get("risk", "HIGH"),
                    regime=decision.get("regime", "RANGING"),
                    probability_of_drop=float(analysis.get("drop_probability", 0.0)),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                ).model_dump()
            )

        return {
            "status": "success",
            "symbols": len(market),
            "signals": signals,
            "message": "Formula Brain pipeline executed successfully.",
        }
