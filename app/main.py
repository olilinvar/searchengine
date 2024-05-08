from flask import Flask, request, render_template, redirect
import mysql.connector


app = Flask(__name__)


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin",
        database="mydb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM brukere")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
except mysql.connector.Error as err:
    print("MySQL Connection Error:", err)


@app.route("/")
def get_search_query():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    tekst = request.form["search_query"]
    print(tekst)

    return render_template("results.html", variabel=tekst)


if __name__ == "__main__":
    app.run(debug=True)
