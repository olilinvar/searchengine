from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def sendedata():
        eksemee = "dette er ting"
        return render_template("eple.html", variabel = eksemee)


if __name__ == "__main__":
    app.run(debug=True)