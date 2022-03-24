# Specify base image
FROM python:3.7-slim-stretch

# Get some important arguments from user, with sane defaults
ARG user=konan-user
ARG port=8000

ENV KONAN_PORT=${port}

# Set some enviroment variables for directories
ENV KONAN_SERVICE_BASE_DIR /home/${user}/app

ENV KONAN_SERVICE_DATA_DIR ${KONAN_SERVICE_BASE_DIR}/data
ENV KONAN_SERVICE_MODELS_DIR ${KONAN_SERVICE_BASE_DIR}/models
ENV KONAN_SERVICE_SCRIPTS_DIR ${KONAN_SERVICE_BASE_DIR}/scripts
ENV KONAN_SERVICE_SRC_DIR ${KONAN_SERVICE_BASE_DIR}/src

# Modify the PATH variable to allow for user-level pip installs
ENV PATH="/home/${user}/.local/bin:${PATH}"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential make gcc gnupg \
    python3-dev unixodbc-dev

# Create the custom user for the application to run as
RUN adduser --disabled-password --gecos "" ${user}
USER ${user}

# Copy relevant files and directories
RUN mkdir ${KONAN_SERVICE_BASE_DIR}
WORKDIR ${KONAN_SERVICE_BASE_DIR}
COPY --chown=${user} . ${KONAN_SERVICE_BASE_DIR}

# Install requirements
RUN pip install --user --upgrade pip && pip install --user --upgrade setuptools uvicorn
RUN pip install --user --no-cache-dir -r ${KONAN_SERVICE_BASE_DIR}/requirements.txt

# Expose port and run web server
EXPOSE ${port}
WORKDIR ${KONAN_SERVICE_SRC_DIR}
CMD [ \
    "sh", \
    "-c", \
    "uvicorn --host 0.0.0.0 --port ${KONAN_PORT} --workers 1 --factory server:app" \
]
