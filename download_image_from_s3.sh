#!/bin/sh
file="random.txt"
lines=`cat $file`
for line in $lines; do
        url="s3://tomandjerrycomicl/${line}"
        aws s3 cp $url "image_0414/${line}"
done