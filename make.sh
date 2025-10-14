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

echo running $1
$1
