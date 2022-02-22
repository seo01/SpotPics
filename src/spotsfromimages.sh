#!/bin/bash

#Arg1 is input path
#Arg2 is output path

for f in $1
do
	name=${f##*/}
	name=${name%%.*}
	echo $name
	python spot_svg.py $f $2/$name.svg
done