#! /bin/sh

for dir in `ls -d */`; do
    cd $dir;
    for file in `ls *.py`; do
        coverage run $file;
    done;
    cd ..;
done
