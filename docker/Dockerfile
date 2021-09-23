################################################################################
# HOWTO use this file for local builds                                         #
################################################################################
# To build Khoca, run this command from your khoca/ directory:                 #
# $ docker build -f docker/Dockerfile --target=make-build --tag khoca .        #
# To run Khoca:                                                                #
# $ docker run -it khoca                                                       #
################################################################################
################################################################################
# Image containing the run-time dependencies for Khoca                          #
################################################################################
FROM ubuntu:latest
LABEL maintainer="Sebastian Oehms <seb.oehms@gmail.com>"
# Set sane defaults for common environment variables.
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash
# install requisites
RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends git g++ make libgmp-dev pari-gp2c python3 python3-dev python3-pip \
    && apt-get -qq clean \
    && rm -r /var/lib/apt/lists/* \
    && pip install cython \
    && git clone https://github.com/soehms/khoca.git \
    && cd khoca/ \
    && git checkout -b replace_mpir_by_gmp \
    && git pull origin replace_mpir_by_gmp \
    && make
WORKDIR "/khoca/"
COPY ./docker/entrypoint.sh /usr/local/bin/khoca-entrypoint
ENTRYPOINT ["/usr/local/bin/khoca-entrypoint"]
CMD ["bash"]
