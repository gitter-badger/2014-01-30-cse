#!/bin/bash

mkdir 2012-07-03

for file in 2012-07-03/*.txt ; do
    echo $file
    dd if=/dev/urandom of=$file bs=100 count=3
done
