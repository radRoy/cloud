# Installation of the unet fiji plugin

Creation date: 27. Feb. 2023  
Author: Daniel Walther (information sources are given)

This document is for documenting the process, difficulties, solutions and specifics regarding the whole backend installation process of the U-Net Fiji Plugin.

## The official web resource of U-Net

https://lmb.informatik.uni-freiburg.de/resources/opensource/unet/#installation-prerequisites  
(link to the written instructions, not the installation tutorial video ( https://lmb.informatik.uni-freiburg.de/resources/opensource/unet/#installation ))  
- - -  
Content  
    Installation  
        Prerequisites  
        Backend (Server) Setup  
            Setup on Amazon Elastic Compute Cloud (EC2)  
            Setup on own Server (using pre-built binaries)  
            Setup on own Server (from source)  
        Frontend (Client) Setup  
    Using the FiJi U-Net Segmentation plugin with the pretrained 2D network for cell segmentation  
        Walk-through example  
        U-Net Segmentation parameters  
    Troubleshooting  
- - -  
(above list is an overview of the content of this website on uni-freiburg.de)  

### Prerequisites

You need a computer for runnning the backend (caffe_unet) and a computer for running the frontend (ImageJ with our U-Net plugin).  
> Frontend: check.  
> Backend: TBD (what this document is for, writing down the process of this backend installation).  
You can run the frontend on the same computer as the backend if desired.  
Frontend (Client) requirements:  
    Linux, Windows or MacOS (requires Java 8)  
> check  
Backend (Server) requirements:  
    Ubuntu Linux (16.04 recommended to use binary distribution)  
    (optional) NVIDIA GPU (e.g. TitanX, GTX1080, GTX980 or similar) for faster runtimes; Requires CUDA 8.0 (Additionally cuDNN 6 or 7 is recommended for large tiles esp. in 3D)  
    (optional) Mathworks MATLAB (TM) R2015a or newer for measuring GPU memory  
> TBD.  

- ubuntu 16.04 or 18.04 work - ubuntu 20.04.5 is installed on lils  
version of the new server: `Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-139-generic x86_64)`  
version of the old server: `Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-210-generic x86_64)`  
- CUDA 8.0 works, CUDA 10.2 installed on old server

`lic@u-net:~$ nvidia-smi`  
Mon Feb 27 15:23:11 2023  
+-----------------------------------------------------------------------------+  
| NVIDIA-SMI 440.64.00    Driver Version: 440.64.00    CUDA Version: 10.2     |  
|-------------------------------+----------------------+----------------------+  
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |  
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |  
|===============================+======================+======================|  
|   0  GeForce GTX 108...  Off  | 00000000:65:00.0 Off |                  N/A |  
| 64%   80C    P2   112W / 250W |   2569MiB / 11175MiB |     78%      Default |  
+-------------------------------+----------------------+----------------------+  
																			     
+-----------------------------------------------------------------------------+  
| Processes:                                                       GPU Memory |  
|  GPU       PID   Type   Process name                             Usage      |  
|=============================================================================|  
|    0      1716      G   /usr/lib/xorg/Xorg                           105MiB |  
|    0     25247      C   ...e/lic/caffe_unet/build/tools/caffe_unet  2449MiB |  
+-----------------------------------------------------------------------------+  

- cuDNN 6 or 7 for large tiles and 3D stuff  
TBD  
- (opt) Matlab R2015a or newer  
TBD (ignore for now)  

### building docker server image from source (building the caffe-unet-docker image on a fresh ubuntu installation, from source, on a server)

```bash
popsicle@t480:~/unet/caffe-unet-docker$ make src
 docker build -f Dockerfile-src -t lmb-unet-server-src .
 Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
 make: *** [Makefile:12: src] Error 1
```  
googling the installation of docker engine (searching for the linux CLI solution, since on lils001, there is only linux (ubuntu 20.04) installed.  
https://docs.docker.com/engine/install/  
**(*1)**  
https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux  
> Install daemon and client binaries on Linux
> Prerequisites
> 
> Before attempting to install Docker from binaries, be sure your host machine meets the prerequisites:
> 
>     - A 64-bit installation
>     - Version 3.10 or higher of the Linux kernel. The latest version of the kernel available for your platform is recommended.
>     - iptables version 1.4 or higher
>     - git version 1.7 or higher
>     - A ps executable, usually provided by procps or a similar package.
>     - XZ Utils 4.9 or higher
>     - A [properly mounted](https://github.com/tianon/cgroupfs-mount/blob/master/cgroupfs-mount) `cgroupfs` hierarchy; a single, all-encompassing `cgroup` mount point is not sufficient. See Github issues [#2683](https://github.com/moby/moby/issues/2683), [#3485](https://github.com/moby/moby/issues/3485), [#4568](https://github.com/moby/moby/issues/4568).  

All except the last point/requirements are met, this last point causes me some trouble (refer to the "properly mounted" link, some bash script about setting up the proper file system (?, guess based on the `...fs` part).)  
TBD: review some `bash` and `awk` syntax.

**(*1)** changing approach from full-on only CLI based (ubuntu within WSL2) installation, to incremental (step by step) progress which I can completely follow.  

The 1st step here is to install the [Desktop Docker Engine](https://docs.docker.com/desktop/install/windows-install/) for Windows to try and fix the `Cannot connect to the Docker daemon ...` error when running the `make src` command.  
This docker installation:  
- "Installing Docker Desktop 4.17.0 (99724)"
- [x] (yes) "use WSL2 instead of Hyper-V (recommended)"