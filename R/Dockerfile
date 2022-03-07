# Specify base image
FROM rocker/verse:4.1.2

# Get some important arguments from user, with sane defaults
ARG user=konan-user
ARG port=8000

# Set some enviroment variables for directories
ENV KONAN_SERVICE_BASE_DIR /home/${user}/app

ENV KONAN_SERVICE_DATA_DIR ${KONAN_SERVICE_BASE_DIR}/data
ENV KONAN_SERVICE_MODELS_DIR ${KONAN_SERVICE_BASE_DIR}/models
ENV KONAN_SERVICE_SCRIPTS_DIR ${KONAN_SERVICE_BASE_DIR}/scripts
ENV KONAN_SERVICE_SRC_DIR ${KONAN_SERVICE_BASE_DIR}/src

# Modify the PATH variable to allow for user-level pip installs
# ENV PATH="/home/${user}/.local/bin:${PATH}"

# Install dependencies
RUN apt-get update --allow-releaseinfo-change && apt-get install -y \
    liblapack-dev \
    libpq-dev

# Create the custom user for the application to run as
RUN adduser --disabled-password --gecos "" ${user}
USER ${user}

# Create user-level R library folder
ENV R_LIBS_USER "/home/${user}/R/library"
RUN mkdir -p ${R_LIBS_USER}

# Copy relevant files and directories
RUN mkdir ${KONAN_SERVICE_BASE_DIR}
WORKDIR ${KONAN_SERVICE_BASE_DIR}
COPY . ${KONAN_SERVICE_BASE_DIR}

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
