# VWGCUSTOMER DEMO - PYTHON BACKEND

A microservice to forward requests associated with payment logic.
To start service navigate to root dir and run in `wsl`:
For Development:
```
make install    # Install dependencies
make run        # Run FastAPI locally
make lint       # Format code with pre-commit
make test       # Run tests
make up         # Build and run with Docker (dev mode)
```
For Production:
```
make up ENV=prod  # Build and run production Docker image
```
Then navigate to browser:
```
localhost:7000
```

To check API docs:
```
localhost:7000/docs <--- Swagger
localhost:7000/redoc <--- ReDoc
```
