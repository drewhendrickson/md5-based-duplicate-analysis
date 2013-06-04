#!/bin/bash
COUNTER=1
while read p; do
#  echo "========"
#  echo "$p"
  cp -i "$p" $2/$COUNTER.$(basename $p)
  let COUNTER=COUNTER+1 
done < $1
