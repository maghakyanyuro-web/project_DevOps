from flask import Flask, render_template_string
import socket
import platform
import datetime
 
app = Flask(__name__)
 
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>DevOps Server</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;800&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
 
    :root {
      --bg: #0a0a0f;
      --surface: #12121a;
      --border: #1e1e2e;
      --accent: #00ff88;
      --accent2: #0088ff;
      --text: #e0e0f0;
      --muted: #555570;
    }
 
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Space Mono', monospace;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }
 
    /* Animated grid background */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(var(--border) 1px, transparent 1px),
        linear-gradient(90deg, var(--border) 1px, transparent 1px);
      background-size: 40px 40px;
      opacity: 0.4;
      animation: gridMove 20s linear infinite;
    }
 
    @keyframes gridMove {
      0%   { transform: translateY(0); }
      100% { transform: translateY(40px); }
    }
 
    /* Glow orbs */
    .orb {
      position: fixed;
      border-radius: 50%;
      filter: blur(80px);
      opacity: 0.12;
      pointer-events: none;
    }
    .orb-1 { width: 500px; height: 500px; background: var(--accent); top: -150px; left: -150px; animation: float1 8s ease-in-out infinite; }
    .orb-2 { width: 400px; height: 400px; background: var(--accent2); bottom: -100px; right: -100px; animation: float2 10s ease-in-out infinite; }
 
    @keyframes float1 { 0%,100% { transform: translate(0,0); } 50% { transform: translate(40px, 30px); } }
    @keyframes float2 { 0%,100% { transform: translate(0,0); } 50% { transform: translate(-30px, -40px); } }
 
    .container {
      position: relative;
      z-index: 1;
      width: min(680px, 95vw);
      animation: fadeUp 0.8s ease both;
    }
 
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to   { opacity: 1; transform: translateY(0); }
    }
 
    /* Header */
    .header {
      border: 1px solid var(--border);
      background: var(--surface);
      padding: 28px 36px;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
 
    .status-dot {
      width: 10px; height: 10px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 12px var(--accent);
      animation: pulse 2s ease-in-out infinite;
      flex-shrink: 0;
    }
 
    @keyframes pulse {
      0%,100% { opacity: 1; transform: scale(1); }
      50%      { opacity: 0.5; transform: scale(0.85); }
    }
 
    .header-text h1 {
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: 1.4rem;
      letter-spacing: -0.5px;
      color: #fff;
    }
 
    .header-text p {
      font-size: 0.7rem;
      color: var(--muted);
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-top: 2px;
    }
 
    .badge {
      margin-left: auto;
      font-size: 0.65rem;
      color: var(--accent);
      border: 1px solid var(--accent);
      padding: 3px 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }
 
    /* Cards grid */
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2px;
      margin-bottom: 2px;
    }
 
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 24px 28px;
      transition: border-color 0.2s;
    }
 
    .card:hover { border-color: var(--accent); }
 
    .card-label {
      font-size: 0.62rem;
      color: var(--muted);
      letter-spacing: 2.5px;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
 
    .card-value {
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: 1.05rem;
      color: var(--accent);
      word-break: break-all;
    }
 
    .card-value.blue { color: var(--accent2); }
    .card-value.white { color: #fff; }
 
    /* Full-width card */
    .card-full {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 24px 28px;
      margin-bottom: 2px;
    }
 
    /* Footer */
    .footer {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 14px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
 
    .footer span {
      font-size: 0.65rem;
      color: var(--muted);
      letter-spacing: 1.5px;
    }
 
    #clock {
      font-size: 0.75rem;
      color: var(--accent2);
      font-variant-numeric: tabular-nums;
    }
  </style>
</head>
<body>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
 
  <div class="container">
 
    <div class="header">
      <div class="status-dot"></div>
      <div class="header-text">
        <h1>SERVER ONLINE</h1>
        <p>System Status Dashboard</p>
      </div>
      <div class="badge">LIVE</div>
    </div>
 
    <div class="grid">
      <div class="card">
        <div class="card-label">Hostname</div>
        <div class="card-value">{{ hostname }}</div>
      </div>
      <div class="card">
        <div class="card-label">IP Address</div>
        <div class="card-value blue">{{ ip }}</div>
      </div>
      <div class="card">
        <div class="card-label">Platform</div>
        <div class="card-value white">{{ platform }}</div>
      </div>
      <div class="card">
        <div class="card-label">Uptime</div>
        <div class="card-value white">{{ uptime }}</div>
      </div>
    </div>
 
    <div class="card-full">
      <div class="card-label">Server Time</div>
      <div class="card-value blue">{{ time }}</div>
    </div>
 
    <div class="footer">
      <span>DEVOPS PROJECT &copy; {{ year }}</span>
      <span id="clock"></span>
    </div>
 
  </div>
 
  <script>
    function tick() {
      const now = new Date();
      document.getElementById('clock').textContent =
        now.toLocaleTimeString('en-GB', { hour12: false });
    }
    tick();
    setInterval(tick, 1000);
  </script>
</body>
</html>
"""
 
@app.route("/")
def index():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "N/A"
    os_info = f"{platform.system()} {platform.release()}"
    now = datetime.datetime.now()
    return render_template_string(HTML,
        hostname=hostname,
        ip=ip,
        platform=os_info,
        uptime="Running",
        time=now.strftime("%Y-%m-%d  %H:%M:%S"),
        year=now.year
    )
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
