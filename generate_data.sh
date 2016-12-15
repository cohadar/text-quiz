#!/bin/sh
GENERATORS=`ls generators/*.py`
for generator in $GENERATORS
do
	name=`basename -s .py $generator`
	target=data/${name}.qadb
	python $generator > $target
	echo $target
done
