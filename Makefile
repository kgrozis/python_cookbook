CONTAINER_NAME = python3
CONTAINER_TAG = 0.0.1
CONTAINER = $(CONTAINER_NAME):$(CONTAINER_TAG)
HOME_DIR = $(shell pwd)

.PHONY: all
all:
	docker build --no-cache -t $(CONTAINER) .
	docker run -t -d --name $(CONTAINER_NAME) -v $(pwd)/app:/usr/src/app $(CONTAINER)
	docker exec -it $(CONTAINER_NAME) /bin/bash
.PHONY: clean
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)
