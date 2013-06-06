#!/bin/bash
COUNTER=1
while read p; do
#  echo "========"
#  echo "$p"
  cp "$p" "$2/$COUNTER.$(basename "$p")"
  let COUNTER=COUNTER+1 
  echo $(basename "$p")
done < $1
