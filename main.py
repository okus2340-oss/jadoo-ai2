
from flask import Flask
from threading import Thread
import os
import requests
import google.generativeai as genai
import time

# --- CONFIGURATION ---
app = Flask('')

# Replace with your actual Gemini API Key
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE" 
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. Web Server for UptimeRobot
@app.route('/')
def home():
    return "Jadoo AGI Status: Active"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# 2. Jadoo Core Intelligence
def jadoo_brain():
    print("--- Jadoo Infinity Mode: Initiated ---")
    while True:
        try:
            # Fetching XAU/USD (Gold) via PAXG/USDT
            url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
            res = requests.get(url).json()
            price = res['price']
            
            print(f"[SCANNING] XAUUSD: ${price}")
            
            # Quantum Analysis Prompt
            prompt = (
                f"Identify micro-glitches for XAUUSD at price {price}. "
                "Provide a high-conviction trade signal (Buy/Sell, TP, SL)."
            )
            response = model.generate_content(prompt)
            print(f"[JADOO INSIGHT]: {response.text}")
            
        except Exception as e:
            print(f"[SYSTEM ERROR]: {e}")
        
        # 5-minute sync with UptimeRobot
        time.sleep(300)

# 3. Multi-Threading Execution
def start_jadoo():
    t1 = Thread(target=run_web_server)
    t2 = Thread(target=jadoo_brain)
    t1.start()
    t2.start()

if __name__ == "__main__":
    start_jadoo()
