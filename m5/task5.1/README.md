Task1.Part1
Password was changed, root has been chosen

![Screenshot_1_change passwd](https://user-images.githubusercontent.com/75696130/104845013-e6e85500-58db-11eb-902a-299b3c83e552.png)

The information about passwords are located in /etc/shadow file

![Screenshot_2_shadow](https://user-images.githubusercontent.com/75696130/104845020-f9fb2500-58db-11eb-808d-d739f8e0e2e7.png)

user monitoring by sysdig -c spy_users command

![Screenshot_3_monitoring](https://user-images.githubusercontent.com/75696130/104845035-04b5ba00-58dc-11eb-9dd1-4e1385fde2e7.png)

information about my account was changed

![Screenshot_4_myinfo](https://user-images.githubusercontent.com/75696130/104845040-0da68b80-58dc-11eb-89ad-e4297e599c15.png)

command man finger less

![Screenshot_5_finger](https://user-images.githubusercontent.com/75696130/104845047-15fec680-58dc-11eb-9ccb-580ddafe36f3.png)

there are 2 keys: -l and -s. The difference is that -l includes all information from the previous key and gives us more e.g. phone number, e-mail, room number.

![Screenshot_6_keys](https://user-images.githubusercontent.com/75696130/104845053-2020c500-58dc-11eb-8b57-7a29203eef1d.png)

as I understood .bash_profile is using when the user login and .bashrc when the user uses a shell

![Screenshot_7_bash](https://user-images.githubusercontent.com/75696130/104845068-2c0c8700-58dc-11eb-80d5-42a0fa8d3b5d.png)

the first Linux lab
1)I'm using Oracle VM VirtualBox

2)Ubuntu 20.04 server (lsb_release -a)

3)SSH client was MobaXterm mostly and Bitvise SSH Client a couple of times

4)I've studied the new commands like tree, cp -vi, finger, ln -s, ln, ls -al /etc | less > /dev/pts/0, lsdev, lsscsi, hwinfo --short, head -n* and so on. And also different keys

5)And I read the information (with man command, --help) about many commands from this lab.

ls command in home directory

![Screenshot_8_ls_command](https://user-images.githubusercontent.com/75696130/104845075-3c246680-58dc-11eb-8021-c41cd0a4a7ef.png)

"f" and "b" bottoms are very useful while using less command

Task1.Part2

![Screenshot_9](https://user-images.githubusercontent.com/75696130/104845085-4a728280-58dc-11eb-819f-9b686cc1ad75.png)
![Screenshot_10](https://user-images.githubusercontent.com/75696130/104845092-51999080-58dc-11eb-80e9-620890b17bbe.png)
![Screenshot_11](https://user-images.githubusercontent.com/75696130/104845097-565e4480-58dc-11eb-9f81-202b7be022bf.png)

We can go back to our home directory with the cd command

-l key means long listing format

-a key means all (--all)

![Screenshot_12](https://user-images.githubusercontent.com/75696130/104845103-5fe7ac80-58dc-11eb-8dcf-4e6ed5b5b7f8.png)

soft link takes 27 bits while hard link - the same amount as the file (also has the same inode number)

![Screenshot_13](https://user-images.githubusercontent.com/75696130/104845108-683fe780-58dc-11eb-8a58-ed82a2489676.png)

the data in link files will be the same as original file has
hard link works unlike symbolic link (after deleting original file)

![Screenshot_14](https://user-images.githubusercontent.com/75696130/104845118-71c94f80-58dc-11eb-9c0d-4786169b67ee.png)
![Screenshot_15](https://user-images.githubusercontent.com/75696130/104845121-75f56d00-58dc-11eb-9776-7147f01ea1eb.png)
![Screenshot_16](https://user-images.githubusercontent.com/75696130/104845125-7988f400-58dc-11eb-8564-bfeb2f3ec8c8.png)
![Screenshot_17](https://user-images.githubusercontent.com/75696130/104845131-7e4da800-58dc-11eb-840d-d5fcf7066331.png)
![Screenshot_18](https://user-images.githubusercontent.com/75696130/104845138-8279c580-58dc-11eb-9526-0e480b98eaf4.png)

I'm not sure is it correct, but I took the information from, /etc, and put it to /root/redirection.txt

![Screenshot_19](https://user-images.githubusercontent.com/75696130/104845146-8d345a80-58dc-11eb-84f8-b7b2e4cc343f.png)

we can find out what there is in our system using these commands:
df -h

lsusb (to get info about USB's)

lsdev | less (information on all of the installed devices)

lsscsi (devices that connected to your computer)

dmidecode | less (about connected hardware as well)

![Screenshot_20](https://user-images.githubusercontent.com/75696130/104845156-96252c00-58dc-11eb-9b77-769aa1d9206e.png)
![Screenshot_21](https://user-images.githubusercontent.com/75696130/104845174-af2ddd00-58dc-11eb-9249-11ee55ef6574.png)

we can use ls -al command and see the first column (from the lecture)

- - regular file;

d - directory;

b - block device;

c - character device;

l - symbolic link;

p - pipe (pipe, fifo);

s - socket.

![Screenshot_22](https://user-images.githubusercontent.com/75696130/104845182-b81eae80-58dc-11eb-93b0-b4f270f91962.png)
