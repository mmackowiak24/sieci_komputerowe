from flask import Flask, json, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

#ZADANIE 1
@app.route("/isbns", methods=['GET'])
def isbns():
    with open('books.json') as json_data:
        results = []
        data = json.load(json_data)
        for book in data['books']:
            results.append(book['isbn'])
        return results

#ZADANIE 2
@app.route("/isbns/<isbn>", methods=['GET'])
def get_isbn(isbn):
    with open('books.json') as json_data:
        results = []
        data = json.load(json_data)
        for book in data['books']:
            if(book['isbn'] == isbn):
                results.append(book)
                return results
        if len(results) == 0:
            return not_found()

#ZADANIE 3
@app.route("/authors/<expression>", methods=['GET'])
def get_authors(expression):
    with open('books.json') as json_data:
        results = []
        data = json.load(json_data)
        for book in data['books']:
            if(expression in book['title']):
                results.append(book["author"])
        if len(results) == 0:
            return not_found()
        else:
            return results


@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

