#!/bin/sh

cp -a /code/* /compile 
cd /compile
make

result=$?
if [ $result -ne 0 ]
    then
        echo "error occured during make, aborting..."
        exit $result
fi

if [ ! -z "$1" ]
    then
        echo running "$1"
        $1
fi
