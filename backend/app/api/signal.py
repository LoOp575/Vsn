from fastapi import APIRouter

router = APIRouter(prefix='/signal', tags=['signal'])

@router.get('/health')
async def health():
    return {'status':'ok','service':'signal'}

@router.post('/scan')
async def scan():
    return {
        'status':'queued',
        'message':'Pipeline integration will be implemented in the next commits.'
    }
