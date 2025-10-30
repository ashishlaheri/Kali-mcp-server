# Kali Pentest MCP Server

MCP server exposing Kali pentest tools (`nmap`, `nikto`, `sqlmap`, `wpscan`, `dirb`, `searchsploit`) for educational network analysis within authorized labs.

## ⚙️ Installation

```bash
git clone https://github.com/ashishlaheri/kali-mcp.git
cd kali-mcp
docker build -t kali-mcp-server .
docker run -it -p 8000:8000 kali-mcp-server
```

Access via: `http://localhost:8000`

### Example API Usage
```bash
curl -X POST http://localhost:8000/run -H "Content-Type: application/json" -d '{"tool": "nmap", "args": ["-sn", "127.0.0.1"]}'
```

## 🔒 Legal Disclaimer
Use this server **only** for systems you own or have explicit permission to test.
