from fastapi import APIRouter

from app.pipeline.formula_pipeline import FormulaPipeline

router = APIRouter(prefix='/signal', tags=['signal'])


@router.get('/health')
async def health():
    return {'status': 'ok', 'service': 'signal'}


@router.post('/scan')
async def scan():
    pipeline = FormulaPipeline()
    result = await pipeline.run()
    return result
