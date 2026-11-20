#!/usr/bin/env python3
"""WebSocket server implementing broadcast communication"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    """Handle client connections and broadcast messages"""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            response = f"B:{message}"

            for client in connected_clients.copy():
                try:
                    await client.send(response)
                except ConnectionClosed:
                    connected_clients.discard(client)

    except ConnectionClosed:
        pass

    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the broadcast WebSocket server"""
    async with websockets.serve(
        connection_handler,
        "127.0.0.1",
        8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
