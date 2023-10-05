#!/bin/sh

mkdir big-directory
cd big-directory/

mkdir small-directory
cd small-directory/

touch file-1.txt
echo "Elijah Guzman"|cat > file-1.txt

seq 1 1 20 >> file-1.txt
cat file-1.txt

wc -w <file-1.txt>>file-2.txt
cat file-2.txt

cp file-1.txt ../file-1.txt
mv file-1.txt file-3.txt

cd ../
rm -r small-directory
ls -l
cd ../
rm -r big-directory
ls -l
