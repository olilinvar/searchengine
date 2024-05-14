from flask import Flask, request, render_template
import mysql.connector


app = Flask(__name__)
app.static_folder = 'static'

try:
    web_pages_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin",
        database="web_pages_db"
    )

    mycursor = web_pages_db.cursor()

    mycursor.execute("SELECT * FROM web_pages")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
except mysql.connector.Error as err:
    print("MySQL Connection Error:", err)


@app.route("/")
def get_search_query():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    search_query = request.form.get("search_query")
    print("Search query:", search_query)
    query = "SELECT * FROM web_pages"
    if search_query:
        query += f" WHERE title LIKE '%{search_query}%' OR description LIKE '%{search_query}%' OR content LIKE '%{search_query}%' LIMIT 5"
    print("SQL query:", query)
    mycursor.execute(query)
    entries = mycursor.fetchall()
    return render_template("results.html", search_query=search_query, entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
