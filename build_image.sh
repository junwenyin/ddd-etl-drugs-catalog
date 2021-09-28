!/bin/bash

version=0.1.0
image=etl-drugs-catalog
tag=$image:$version
latest=$image:latest
LOCATION=europe-west1
PROJECT=gnomon-digital-website
REPO=test
# build image
docker build . --no-cache -t $tag
# login to Container Registry
gcloud auth configure-docker $LOCATION-docker.pkg.dev
# tag docker image
docker tag $tag $LOCATION-docker.pkg.dev/$PROJECT/$REPO/$tag
docker tag $tag $LOCATION-docker.pkg.dev/$PROJECT/$REPO/$latest
# push docker image
docker push $LOCATION-docker.pkg.dev/$PROJECT/$REPO/$tag
docker push $LOCATION-docker.pkg.dev/$PROJECT/$REPO/$latest
#remove dangling images
sudo docker system prune -f