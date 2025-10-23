#!/usr/bin/env python3
import subprocess, json, os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Kali MCP Server")

TOOLS = ["nmap", "nikto", "sqlmap", "wpscan", "dirb", "searchsploit"]

class CommandInput(BaseModel):
    tool: str
    args: list[str] = []

@app.get("/")
def root():
    return {"status": "Kali MCP Server running", "tools": TOOLS}

@app.post("/run")
def run_tool(cmd: CommandInput):
    if cmd.tool not in TOOLS:
        return {"error": "Unsupported tool"}
    try:
        output = subprocess.check_output([cmd.tool] + cmd.args, stderr=subprocess.STDOUT, text=True)
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": e.output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
