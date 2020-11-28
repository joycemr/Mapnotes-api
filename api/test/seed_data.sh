#!/bin/sh

curl -X POST -H 'content-type: application/json' http://localhost:5000/notes -d '{"title":"Test 1", "body":"Test body"}'
curl -X POST -H 'content-type: application/json' http://localhost:5000/notes -d '{"title":"Test 2", "body":"Test body"}'
curl -X POST -H 'content-type: application/json' http://localhost:5000/notes -d '{"title":"Test 3", "body":"Test body"}'

