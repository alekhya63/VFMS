#!/bin/bash

username=$(awk -F"," '{print $1}' ACL_USER_CREATE.txt | tr 'A-Z' 'a-z')
role=$(awk -F"," '{print $2}' ACL_USER_CREATE.txt | tr 'A-Z' 'a-z')
password="{$username}+'12345'"

for user in $username
do
sudo useradd $user

done


sudo groupadd -f studentgroup

sudo usermod -a -G studentgroup user1


path=$( getent passwd "$USER" | cut -d: -f6 )
folder1="VFMS_test2"
folder2="student"
folder3="assignments"
folder4="personal"

mkdir -p "$path/$folder1"

mkdir -p "$path/$folder1/$folder2"

mkdir -p "$path/$folder1/$folder2/$folder3"

mkdir -p "$path/$folder1/$folder4"

sudo chown -R user2 "$path/$folder1"

exit 0





