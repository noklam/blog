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
