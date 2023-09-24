#!/bin/bash

echo "TEST TEXT" | cat > input.txt
cat input.txt

rm -r copy1.txt
rm -r copy2.txt

cat input.txt >  copy1.txt
cat input.txt >  copy2.txt

cat copy1.txt
cat copy2.txt


