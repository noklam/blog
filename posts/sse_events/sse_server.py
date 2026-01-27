from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def sse_generator():
    for i in range(5):
        yield f"data: tick {i}\n\n"
        print(f"📤 Sent: tick {i}")
        await asyncio.sleep(2)
    yield "data: [DONE]\n\n"

@app.get("/")
async def sse():
    return StreamingResponse(sse_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
