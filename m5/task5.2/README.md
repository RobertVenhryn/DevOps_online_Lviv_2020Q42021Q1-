1)There are several fields in passwd file (username, password, UID, GID, GEOS, home directory, login shell) and in the group file (group name, password, GID, group list). We have common users and pseudo-users (which can be defined by their default shell, like /bin/false, /sbin/nologin. pseudo-users: bin, sys, man, deamon, adm, sshd, nobody users) user id is also important: 1-999 are daemons, pseudo-users, system and reserved users. >1000 - regular users

![Screenshot_1](https://user-images.githubusercontent.com/75696130/105391520-dceb8c80-5c22-11eb-91c3-8a54141275e6.png)

2)UID is the special identifier of a user. we can see it in the third place after password "x". UID range is a sequence of ids that are given by the system to users, pseudo-users, and so on. 0-root, 1-999 deamons, pseudo-users, system (from the lecture). we hawe to type cut -d: -f1,3 /etc/passwd and we will see UID

![Screenshot_2](https://user-images.githubusercontent.com/75696130/105391562-e83eb800-5c22-11eb-98ac-1bcdfc482d9e.png)


3)GID is the special identifier of a group. we can see it in the third place after password "x" if we open /etc/group file. GID is a sequence of id`s that are given by the system. we can. Useful commands are id -g (which gives you GID of current user), more /etc/group...

![Screenshot_3](https://user-images.githubusercontent.com/75696130/105391597-ef65c600-5c22-11eb-88f7-8411e58c1050.png)

4)We can do it using /etc/group file. Different users can belong to the same group or they can be in different.

5)As fur as I'm concerned there are 2 the most popular commands: adduser and useradd. I mostly use adduser because I can set the password, user's home directory creates at once, the default shell is bash.
We have to define user`s name and password (also we can give additional information like phone number and "other" info)

![Screenshot_4](https://user-images.githubusercontent.com/75696130/105391646-fee50f00-5c22-11eb-8c35-9f23a8cba9d2.png)
![Screenshot_5](https://user-images.githubusercontent.com/75696130/105391670-05738680-5c23-11eb-807b-28afc50a9e38.png)

6)We can change user's name by this command: usermod -l newlogin oldlogin. Also we can change UID by this: usermod -u [NEW_USER_ID] [USERNAME]

![Screenshot_6](https://user-images.githubusercontent.com/75696130/105391702-102e1b80-5c23-11eb-9e21-68e5d07e5d24.png)

7)/etc/skel contains the default files for new users. It will be copied to the new user's home directory.
we can add /etc/skel/useradd file to change the default directory of a new user.

![Screenshot_7](https://user-images.githubusercontent.com/75696130/105391736-17552980-5c23-11eb-913e-62cfb6c27cb0.png)

8)"userdel -r username" command

9)the command "passwd -l user_name" to lock and "passwd -u username" to unlock the same with these commands "usermod -L user_name" "usermod -U username" But these commands will work just with login via username, and allow the user to log in via SSH keys.
To disable acces by SSH we have to use "usermod -s /sbin/nologin username"

10)We can do so with SSH key pair
the first step is creating the key:
ssh-keygen -t rsa -b 4096 -C "your_email@domain.com"
to check it:
ls ~/.ssh/id_*
now we have to send it to the remote host:
ssh-copy-id remote_username@server_ip_address
and now we can log in:
ssh remote_username@server_ip_address

![Screenshot_8](https://user-images.githubusercontent.com/75696130/105391789-26d47280-5c23-11eb-8451-919d27512993.png)
![Screenshot_9](https://user-images.githubusercontent.com/75696130/105391805-2b009000-5c23-11eb-81ad-613b35e610f5.png)

11)
![Screenshot_10](https://user-images.githubusercontent.com/75696130/105391840-318f0780-5c23-11eb-8f8f-a79e2d85eb7c.png)


12-13)Each file and folder has owner, group, others permission. You can read, write or execute a file. To change the permission we can use "chmod" command. Also there are special permission flags: - (no special permission), d (irectory), l (simbolic link), s (to tell the system run executable files with owner permission), t (Useful in shared enwironment. Only file owner can rename or delete the file). We can define permission with chmod +/-/= filename. + to add a permission, - to pick up, and = to owerrite a permission. There is also number form of permission types.

14)To do so we user chown command. For changing group owner of a file or directory: "chgrp new_user_group filename". To change the user owner and group to root a.g. "sudo chown root:root agatha.txt"
скрін11
we can give a permission to execute files in the directory for users in group: "chmod g+s testdirectory -R". S means group users couldn't execute these files. We had to give them "chmod g+x" before that.

![Screenshot_12](https://user-images.githubusercontent.com/75696130/105391889-3fdd2380-5c23-11eb-9a7e-3d1b90941021.png)
![Screenshot_13](https://user-images.githubusercontent.com/75696130/105391929-4b304f00-5c23-11eb-9927-a6b9cd13a384.png)

15)The default access rights can be set by umask command. We can prohibit access to the new files from "Others" in this way: umask 770
Or give anybody only read permission to the new directories and full access by the owner: umask 33 (because 777-774=33)

![Screenshot_14](https://user-images.githubusercontent.com/75696130/105391953-508d9980-5c23-11eb-9522-31b53805e0d5.png)

16)Sticky bit is a protection mechanism of a folder. It concerns "Others" to avoid deleting files in the folder. There are two ways to add the sticky bit: chmod o+t /home/robert1/test
another: chmod 1757 /home/robert1/test
Here in 1757, 1 indicates Sticky Bit set, 7 for full permissions for owner, 5 for read and execute permissions for group, and full permissions for others.

![Screenshot_15](https://user-images.githubusercontent.com/75696130/105391979-54b9b700-5c23-11eb-9ed9-26eb9c8fc03f.png)

I'v found the command to locate files with sticky bits: "find . -perm -1000"

![Screenshot_16](https://user-images.githubusercontent.com/75696130/105391994-597e6b00-5c23-11eb-84f7-0ee29e2c4020.png)


17)Command script has to be executable to be run:
"chmod ugo+x filename"
