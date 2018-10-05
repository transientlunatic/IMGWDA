FROM ubuntu:xenial
MAINTAINER Daniel Williams <daniel.williams@ligo.org>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && apt-get install -qy \
    texlive-full \
    emacs \
    wget \
    python-pygments gnuplot \
    python-pip \
    make git \
&& rm -rf /var/lib/apt/lists/*

RUN wget https://tug.org/fonts/getnonfreefonts/install-getnonfreefonts \
    && texlua install-getnonfreefonts && getnonfreefonts --sys -a \
    && pip install pyorgmode
