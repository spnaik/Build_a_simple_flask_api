import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for i, val in enumerate(cursor.description):
        d[val[0]] = row[i]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1> Access customer invoices</h1>
<p> A prototype API for access invoices for multiple customers.</p>'''


@app.route('/api/customers/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('chinook.db')

    # instead of tuples it starts returning 'dictionary' rows
    conn.row_factory = dict_factory

    # by starting the cursor object you can execute SQL statement
    cur = conn.cursor()

    # use the cursor to execute the SQL statement
    all_books = cur.execute('SELECT * FROM invoices;').fetchall()

    return jsonify(all_books)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/customers', methods=['GET'])
def api_filter():
    query_parameters = request.args

    # allows filtering via id, published and author
    id = query_parameters.get('id')
    city = query_parameters.get('city')
    country = query_parameters.get('country')

    query = "SELECT * FROM invoices WHERE"
    to_filter = []

    if id:
        query += ' InvoiceId=? AND'
        to_filter.append(id)
    if city:
        query += ' BillingCity=? AND'
        to_filter.append(city)
    if country:
        query += ' BillingCountry=? AND'
        to_filter.append(country)
    if not (id or city or country):
        return page_not_found(404)

    # remove the trailing 'AND'
    # and add ';' to the end of the SQL statement
    query = query[:-4] + ';'

    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    # SQL query that was built above is now matched to the filters list
    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()
