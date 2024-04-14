from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<sation>/<date>")
def about(station, date):
    df = pandas.read_csv("")
    temprature = df.station(date)
    return {"station": station,
            "date": date,
            "temprature": temprature}


if __name__ == "main" :
    app.run(debug=True)
