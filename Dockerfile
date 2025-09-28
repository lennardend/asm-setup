# use latest alpine image as base
FROM alpine:latest
# update package manager
RUN apk update && apk upgrade
# install required packages
RUN apk add nasm make binutils

WORKDIR /code
WORKDIR /compile

COPY make.sh /scripts/make.sh
RUN ["chmod", "+x", "/scripts/make.sh"]

ENTRYPOINT ["/scripts/make.sh"]
CMD ["./main"]
