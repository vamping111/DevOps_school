#!/bin/bash
cd /root/git/dir_1/
git clone https://github.com/vamping111/DevOps_school.git
cd /root/git/dir_2/
git clone https://github.com/vamping111/DevOps_school.git
#cd /root/git/dir_1/DevOps_school
echo "Linar_Nasyrov_Test_Text" > /root/git/dir_1/DevOps_school/some_file.txt
echo "Linar_Nasyrov_Test_Text" > /root/git/dir_2/DevOps_school/some_file.txt

cd /root/git/dir_1/DevOps_school
git add some_file.txt
git commit -m "some comment0033"

cd /root/git/dir_2/DevOps_school
git add some_file.txt
git commit -m "some comment0033"
