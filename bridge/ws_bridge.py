import json, asyncio, websockets, sys, uuid

async def send_message(tunnel_url, token, message):
    url = f"wss://{tunnel_url}/ws"
    try:
        async with websockets.connect(url, open_timeout=10) as ws:
            # Step 1: Send connect request
            connect_msg = json.dumps({
                "type": "req",
                "id": str(uuid.uuid4()),
                "method": "connect",
                "params": {
                    "minProtocol": 3,
                    "maxProtocol": 3,
                    "client": {
                        "id": "cli",
                        "displayName": "Gerard Bridge",
                        "version": "dev",
                        "platform": "node",
                        "mode": "cli"
                    },
                    "auth": {"token": token}
                }
            })
            await ws.send(connect_msg)
            
            # Wait for response(s)
            while True:
                resp = await asyncio.wait_for(ws.recv(), timeout=5)
                data = json.loads(resp)
                print(f"Received: {json.dumps(data, indent=2)[:200]}")
                
                # Check if connected
                if data.get("type") == "res" and data.get("ok"):
                    print("✅ Connected!")
                    break
                elif data.get("type") == "event":
                    continue  # Skip events during connect
                elif data.get("type") == "res" and not data.get("ok"):
                    print(f"❌ Connection failed: {data.get('error')}")
                    return
            
            # Step 2: Send chat message
            send_msg = json.dumps({
                "type": "req",
                "id": str(uuid.uuid4()),
                "method": "chat.send",
                "params": {
                    "sessionKey": "main",
                    "message": message,
                    "idempotencyKey": str(uuid.uuid4())
                }
            })
            await ws.send(send_msg)
            resp = await asyncio.wait_for(ws.recv(), timeout=10)
            data = json.loads(resp)
            print(f"Send response: {json.dumps(data, indent=2)[:300]}")
            
            if data.get("ok"):
                print("✅ Message sent successfully!")
            else:
                print(f"❌ Send failed: {data}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tunnel = sys.argv[1] if len(sys.argv) > 1 else "pressed-largest-loose-above.trycloudflare.com"
    token = sys.argv[2] if len(sys.argv) > 2 else "0b48799949ee51d30237dc9f133c0a339de659d088146e25"
    msg = sys.argv[3] if len(sys.argv) > 3 else "[FROM_GERARD] 🐹 Test message via real-time bridge!"
    
    asyncio.run(send_message(tunnel, token, msg))
