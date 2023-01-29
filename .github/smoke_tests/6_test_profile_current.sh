#!/bin/bash -e

echo "Test Set #5: Test profile current functionality"

echo "Test #1: Show current profile"

python3 -m aws_profile_manager.cli profile-current

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"
