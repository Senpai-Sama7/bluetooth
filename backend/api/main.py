from fastapi import FastAPI, WebSocket
from endpoints.scan import router as scan_router
from endpoints.services import router as svc_router
from endpoints.attacks import router as atk_router

app = FastAPI()
app.include_router(scan_router, prefix="/scan")
app.include_router(svc_router, prefix="/services")
app.include_router(atk_router, prefix="/attacks")

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    # streaming logic here
    await ws.close()
