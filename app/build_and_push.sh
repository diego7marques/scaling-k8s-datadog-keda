#! /bin/bash
repository=$1

docker build -t local:app-test .
docker tag local:app-test $repository/app-test:latest
docker push $repository/app-test:latest