# mcp_server.py
import sys
import json
import uuid

def send(msg):
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()

def handle_message(msg):
    if msg.get("method") == "tools/list":
        # Advertise available tools
        return {
            "id": msg["id"],
            "result": {
                "tools": [
                    {
                        "name": "echo",
                        "description": "Echo back a message",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"}
                            },
                            "required": ["message"]
                        }
                    }
                ]
            }
        }

    if msg.get("method") == "tools/call":
        params = msg["params"]
        if params["name"] == "echo":
            user_msg = params["arguments"]["message"]
            return {
                "id": msg["id"],
                "result": {
                    "content": [{"type": "text", "text": f"Echo: {user_msg}"}]
                }
            }

    # Fallback: method not found
    return {"id": msg["id"], "error": {"code": -32601, "message": "Method not found"}}

# ---- Main loop ----
for line in sys.stdin:
    try:
        msg = json.loads(line)
        resp = handle_message(msg)
        if resp:
            send(resp)
    except Exception as e:
        send({"error": str(e)})
