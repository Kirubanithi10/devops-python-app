from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

SHIPMENTS = {
    "CG001": {"origin": "Chennai", "destination": "Dubai",
              "status": "In Transit", "weight_kg": 450},
    "CG002": {"origin": "Mumbai", "destination": "Singapore",
              "status": "Delivered", "weight_kg": 320},
    "CG003": {"origin": "Delhi", "destination": "London",
              "status": "Pending", "weight_kg": 780},
}


@app.route('/')
def home():
    return jsonify({
        "app": "iCargo Tracker API",
        "version": "1.0.0",
        "status": "ok"
    })


@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


@app.route('/shipments')
def get_shipments():
    return jsonify({"shipments": SHIPMENTS})


@app.route('/shipments/<awb>')
def get_shipment(awb):
    shipment = SHIPMENTS.get(awb.upper())
    if not shipment:
        return jsonify({"error": "AWB not found"}), 404
    return jsonify({"awb": awb.upper(), **shipment})


@app.route('/shipments/status/<status>')
def get_by_status(status):
    result = {
        k: v for k, v in SHIPMENTS.items()
        if v["status"].lower() == status.lower()
    }
    return jsonify({"shipments": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
