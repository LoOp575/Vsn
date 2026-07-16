from fastapi import APIRouter, WebSocket
from app.services.live_scan_service import LiveScanService

router=APIRouter(prefix='/ws',tags=['websocket'])

@router.websocket('/signal')
async def signal_socket(ws: WebSocket):
    await ws.accept()
    service=LiveScanService()
    while True:
        result=await service.scan()
        await ws.send_json(result)
