# use latest alpine image as base
FROM ubuntu:latest
# update package manager
RUN apt update && apt upgrade
# install required packages
RUN apt -y install nasm make binutils gdb xxd gcc python3

# copy gdb config files
COPY .gdbearlyinit /root/.gdbearlyinit
COPY .gdbinit /root/.gdbinit

# setup for make
WORKDIR /code
WORKDIR /compile

COPY get_executable.py /scripts/get_executable.py

ENTRYPOINT ["python3", "/scripts/get_executable.py"]
