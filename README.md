# FlaskRestApiRest

[![Build Status](https://travis-ci.org/Tony133/FlaskRestApiRest.svg?branch=master)](https://travis-ci.org/Tony133/FlaskRestApiRest)

Simple Example Api Rest with Flask

## Import db object and generate SQLite database

```
   $ python
   >>> from book import db
   >>> db.create_all()
```

## Run App

```
   $ python book.py 
    
    or
   
   $ export FLASK_APP=book.py
   $ flask run 
```

## Getting with Curl

```
    $ curl -H 'content-type: application/json' -v -X GET http://127.0.0.1:5000/api/book 
    $ curl -H 'content-type: application/json' -v -X GET http://127.0.0.1:5000/api/book:id
    $ curl -H 'content-type: application/json' -v -X POST -d '{"title":"Foo bar","price":"19.99"}' http://127.0.0.1:5000/api/book 
    $ curl -H 'content-type: application/json' -v -X PUT -d '{"title":"Foo bar","price":"19.99"}' http://127.0.0.1:5000/api/book:id
    $ curl -H 'content-type: application/json' -v -X DELETE http://127.0.0.1:5000/api/book/:id
```
