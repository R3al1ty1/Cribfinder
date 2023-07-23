from flask import Flask, render_template
from scrapes import cianCribScrapper
import psycopg2
import consts

conn = psycopg2.connect(
    host="localhost",
    database="CribFinderDB",
    user=consts.user,
    port=consts.port,
    password=consts.password
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title='CribFinder')

if __name__ == '__main__':
    app.run(debug=True)