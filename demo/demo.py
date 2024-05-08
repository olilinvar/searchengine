from flask import Flask, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin",
    database="flaskepost"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM flaskedata")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

@app.route("/")
def sendedata():
        return """
                <form method = "post" action = "/sende-data">
                <input type = "text" name = "fornavn" />
                <input type = "submit" value = "submit" />
                </form>
                """

@app.route("/sende-data", methods = ["POST"])
def motta():
    # return request.form["fornavn"]
    fornavn = request.form["fornavn"]
    query = "INSERT INTO flaskedata (fornavn) VALUES (%s)"
    VALUES = (fornavn,)
    mycursor.execute(query, VALUES)

    mydb.commit()
    return "Data sendt"



if __name__ == "__main__":
    app.run(debug=True)