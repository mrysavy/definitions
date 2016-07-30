IMAGE=installwebserver
REPO=michalr

build:
	docker-compose build

tag:
	docker tag ${IMAGE} ${REPO}/${IMAGE}

push: tag
	docker push ${REPO}/${IMAGE}

