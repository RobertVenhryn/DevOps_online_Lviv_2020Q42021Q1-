Part 1
1)Running/Runnable (R), Sleeping (S/D), Stopped (T), Zombie (Z)

2)to display a tree of processes we use pstree command. pstree -H PID to highlight certain process

![Screenshot_1](https://user-images.githubusercontent.com/75696130/106194465-8c8ea480-61b7-11eb-8e80-b79415a277cd.png)

3)when we ask for some information from the kernel by typing top command, it gives us a snapshot of the system's current state. /proc is a mechanism that helps us to get underlying kernel data, it is an interface that provides interacting between user and kernel

4)cat /proc/cpuinfo | less

5)"ps -leF" and "ps aux"

6)kernel processes have the process id (PID) = 2  (e.g. kthread)
sudo ps --pid=2
sudo ps --ppid=2
All the rest - user processes (PID ≠ 2)
sudo ps -N --pid=2
sudo ps -N --ppid=2

7)Running/Runnable (R) means a process is using a CPU right now or has everything to be run (Runnable). Sleeping (S/D) - the process is just waiting for a.g. I/O operation, event. It becomes Stopped (T) after receiving SIGSTOP signal. Zombie (Z) - when a process finishes, but parent process isn't programmed properly and newer calls wait(). We can see zombie processes using top command.
From the interruptible sleep, a process can get a wake-up signal and become running and vice versa. From the running state, it can be stopped (SIGSTOP)/go to uninterruptible sleep/become a zombie.

![Screenshot_2](https://user-images.githubusercontent.com/75696130/106194511-9dd7b100-61b7-11eb-80a7-7f674dcfda9f.png)

8)
![Screenshot_3](https://user-images.githubusercontent.com/75696130/106194534-a6c88280-61b7-11eb-82ed-20400b5faad4.png)

![Screenshot_4](https://user-images.githubusercontent.com/75696130/106194576-b051ea80-61b7-11eb-9de0-fb1a145670d9.png)

9)
![Screenshot_5](https://user-images.githubusercontent.com/75696130/106194619-bf389d00-61b7-11eb-8d53-a52edca4be13.png)

10)It shows the amount of time: that the CPU spends, time lost due to running virtual machines, CPU idle time, and many things in the dashboard. The new for me from the process list is RES (amount of resident memory used by the process), SHR (Amount of shared memory used by the process), TIME+ (Total CPU time used by the task in hundredths of a second). This command gives us much more than mentioned above.

![Screenshot_6](https://user-images.githubusercontent.com/75696130/106194641-c65fab00-61b7-11eb-8c73-048d3feedf03.png)

11)we have to press u and type the name

![Screenshot_7](https://user-images.githubusercontent.com/75696130/106194664-ccee2280-61b7-11eb-97b2-1eafcd5b7e97.png)

12)we can type t to display CPU as a line. After pressing m letter - we will change the memory look. Or even  t and m simultaneously. Z letter to change color. We can sort by memory (M), CPU (P), PID (N), Time+ (T)

13)
![Screenshot_8](https://user-images.githubusercontent.com/75696130/106194707-d9727b00-61b7-11eb-943b-7be90f3bc0be.png)
![Screenshot_9](https://user-images.githubusercontent.com/75696130/106194716-dc6d6b80-61b7-11eb-84af-a910f67303c4.png)

14-15)there are two of them nice and renice. we can use nice command if we want to start the process with some priority and renice, when we need to change it. From the top command, we can do the same using r command.

![Screenshot_10](https://user-images.githubusercontent.com/75696130/106194734-e3947980-61b7-11eb-91df-701e36e98ab9.png)
![Screenshot_11](https://user-images.githubusercontent.com/75696130/106194744-e68f6a00-61b7-11eb-9597-d7dfe85c4959.png)

16)we can send different signals to processes with the kill command. kill -15 PID used to ask a process to stop, kill -9 PID will stop the process immediately and we can lose data if the process was connected to another.

![Screenshot_12](https://user-images.githubusercontent.com/75696130/106194769-f0b16880-61b7-11eb-94b0-612c7a694f0e.png)

17)bg - command to restart a process and force it to work in the background. to start a command in the background - bg sleep 500 & to move running the command in the background - bg jobnumber. To move it to the foreground - fg %1. The fg command has now brought the system back into a sleep state. Nohup command will send any output of running commands to the file nohup.out in the working directory or /home/userdir. nohup mycommand & will run the command in the background.

![Screenshot_13](https://user-images.githubusercontent.com/75696130/106194805-f909a380-61b7-11eb-905e-ac874bbc3688.png)
![Screenshot_14](https://user-images.githubusercontent.com/75696130/106194813-fc049400-61b7-11eb-9732-9094bd23f0a4.png)
![Screenshot_15](https://user-images.githubusercontent.com/75696130/106194820-fe66ee00-61b7-11eb-9a45-5212696eac10.png)

Part2
1)
![Screenshot_16](https://user-images.githubusercontent.com/75696130/106194870-10489100-61b8-11eb-9a2e-801fbde955b5.png)
![Screenshot_17](https://user-images.githubusercontent.com/75696130/106194879-13dc1800-61b8-11eb-9479-73ed34accea0.png)
![Screenshot_18](https://user-images.githubusercontent.com/75696130/106194885-163e7200-61b8-11eb-9b1e-c36c6c44fd78.png)

I can't connect from my VM to the host OS - Windows 10 via SSH

2)I've created a pair of keys and put public key info into the file in another ubuntu server /home/robert/.ssh/authorized_key
And after typing ssh robert@192.168.0.113 it has been connected.

![Screenshot_19](https://user-images.githubusercontent.com/75696130/106194922-22c2ca80-61b8-11eb-8b1a-e2dfd6b70da2.png)
![Screenshot_20](https://user-images.githubusercontent.com/75696130/106194929-25bdbb00-61b8-11eb-8068-01e532b72bd9.png)

3)
![Screenshot_21](https://user-images.githubusercontent.com/75696130/106194951-2bb39c00-61b8-11eb-9b6e-5e7ecbf3cbea.png)

4)I've made port forwarding on VirtualBox and my VM has a connection to the internet. But there is a strange result after typing traceroute 8.8.8.8

![Screenshot_22](https://user-images.githubusercontent.com/75696130/106194966-31a97d00-61b8-11eb-9dfd-b2200d81d91a.png)

5)
![Screenshot_23](https://user-images.githubusercontent.com/75696130/106194980-3b32e500-61b8-11eb-995a-30d6c00dd524.png)

I've chosen bbc.com to test. I typed "ping bbc.com" from another terminal and got this screen with information:  robert-VirtualBox > 151.101.0.81: ICMP echo request, id 5, seq 1, length 64.

![Screenshot_24](https://user-images.githubusercontent.com/75696130/106195003-4259f300-61b8-11eb-88cc-d9187da2841b.png)

This is telnet connection. I printed a command "ip a" from the terminal (telnet) and got these messages (screen below)

![Screenshot_25](https://user-images.githubusercontent.com/75696130/106195022-48e86a80-61b8-11eb-8f15-ce9418165994.png)

if we are using SSH - a boundless current of info appears (screen below)

![Screenshot_26](https://user-images.githubusercontent.com/75696130/106195046-500f7880-61b8-11eb-98c9-d42de34907b3.png)
![Screenshot_27](https://user-images.githubusercontent.com/75696130/106195054-530a6900-61b8-11eb-8157-7f4b33a2621a.png)

It shows us: the most used IP is V4 and TCP has 99.7% of the traffic

![Screenshot_28](https://user-images.githubusercontent.com/75696130/106195082-5bfb3a80-61b8-11eb-9c06-6cf6e87399cb.png)
![Screenshot_29](https://user-images.githubusercontent.com/75696130/106195092-5f8ec180-61b8-11eb-9896-85cba4b6dda6.png)
