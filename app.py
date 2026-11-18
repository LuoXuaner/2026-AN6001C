# web app

from math import isfinite
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
model = joblib.load(Path(__file__).resolve().with_name("DBS_SGD.pkl"))


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html")


@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    return render_template("dbs.html")


@app.route("/dbsPred", methods=["POST"])
def dbs_prediction():
    exchange_rate_text = request.form.get("q", "").strip()
    try:
        exchange_rate = float(exchange_rate_text)
    except ValueError:
        return render_template(
            "dbs.html", error="Please enter a valid exchange rate.",
            exchange_rate=exchange_rate_text,
        ), 400

    if not isfinite(exchange_rate) or exchange_rate <= 0:
        return render_template(
            "dbs.html", error="Please enter a positive, finite exchange rate.",
            exchange_rate=exchange_rate_text,
        ), 400

    features = pd.DataFrame({"SGD": [exchange_rate]})
    prediction = model.predict(features).item()
    if not isfinite(prediction):
        return render_template(
            "dbs.html", error="The model could not produce a finite prediction.",
            exchange_rate=exchange_rate_text,
        ), 400

    return render_template(
        "dbsPred.html", prediction=f"{prediction:.2f}",
        exchange_rate=exchange_rate_text,
    )


if __name__ == "__main__":
    app.run()
