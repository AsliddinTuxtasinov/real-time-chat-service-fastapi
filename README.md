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