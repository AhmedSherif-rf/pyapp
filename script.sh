#!/bin/bash
echo "number of problems is "
docker attach app
while read -r a; do
        echo  $a 
done < inputs

