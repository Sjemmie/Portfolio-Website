from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv(r"C:\Users\youri\PycharmProjects\Portfolio Website\WeatherAPI\dictionary.csv")


@app.route("/")
def home():
    return render_template("dict.html")


@app.route("/dict/v1/<word>")
def definition(word):
    def_01 = df.loc[df["word"] == word]["definition"].squeeze()
    return {"definition": str(def_01),
            "word": word
            }


if __name__ == "__main__":
    app.run(debug=True)
