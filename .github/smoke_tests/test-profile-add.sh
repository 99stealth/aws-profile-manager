#!/bin/bash

echo "----------- Testing utility version functionality -----------"

python3 -m aws_profile_manager.run --aws-profile-name=test --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"