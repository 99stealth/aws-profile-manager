#!/bin/bash

echo "----------- Testing utility version functionality -----------"

python3 -m aws_profile_manager.cli --version

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"