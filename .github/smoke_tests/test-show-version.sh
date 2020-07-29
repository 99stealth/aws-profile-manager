#!/bin/bash

echo "------------------ Testing with image names ------------------"

python3 -m aws_profile_switcher.run --version

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"