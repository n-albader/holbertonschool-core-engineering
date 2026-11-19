#!/usr/bin/env python3
"""
A simple WebSocket echo server
"""

import asyncio
import websockets


async def connection_handler(websocket):
    """Receive messages and send them back to the client"""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server"""
    async with websockets.serve(
        connection_handler,
        "127.0.0.1",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
