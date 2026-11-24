
import asyncio
import websockets


async def test():
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        await ws.send("Hello")
        response = await ws.recv()
        print(response)


asyncio.run(test())


