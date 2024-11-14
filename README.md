# Chat Services
___

Running project using that command line in the root directory
```commandline
fastapi dev chat_app/app.py
```

# Database Migrations
Alembic is used to handle database migrations. Here are some common commands:
- Generate a new migration (after making changes to the SQLAlchemy models):
    ```commandline
    alembic revision --autogenerate -m "{COMMIT MSG}"
    ```
 - Apply migrations:
    ```commandline
    alembic upgrade head
    ```
 - Check the current migration status:
    ```commandline
     alembic current
     ```
- Downgrade a migration:
    ```commandline
    alembic downgrade -1
    ```

# Run server for dev mode
```commandline
fastapi dev chat_app/app.py
```
___

### docker-compose.yml file
```yaml
version: "3.0"

services:

  chat-service:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: chat-service
    ports:
      - "8000:8000"  # Host port 6000 mapped to container port 8000
    env_file:
      - .env
    volumes:
      - .:/chat-app-service
    command: sh -c "uvicorn chat_app.app:app --reload --port=8000 --host=0.0.0.0"
    depends_on:
      - db

  db:
    image: postgres:14.0-alpine
    container_name: db
    volumes:
      - C:\Users\User\Desktop\projects\chat-app-service\postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=chat_service
      - POSTGRES_USER=asliddin
      - POSTGRES_PASSWORD=Asliddin1!
    ports:
      - "5432:5432"
```