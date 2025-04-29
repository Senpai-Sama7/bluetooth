from fastapi import APIRouter, WebSocket
from btcore.scanner import BluetoothScanner
import json

router = APIRouter()
scanner = BluetoothScanner()

@router.websocket("/ws/scan")
async def websocket_scan(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            scan_type = data.get('type', 'classic')
            
            if scan_type == 'classic':
                results = scanner.classic_scan()
            elif scan_type == 'ble':
                results = await scanner.ble_scan()
            elif scan_type == 'combined':
                classic = scanner.classic_scan()
                ble = await scanner.ble_scan()
                results = classic + ble
            else:
                results = []
            
            await websocket.send_json({
                "status": "complete",
                "results": results
            })
            
    except Exception as e:
        await websocket.send_json({"error": str(e)})
    finally:
        await websocket.close()
