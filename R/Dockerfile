# Specify base image
FROM rocker/verse:4.1.2

# Get some important arguments from user, with sane defaults
ARG user=konan-user
ARG port=8000

# Install dependencies
RUN apt-get update --allow-releaseinfo-change && apt-get install -y \
    liblapack-dev \
    libpq-dev

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
# ENV PATH="/home/${user}/.local/bin:${PATH}"

# Create user-level R library folder
ENV R_LIBS_USER "/home/${user}/R/library"
RUN mkdir -p ${R_LIBS_USER}

# Install requirements
RUN R -e \
    "install.packages( \
        c('plumber'), \
        lib = Sys.getenv('R_LIBS_USER'), \
        repos = 'http://cran.us.r-project.org' \
    )"

RUN R -e \
    "install.packages( \
        readLines('requirements.txt'), \
        lib = Sys.getenv('R_LIBS_USER'), \
        repos = 'http://cran.us.r-project.org' \
    )"

# Expose port and run web server
EXPOSE ${port}
ENTRYPOINT ["R", "-e", "r = plumber::plumb('${KONAN_SERVICE_SRC_DIR}/endpoints.R'); r$run(port = ${port}, host = '0.0.0.0')"]
