#!/bin/bash

echo "Test #1. Show version and exit"

python3 -m aws_profile_manager.cli --version

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #2. Show help message and exit"

python3 -m aws_profile_manager.cli --help

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"