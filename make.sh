#!/bin/sh

cp /code/* /compile 
cd /compile
make

$1
