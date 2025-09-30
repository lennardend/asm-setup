#!/bin/sh

cp -a /code/* /compile 
cd /compile
make

echo running $1
$1
