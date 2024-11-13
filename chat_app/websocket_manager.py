from fastapi.websockets import WebSocket


class WebSocketManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        # client has connected
        await websocket.accept()

        # add client to active connections list
        self.active_connections.append(websocket)

        # send welcome message to the client
        await websocket.send_json(data={"message": "Welcome"})

    async def send_message(self, message: str, websocket: WebSocket):
        # get client ip and port from websocket connection
        client_ip = f"{websocket.client.host}:{websocket.client.port}"

        # send message to client
        await websocket.send_json(data={
            "client": client_ip,
            "your message": message
        })

        # send data to another connections
        await self.send_message_broadcast_to_others(websocket=websocket, data={
            "client": client_ip,
            "message": message
        })

    async def send_message_broadcast_to_others(self, data: dict, websocket: WebSocket):

        # iter through all connections
        for connection in self.active_connections:

            # send message to other clients
            if connection != websocket:
                await connection.send_json(data=data)

    def disconnect(self, websocket: WebSocket):
        # disconnect from websocket connection
        self.active_connections.remove(websocket)
