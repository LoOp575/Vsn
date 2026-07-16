from app.pipeline.formula_pipeline import FormulaPipeline


class LiveScanService:
    def __init__(self):
        self.pipeline = FormulaPipeline()

    async def scan(self):
        return await self.pipeline.run()
