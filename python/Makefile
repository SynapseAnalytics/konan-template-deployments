# import konan config.
cnf ?= .konan
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

# Check if pushing to kcr or third-party container registry
ifeq ($(KONAN_CONTAINER_REGISTRY),konan.azurecr.io)
	TAG_TARGETS = tag-for-kcr
	PUBLISH_TARGETS = publish-kcr
else
	TAG_TARGETS = tag-latest tag-version
	PUBLISH_TARGETS = publish-latest publish-version
endif

# Check if registry namespace is set or can be defaulted
ifndef KONAN_CONTAINER_REGISTRY_NAMESPACE
ifeq ($(KONAN_CONTAINER_REGISTRY),konan.azurecr.io)
$(error Using the konan.azurecr.io KONAN_CONTAINER_REGISTRY yet KONAN_CONTAINER_REGISTRY_NAMESPACE is unset)
else
# $(info KONAN_CONTAINER_REGISTRY_NAMESPACE is unset. Defaulting to $(KONAN_CONTAINER_REGISTRY_USERNAME))
KONAN_CONTAINER_REGISTRY_NAMESPACE = $(KONAN_CONTAINER_REGISTRY_USERNAME)
endif
endif

# Clean the enviroment
clean: ## Remove all images named `{KONAN_APP_NAME}`
	docker rmi $$(docker images | grep $(KONAN_APP_NAME))

# Build the image
build: ## Build the image
	docker build -t $(KONAN_APP_NAME) .

build-nc: ## Build the image without caching
	docker build -t $(KONAN_APP_NAME) --no-cache .

# Locally test the image
run: ## Run a container of the image
	docker run -i -t --rm --name="$(KONAN_APP_NAME)" $(KONAN_APP_NAME)

up: build run ## Build the image and run a container of it (Alias to make build && make run)

stop: ## Stop and remove a running container
	docker stop $(KONAN_APP_NAME); docker rm $(KONAN_APP_NAME)

# Tag the image
tag: $(TAG_TARGETS) ## Generate image tag(s)

tag-latest: ## Generate image `latest` tag
	@echo 'creating tag latest'
	docker tag $(KONAN_APP_NAME) $(KONAN_CONTAINER_REGISTRY)/$(KONAN_CONTAINER_REGISTRY_NAMESPACE)/$(KONAN_APP_NAME):latest

tag-version: ## Generate image `{KONAN_APP_VERSION}` tag
	@echo 'creating tag $(KONAN_APP_VERSION)'
	docker tag $(KONAN_APP_NAME) $(KONAN_CONTAINER_REGISTRY)/$(KONAN_CONTAINER_REGISTRY_NAMESPACE)/$(KONAN_APP_NAME):$(KONAN_APP_VERSION)

tag-for-kcr: ## Generate image for kcr
	@echo 'creating tag for kcr'
	docker tag $(KONAN_APP_NAME) konan.azurecr.io/$(KONAN_CONTAINER_REGISTRY_NAMESPACE):$(KONAN_APP_NAME)

# Login to container registry
repo-login: ## Auto login to container registry
	docker login ${KONAN_CONTAINER_REGISTRY} -u $(KONAN_CONTAINER_REGISTRY_USERNAME) -p $(KONAN_CONTAINER_REGISTRY_PASSWORD)

# Publish the image
publish: repo-login $(PUBLISH_TARGETS) ## Publish the (tagged) image(s) to `{KONAN_CONTAINER_REGISTRY}`

publish-latest: tag-latest ## Publish the `latest` tagged image to `{KONAN_CONTAINER_REGISTRY}`
	@echo 'publishing latest to $(KONAN_CONTAINER_REGISTRY)'
	docker push $(KONAN_CONTAINER_REGISTRY)/$(KONAN_CONTAINER_REGISTRY_NAMESPACE)/$(KONAN_APP_NAME):latest

publish-version: tag-version ## Publish the `{KONAN_APP_VERSION}` tagged image to `{KONAN_CONTAINER_REGISTRY}`
	@echo 'publishing $(KONAN_APP_VERSION) to $(KONAN_CONTAINER_REGISTRY)'
	docker push $(KONAN_CONTAINER_REGISTRY)/$(KONAN_CONTAINER_REGISTRY_NAMESPACE)/$(KONAN_APP_NAME):$(KONAN_APP_VERSION)

publish-kcr: tag-kcr ## Publish the image to kcr
	@echo 'publishing $(KONAN_APP_VERSION) to $(KONAN_CONTAINER_REGISTRY)'
	docker push $(KONAN_CONTAINER_REGISTRY)/$(KONAN_CONTAINER_REGISTRY_NAMESPACE):$(KONAN_APP_NAME)

# Release the image
release: build-nc publish ## Make a release by building and publishing the (tagged) image(s) to `{KONAN_CONTAINER_REGISTRY}`

# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Show this help message and exit.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help