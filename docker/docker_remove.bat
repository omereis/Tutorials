docker container rm -f $(docker container ls -aq)
docker rmi -f $(docker images -q)
