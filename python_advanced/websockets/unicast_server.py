#!/usr/bin/env python3
"""WebSocket server implementing unicast communication"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """Handle messages from each connected client"""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")

    except ConnectionClosed:
        pass

    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the unicast WebSocket server"""
    async with websockets.serve(
        connection_handler,
        "127.0.0.1",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
