import logging, json, random
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# לוגר שמדפיס ל-stdout בפורמט JSON (ככה Elastic אוסף לוגים ב-OCP)
class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "customer_id": random.randint(100, 999),
            "service": "customer-service"
        })

logger = logging.getLogger("App")
logHandler = logging.StreamHandler()
logHandler.setFormatter(JsonFormatter())
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/call')
def simulate_call():
    actions = ["Incoming Call", "Live Chat Started", "Ticket Created"]
    action = random.choice(actions)
    logger.info(f"Action: {action}")
    return jsonify({"status": "Success", "action": action})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)