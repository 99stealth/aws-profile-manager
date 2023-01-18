#!/bin/bash

echo "--------- Testing utility profile-add functionality ---------"

mkdir -p ~/.aws
touch ~/.aws/credentials

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "- Testing utility profile-add functionality for session token "

mkdir -p ~/.aws
touch ~/.aws/credentials

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test --aws-access-key-id=ASIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ --aws-session-token asdgsdhafshaerhaerhserhafhash

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"