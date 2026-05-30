from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Dict
# import psycopg2
# from psycopg2.extras import RealDictCursor

# TODO: Put your actual Supabase URI connection string here
DB_URL = "YOUR_SUPABASE_CONNECTION_STRING_HERE"

def init_db():
    # conn = psycopg2.connect(DB_URL)
    # cur = conn.cursor()
    # cur.execute("""
    #     # CREATE TABLE IF NOT EXISTS messages (
    #         id SERIAL PRIMARY KEY,
    #         sender VARCHAR(100),
    #         text TEXT,
    #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #     );
    # """)
    # conn.commit()
    # cur.close()
    # conn.close()

# init_db()

 app = FastAPI()

class ChatManager:
    def __init__(self):
        self.connections: Dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.connections[websocket] = username
        await self.send_active_count()

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.connections:
            del self.connections[websocket]
            await self.send_active_count()

    async def send_active_count(self):
        total = len(self.connections)
        for ws in self.connections.keys():
            await ws.send_json({"type": "count", "count": total})

    async def send_to_all(self, payload: dict):
        for ws in self.connections.keys():
            await ws.send_json(payload)

manager = ChatManager()

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Web Chat</title>
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-gray-100 font-sans h-screen flex flex-col justify-between">

    <header class="bg-gray-800 p-4 shadow flex justify-between items-center border-b border-gray-700">
        <div>
            <h1 class="text-xl font-bold text-teal-400">⚡ Live Chatroom</h1>
            <p style="color:yello;">FastAPI + PostgreSQL Chat Engine</p>
        </div>
        <div class="bg-gray-700 px-3 py-1.5 rounded-full flex items-center gap-2 border border-gray-600">
            <span class="w-2.5 h-2.5 bg-green-500 rounded-full animate-pulse"></span>
            <span id="userCount" class="text-xs font-semibold text-green-400">0 Online</span>
        </div>
    </header>

    <main id="chat-box" class="flex-1 p-4 overflow-y-auto space-y-3 max-w-3xl w-full mx-auto">
        <div class="bg-teal-950/40 border border-teal-800 p-3 rounded-lg text-sm text-teal-300 text-center">
            Enter your username below to join the chat and see history.
        </div>
    </main>

    <footer class="bg-gray-800 p-4 border-t border-gray-700">
        <div class="max-w-3xl mx-auto flex flex-col sm:flex-row gap-2">
            <input id="usernameInput" type="text" placeholder="Your username..." 
                   class="bg-gray-700 text-white px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 sm:w-1/4">
            <div class="flex-1 flex gap-2">
                <input id="messageInput" type="text" placeholder="Type a message..." disabled
                       class="flex-1 bg-gray-700 text-white px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 disabled:opacity-50">
                <button id="sendBtn" onclick="sendMessage()" disabled
                        class="bg-teal-500 hover:bg-teal-600 text-gray-900 font-bold px-6 py-2 rounded-lg transition disabled:opacity-50">
                    Send
                </button>
            </div>
        </div>
    </footer>

    <script>
        let ws;
        let myUsername = "";
        const chatBox = document.getElementById('chat-box');
        const usernameInput = document.getElementById('usernameInput');
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        const userCountSpan = document.getElementById('userCount');

        usernameInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter' && usernameInput.value.trim() !== "") {
                myUsername = usernameInput.value.trim();
                initWebSocket(myUsername);
                usernameInput.disabled = true;
                messageInput.disabled = false;
                sendBtn.disabled = false;
                messageInput.focus();
            }
        });

        function appendMessage(sender, text, type) {
            const msgDiv = document.createElement('div');
            if (type === 'system') {
                msgDiv.className = "text-center text-xs text-gray-500 my-2 italic";
                msgDiv.innerText = text;
            } else {
                const isMe = sender === myUsername;
                msgDiv.className = `flex flex-col ${isMe ? 'items-end' : 'items-start'}`;
                msgDiv.innerHTML = `
                    <span class="text-xs text-gray-400 mb-1">${sender}</span>
                    <div class="${isMe ? 'bg-teal-500 text-gray-900 font-medium' : 'bg-gray-700 text-white'} px-4 py-2 rounded-2xl max-w-xs shadow">
                        ${text}
                    </div>
                `;
            }
            chatBox.appendChild(msgDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function initWebSocket(username) {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            ws = new WebSocket(`${protocol}//${window.location.host}/ws/${encodeURIComponent(username)}`);

            ws.onmessage = event => {
                const data = JSON.parse(event.data);
                
                if (data.type === 'count') {
                    userCountSpan.innerText = `${data.count} Online`;
                } else if (data.type === 'history') {
                    chatBox.innerHTML = "";
                    data.messages.forEach(msg => {
                        appendMessage(msg.sender, msg.text, 'chat');
                    });
                } else {
                    appendMessage(data.sender, data.text, data.type);
                }
            };

            ws.onclose = () => {
                alert("Connection lost. Please refresh.");
            };
        }

        function sendMessage() {
            const text = messageInput.value.trim();
            if (text !== "" && ws && ws.readyState === WebSocket.OPEN) {
                ws.send(text);
                messageInput.value = '';
                messageInput.focus();
            }
        }

        messageInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
"""

@app.get('/', response_class=HTMLResponse)
async def get():
    return html

@app.websocket('/ws/{username}')
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    
    conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    cur.execute("SELECT sender, text FROM messages ORDER BY id ASC LIMIT 50;")
    history = cur.fetchall()
    cur.close()
    conn.close()
    
    await websocket.send_json({"type": "history", "messages": history})
    await manager.send_to_all({"type": "system", "text": f"🚀 {username} joined the chat."})
    
    try:
        while True:
            data = await websocket.receive_text()
            
            conn = psycopg2.connect(DB_URL)
            cur = conn.cursor()
            cur.execute("INSERT INTO messages (sender, text) VALUES (%s, %s);", (username, data))
            conn.commit()
            cur.close()
            conn.close()
            
            await manager.send_to_all({
                "type": "chat",
                "sender": username,
                "text": data
            })
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.send_to_all({"type": "system", "text": f"🚪 {username} left the chat."})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
