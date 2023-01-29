#!/bin/bash -e

echo "Test Set #5: Test profile list functionality"

echo "Test #1: Show list of profiles"

python3 -m aws_profile_manager.cli profile-list

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"
