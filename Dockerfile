FROM kalilinux/kali-rolling

RUN apt update && apt install -y python3 python3-pip nmap nikto sqlmap wpscan dirb exploitdb &&     pip install fastapi uvicorn &&     rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY kali-mcp_server.py .

EXPOSE 8000
CMD ["python3", "kali-mcp_server.py"]
