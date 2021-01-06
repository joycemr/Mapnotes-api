docker-compose --env-file .env.test.container up -d

sleep 6s

docker ps

sleep 1s

newman run api/test/postman_collection.json -e api/test/postman_container_environment.json

sleep 1s

docker-compose --env-file .env.docker down
