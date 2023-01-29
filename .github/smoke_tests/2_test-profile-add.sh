#!/bin/bash -e

echo "Test #1. Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY"

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test1 --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #2. Add existing AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY"

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test1 --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ

if [ $? == 1 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "Test #3. Add AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_SESSION_TOKEN"

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test2 --aws-access-key-id=ASIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ --aws-session-token asdgsdhafshaerhaerhserhafhash

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #4. Provide invalid AWS_ACCESS_KEY_ID"

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test3 --aws-access-key-id=AZIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zZ

if [ $? == 1 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #5. Provide invalid AWS_SECRET_ACCESS_KEY"

python3 -m aws_profile_manager.cli profile-add --aws-profile-name=test3 --aws-access-key-id=AKIAAAAAAAAAAAAAAAAA --aws-secret-access-key=Aa1Aa0a

if [ $? == 1 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"