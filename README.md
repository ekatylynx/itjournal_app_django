# ItJournal - Django Application

This is a simple Python and Django App that allows you to create news, articles and other notes with filtering by categories.

# REST API

The REST API to the app is described below.

## Get list of Todos

### Request

`GET /todos/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/todos/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []
    