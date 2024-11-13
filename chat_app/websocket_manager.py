from fastapi.websockets import WebSocket


class WebSocketManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Establishes a WebSocket connection with a client.

        This method performs the following steps:
        1. Accepts the incoming WebSocket connection.
        2. Adds the client to the list of active connections.
        3. Sends a welcome message to the newly connected client.

        Args:
            websocket (WebSocket): The WebSocket connection object for the client.

        Returns:
            None

        Note:
            This method is asynchronous and should be awaited when called.
        """
        # client has connected
        await websocket.accept()

        # add client to active connections list
        self.active_connections.append(websocket)

        # send welcome message to the client
        await websocket.send_json(data={"message": "Welcome"})

    async def send_message(self, message: str, websocket: WebSocket):
        """
        Sends a message to a specific client and broadcasts it to all other connected clients.

        This method performs the following steps:
        1. Retrieves the client's IP address and port.
        2. Sends the message back to the original sender.
        3. Broadcasts the message to all other connected clients.

        Args:
            message (str): The message to be sent.
            websocket (WebSocket): The WebSocket connection object for the client who sent the message.

        Returns:
            None

        Note:
            This method is asynchronous and should be awaited when called.
        """
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
        """
        Broadcasts a message to all connected clients except the sender.

        This method iterates through all active connections and sends the provided
        data to each client, excluding the original sender's WebSocket connection.

        Args:
            data (dict): The message data to be broadcast to other clients.
            websocket (WebSocket): The WebSocket connection of the sender to be excluded from the broadcast.

        Returns:
            None

        Note:
            This method is asynchronous and should be awaited when called.
        """

        # iter through all connections
        for connection in self.active_connections:

            # send message to other clients
            if connection != websocket:
                await connection.send_json(data=data)

    def disconnect(self, websocket: WebSocket):
        # disconnect from websocket connection
        self.active_connections.remove(websocket)
