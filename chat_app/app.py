from fastapi import FastAPI
from fastapi.websockets import WebSocket, WebSocketDisconnect

from websocket_manager import WebSocketManager

app = FastAPI()
websocket_manager = WebSocketManager()


@app.get(path="/")
async def root():
    return {
        "success": True,
        "msg": "Hello world from chat service"
    }


@app.websocket(path="/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket=websocket)

    try:

        while True:
            data = await websocket.receive_json()
            await websocket_manager.send_message(websocket=websocket, message=data)

    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket=websocket)
        await websocket_manager.send_message_broadcast_to_others(websocket=websocket, data={
            "message": f"Client ### has left the chat"
        })
