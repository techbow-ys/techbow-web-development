Docker flask quick deployment for mac

To build the image
docker build -t web .

To check the image we just build
docker image ls

docker rmi <image id>
docker rm <container id>

To run the flask app in docker.
docker run -p 5000:80 --volume=/Users/yufan/Documents/workspace/flaskdocker:/app flask
Open browser localhost:5000

To check the status of the container
docker container ls

