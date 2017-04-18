#!/bin/bash

for f in *.zip
do
	echo "Deflating $f"
	unzip -P infected $f
done
