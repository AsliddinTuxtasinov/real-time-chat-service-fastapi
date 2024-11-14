FROM python:3.9

WORKDIR /chat-app-service

# Copy the rest of the application code
COPY . /chat-app-service

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /chat-app-service/requirements.txt
