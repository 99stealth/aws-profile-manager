#!/bin/bash -e

echo "Test Set #4: Test profile remove functionality"

echo "Test #1: Remove profile"

python3 -m aws_profile_manager.cli profile-remove --aws-profile-name=test1 --yes

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #2: Remove not existing profile"

python3 -m aws_profile_manager.cli profile-remove --aws-profile-name=test --yes

if [ $? == 1 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"