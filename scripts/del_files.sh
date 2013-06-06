#!/bin/bash
COUNTER=0
while read p; do
  rm "$p"
  let COUNTER=COUNTER+1 
done < $1
echo $COUNTER
