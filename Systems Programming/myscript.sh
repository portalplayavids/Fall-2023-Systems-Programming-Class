#!/bin/sh

ls -alh

echo "creating hello.txt"
touch hello.txt
echo "finished creating hello.txt"

ls -alh
rm hello.txt
ls -alh