#!/bin/bash -e

echo "Test Set #4: Test profile remove functionality"

echo "Test #1: Edit profile with AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY"

python3 -m aws_profile_manager.cli profile-edit --aws-profile-name=test1 --aws-access-key-id=AKIAAAAAAAAAAAAAAAAZ --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zA

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"

echo "Test #2: Edit profile AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_SECURITY_TOKEN"

python3 -m aws_profile_manager.cli profile-edit --aws-profile-name=default --aws-access-key-id=ASIAAAAAAAAAAAAAAAAZ --aws-secret-access-key=Aa1Aa0az00+AzA/01AzZZZz0Z0z0ZzzZZzZZz0zA --aws-session-token asdgsdhafshaerhaerhserhafhashagfagwaerg

if [ $? == 0 ]; then 
    echo "[+] Test Passed"
else
    echo "[-] Test Failed"
    exit 1
fi

echo "--------------------------------------------------------------"