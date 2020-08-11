from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

mydb = None


def createConnection():
    global mydb
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password=,
        database="ebookshop"
        )
    print(mydb)


createConnection()


def get_articles(keyword=''):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM books WHERE title like  '%"+keyword+"%'")
    articles = cursor.fetchall()
    jsonResult = []
    for article in articles:
        jsonResult.append({
            'Article Name': article[0],
            'Article Link' : article[1]
        })
    return jsonResult

from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint((get_articles('Java')))

@app.route('/')
def pageLoad():
    return jsonify({"Welcome Message": "Hello there, visit 127.0.0.1:1234/articles"})


@app.route('/articles')
def loadAllArticles():
    response = get_articles()
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles"})
    else:
        return jsonify(response)


@app.route('/articles/<keyword>')
def loadArticlesByKeyword(keyword):
    response = get_articles(keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles with keyword " + keyword})
    else:
        return jsonify(response)


if __name__ == '__main__':
    app.run(port=1234,debug=True)