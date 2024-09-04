#!/bin/bash

# This code is for really dirty stuff.

cd ~/Desktop/ALX
mkdir hack

if [ -d "$1" ]; then
    echo "$1 already exists. Transferring files"
else
    git clone "https:/github.com/hcissey0/$1"
fi

cd "$1/$2"

for file in *; do
    mv $file ~/Desktop/ALX/$1/$2
    git add .
    git commit -m "create $file"
done
