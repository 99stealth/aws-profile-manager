#!/bin/bash

echo "-------- Testing utility profile-remove functionality --------"

mkdir -p ~/.aws
touch ~/.aws/credentials

python3 -m aws_profile_manager.cli profile-remove --aws-profile-name=test --yes

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"