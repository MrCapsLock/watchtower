# Set base image
FROM python:3.8-slim-buster

RUN apt-get update && apt-get upgrade -y && apt-get install -y iputils-ping wget

# Set working directory
WORKDIR /app

# Copy Reqs
COPY requirements.txt .

# Remove cache
RUN rm ~/.cache/pip -rf

# Install Deps
RUN pip3 install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# Run
CMD [ "python3", "./main.py" ]
