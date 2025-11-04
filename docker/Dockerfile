# use latest alpine image as base
FROM alpine:latest
# update package manager
RUN apk update && apk upgrade
# install required packages
RUN apk add --no-cache nasm make binutils gdb xxd gcc

# copy gdb config files
COPY .gdbearlyinit /root/.gdbearlyinit
COPY .gdbinit /root/.gdbinit

COPY compile.c /root/compile.c
RUN ["gcc", "compile.c", "-o", "/bin/compile"]

# setup for make
WORKDIR /code
WORKDIR /compile

COPY get_executable.py /scripts/get_executable.py
COPY make.sh /scripts/make.sh
RUN ["chmod", "+x", "/scripts/make.sh"]

ENTRYPOINT ["compile"]
