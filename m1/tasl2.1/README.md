1. What are the most popular hypervisors for infrastructure virtualization?

the most popular hypervisors are Xen, Hyper-V, Vmware, KVM, KVM w/OpenStack

2. Briefly describe the main differences of the most popular hypervisors.

VMware takes leading positions and has a free trial version in case you don't need all advantages
KVM is an open-source hypervisor with all the features of Linux. This makes it very popular for enterprises.
Microsoft Hyper-V is a worthy opponent to VMware, it also has a free license. In case you need GUI you will take on of the commercial versions.
Citrix Hypervisor (formerly known as Xen Server) is the best choice for enterprises. There is the proprietary feature with Intel, NVIDIA, and workload security with Direct Inspect APIs.

my VM's and settings
![Screenshot_2](https://user-images.githubusercontent.com/75696130/102225593-15939a00-3ef0-11eb-806a-e8b5e3b0a768.png)

![Screenshot_1](https://user-images.githubusercontent.com/75696130/102225629-1d533e80-3ef0-11eb-8bb5-c27dea57c349.png)

to create shared folder samba has been installed manually

![Screenshot_7](https://user-images.githubusercontent.com/75696130/102225678-293f0080-3ef0-11eb-8a81-99be6d750b73.png)

I've had problems with the connection between VMs. I configure IP addresses instead of DHCP but my machines don't see each other

![Screenshot_3](https://user-images.githubusercontent.com/75696130/102225708-352ac280-3ef0-11eb-9940-1197fde1c45f.png)

(but have a connection with the internet)
![Screenshot_4](https://user-images.githubusercontent.com/75696130/102225799-4673cf00-3ef0-11eb-9101-553672b08a1a.png)

In my view, there is a problem with NAT configuration or so.

With the bridge adapter, everything working.

I've installed VirtualBox on Ubuntu gest machine and tried different CLI commands.

![Screenshot_5](https://user-images.githubusercontent.com/75696130/102225845-54c1eb00-3ef0-11eb-84ef-30e1d901f96a.png)

![Screenshot_6](https://user-images.githubusercontent.com/75696130/102225865-5b506280-3ef0-11eb-9635-3c259105c83f.png)

Work with Vagrant
I created folder Robert_Venhryn with vagrantfile and connected via Putty

![Screenshot_8_vagrant_vm_up](https://user-images.githubusercontent.com/75696130/102225900-67d4bb00-3ef0-11eb-94e6-197dd9adc9d1.png)

![Screenshot_9_vm_ssh](https://user-images.githubusercontent.com/75696130/102225920-6c996f00-3ef0-11eb-9997-8c59bcd75995.png)
