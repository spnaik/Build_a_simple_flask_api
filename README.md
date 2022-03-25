# Build a flask api to query database
Create a basic Flask app and connect it to a database

Flask is a web framework for python that helps in building web applications, managing HTTP requests etc.
In this repo, we will create a basic Flask application and access the database on disk. 
The database used in this repo is a public database which could also be accessed from https://www.sqlitetutorial.net/sqlite-sample-database/


The Flask app connects to the chinook database
and the user can query the invoices table based on three filtering criteria - InvoiceId, BillingCountry, BillingCity

## Steps to run the flask api
1. First download the public database file - chinook.db
2. To start the flask server - python app.py
3. This will open  the flask app serving at http://127.0.0.1:5000/

Once the flask server has started, try filtering with the following HTTP requests:
1. http://127.0.0.1:5000/api/customers/all
2. http://127.0.0.1:5000/api/customers?country=Germany
3. http://127.0.0.1:5000/api/customers?city=Oslo
