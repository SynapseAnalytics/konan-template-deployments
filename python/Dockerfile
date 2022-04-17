# Specify base image
FROM python:3.7-slim-stretch

# Get some important arguments from user, with sane defaults
ARG user=konan-user
ARG port=8000

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential make gcc gnupg \
    python3-dev unixodbc-dev

# Set some enviroment variables for directories
ENV KONAN_SERVICE_BASE_DIR /app
ENV KONAN_SERVICE_ARTIFACTS_DIR ${KONAN_SERVICE_BASE_DIR}/artifacts
ENV KONAN_SERVICE_SRC_DIR ${KONAN_SERVICE_BASE_DIR}/src

ENV KONAN_SERVICE_RETRAINING_DIR /retraining
ENV KONAN_SERVICE_RETRAINING_ARTIFACTS_DIR ${KONAN_SERVICE_RETRAINING_DIR}/artifacts
ENV KONAN_SERVICE_RETRAINING_DATA_DIR ${KONAN_SERVICE_RETRAINING_DIR}/data

# Create the konan-service parent directory
RUN mkdir -m 777 ${KONAN_SERVICE_BASE_DIR}

# Create the custom user for the application to run as
RUN adduser --disabled-password --gecos "" ${user}
USER ${user}

# Copy relevant files and directories
WORKDIR ${KONAN_SERVICE_BASE_DIR}
COPY --chown=${user} . ${KONAN_SERVICE_BASE_DIR}

# Make scripts executable
RUN chmod +x ${KONAN_SERVICE_BASE_DIR}/retrain.sh || true

# Modify the PATH variable to allow for user-level pip installs
ENV PATH="/home/${user}/.local/bin:${PATH}"

# Install requirements
RUN pip install --user --upgrade pip && pip install --user --upgrade setuptools uvicorn
RUN pip install --user --no-cache-dir -r ${KONAN_SERVICE_BASE_DIR}/requirements.txt

# Expose port
ENV KONAN_PORT=${port}
EXPOSE ${KONAN_PORT}

# Run Webserver
WORKDIR ${KONAN_SERVICE_SRC_DIR}
CMD [ \
    "sh", \
    "-c", \
    "uvicorn --host 0.0.0.0 --port ${KONAN_PORT} --workers 1 --factory server:app" \
]
