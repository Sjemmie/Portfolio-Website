from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dict.html")


@app.route("/dict/v1/<word>")
def definition(word):
    return {"definition": word.upper,
            "word": word
            }


if __name__ == "__main__":
    app.run(debug=True)
