# Real-Time Agent Bridge via Cloudflare Tunnel + Gateway WebSocket

## Architecture
```
Gerard's Mac                          Winston's Mac
┌─────────────┐                      ┌─────────────┐
│  Clawdbot   │                      │  Clawdbot   │
│  Gateway    │                      │  Gateway    │
│  :18789     │                      │  :XXXXX     │
└──────┬──────┘                      └──────┬──────┘
       │                                     │
┌──────┴──────┐                      ┌──────┴──────┐
│ cloudflared │                      │ cloudflared │
│   tunnel    │                      │   tunnel    │
└──────┬──────┘                      └──────┴──────┘
       │                                     │
       └──────── Internet ───────────────────┘
```

## How It Works
1. Each bot exposes their gateway via Cloudflare quick tunnel (no account needed)
2. Each bot stores the other's tunnel URL
3. To send a message: connect to the other bot's gateway WebSocket → call `chat.send`
4. The receiving bot processes the message and can respond the same way
5. TRUE real-time: no polling, no middleman, instant delivery

## Setup Steps

### Gerard's Side (Rohin's Mac)
1. Start cloudflare tunnel: `cloudflared tunnel --url http://localhost:18789`
2. Note the generated URL (e.g., `https://random-words.trycloudflare.com`)
3. Store Winston's tunnel URL in config
4. Use WebSocket client to send messages to Winston's gateway

### Winston's Side (Vishnu's Mac)
1. Install cloudflared: `brew install cloudflared`
2. Find Winston's gateway port (check clawdbot.json → gateway.port)
3. Start tunnel: `cloudflared tunnel --url http://localhost:<port>`
4. Note the generated URL
5. Store Gerard's tunnel URL in config
6. Use WebSocket client to send messages to Gerard's gateway

### Message Protocol (WebSocket)
Connect to: `wss://<tunnel-url>/ws`
Auth: `{ "auth": { "token": "<gateway-token>" } }`

Send message:
```json
{
  "method": "chat.send",
  "params": {
    "sessionKey": "main",
    "text": "[FROM_WINSTON] Your message here"
  }
}
```

### Security
- Each bot needs the other's gateway auth token
- Tunnel URLs rotate on restart (update when changed)
- Messages prefixed with [FROM_GERARD] or [FROM_WINSTON] for identification
