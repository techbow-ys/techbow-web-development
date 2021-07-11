### Docker flask quick deployment commands overview

To build the image
```
docker build -t web:v1 .
```

To check the image we just build
```
docker image ls
```

Fetch a docker contains redis remotely. -d means run as daemon. -p means the port
```
docker run --name redis -p 6379:6379 -d redis:latest
```

Deploy a docker contains the web app.
```
docker run -p 5000:5000 --link redis:redis-host -d --name web web:v1
```

Then we can visit the API using the following
 - http://localhost:5000/
 - http://localhost:5000/set?key=A&value=1
 - http://localhost:5000/get?key=A

Check data in redis from docker container.
```
docker exec -ti <container_id> /bin/bash
redis-cli
get A
```