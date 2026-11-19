#!/usr/bin/env python3
"""WebSocket client implementation"""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to a WebSocket server, send a message, and receive a response"""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Run the WebSocket client demo"""
    response = await connect_and_send(
        "ws://localhost:8765",
        "Hello WebSocket"
    )
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
