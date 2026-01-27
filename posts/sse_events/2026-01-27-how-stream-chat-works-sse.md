---
author: <a href='https://twitter.com/HamelHusain'>Hamel Husain</a> & <a href='https://twitter.com/jeremyphoward'>Jeremy
  Howard</a>
categories:
- codespaces
- nbdev
date: '2026-01-27'
description: How does a streaming chat actually works?
  before.
hide: false
image: images/fastpages_posts/codespaces/codespaces.png
layout: post
permalink: /codespaces
title: 'How chat.stream() works under the hood'?
toc: false

---

# Introduction
```python
from mistralai import Mistral
import os

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
stream = client.chat.stream(model="mistral-small-latest", messages=[{"role": "user", "content": "Explain generators in 100 words."}])


for i, chunk in enumerate(stream):
    delta = chunk.data.choices[0].delta.content or ""
    print(f"Chunk {i}: {delta}", end="", flush=True)
```

Most Chat API support a "stream" mode where you can stream your response as it comes instead of one big chunk of data. This is handy when you have a long conversation and this is what support the experience that it feels like someone is typing a response as you asked a question.

What unusual to me is this line of code:
```
for i, chunk in enumerate(stream):
```

If this is just a Python for-loop, wouldn't this waste a lot of CPU cycle where the Python interpreter just keep iterating on the same object until it's done?

## Quick Refresher of `Iterator`, `Iterable` and `Generator`
In Python, anything that can be "loop" is called `Iterable`. At the start of a for-loop, the statement first create an `Iterator` from `iter(obj)`, and the repeated invokes `next(iterator)` inside a loop until it sees a special `StopIteration` exception and terminate.

```python
obj = [1, 2, 3]  # Iterable
it = iter(obj)   # Returns Iterator
while True:
    try:
        item = next(it)  # Yields 1, then 2, then 3
        # Loop body
    except StopIteration:
        break
```

## Simlutation of SSE Server and client
On server side, we are not doing anything fancy but using FastAPI streaming response to push data continuously.
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def sse_generator():
    for i in range(5):
        yield f"data: tick {i}\n\n"
        print(f"📤 Sent: tick {i}")
        await asyncio.sleep(1)
    yield "data: [DONE]\n\n"

@app.get("/")
async def sse():
    return StreamingResponse(sse_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

```
On Client side
```python
#!/usr/bin/env python3
import socket
import time
import sys

# Raw TCP socket → PROVES OS epoll control
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8000))

# HTTP request
sock.send(b"""GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Accept: text/event-stream\r\n\r\n""")

# Skip HTTP headers
header = b''
while b'\r\n\r\n' not in header:
    header += sock.recv(1024)

print("🔄 Raw socket FOR loop - OS epoll pausing...", flush=True)
start = time.time()
count = 0

# YOUR FOR LOOP - PURE OS PAUSE
while count < 5:
    chunk = sock.recv(1024).decode(errors='ignore')
    if 'tick ' in chunk:
        tick_num = chunk.split('tick ')[1].split('\n')[0]
        now = time.time() - start
        print(f"T+{now:.1f}s 📦 tick {tick_num}", flush=True)
        count += 1
    elif '[DONE]' in chunk:
        break

print("✅ Epoll demo complete")
sock.close()
```

On client side, you can see that in this `while` loop - the loop actually get paused on `sock.recv`. Under the hood, `sock.recv` will trigger a OS level `epoll_wait` call that only resume when data arrives. One way to prove that is try to change the code in the server side i.e. sleep for 2 seconds, and see how client response change.

This is magic that is done at the OS level. Imagine if this feature is not supported by OS, the application code will need to poll the server continuously to waste a lot of CPU cycle (i.e. poll every 10ms).


## But why do you still need to check if delta.content is empty?
As we understood, the stream is only resume where there is new data arrived. So when then we still need to check `if delta.context` exists?

The reason is simple, the server sends data without contents:
- Usage stats
- tool calls

An example of data may looks like this:
```json
data: {"choices":[{"delta":{"tool_calls":[{"index":0,"type":"function","function":{"name":"get_weather"}}]}}]}

```

# Summary
In summary, the short answer for an efficient for-loop without constant polling is because of the OS level `epoll_wait` feature that is support by modern web socket already. As a result, the application code is simplified and remains efficient.