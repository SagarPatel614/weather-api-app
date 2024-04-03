from flask import Flask, render_templates

# Flask app object
app = Flask(__name__)


@app.route("/")
def home():
    return render_templates("home.html")


@app.route("/api/v1/<station>/<date>")
def get_weather(station, date):
    temperature = 24
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
