# Default environment (dev or prod)
ENV ?= dev
DOCKERFILE ?= docker/$(ENV).dockerfile
IMAGE_NAME = myapp-$(ENV)

# Run FastAPI locally
run:
	PYTHONPATH=src uvicorn src.main:app --host=0.0.0.0 --port=7000 --reload

# Install dependencies
install:
	pip install -r requirements-dev.txt

TODO:
# Run tests
#test:
#	pytest --cov=src

# Lint with pre-commit
lint:
#    @echo "Running full pre-commit check"
	pre-commit run --all-files

# Build Docker image
build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) .

# Run Docker container
run-docker:
	docker run -p 7000:70 $(IMAGE_NAME)

# Build and Run Docker container
up: build run-docker

# Clean up Docker images
clean:
	docker system prune -f
