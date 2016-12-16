Signal Processing Emulator
==============

This folder contains everything needed to cross-compile your codes on your local machine and then execute them on your RedPitaya.

## Content ##

| File                  | Description
|-----------------------|-----------------------------------------
| `install.sh`          | Red Pitaya sdk install script
| `run.sh`              | Run and execute script
| `Makefile`            | Red Pitaya compile Makefile


## Instalation procedure  ##

First run the install script using the command below:
```bash
sudo ./install.sh
```

This will install a few programs including the linaro hf compiler needed to compile Red Pitaya compatible programs. It will also set all the needed environmental variables.

#### Installed programs ####

- nano
- curl
- putty-tools
- Linaro compiler

#### Modified variables ####

- PATH : Add `linaro` path to the PATH environment variable
- CROSS_COMPILE : Add the `CROSS_COMPILE` environment variable set to linaro bin path

## Run program on RedPitaya from your local machine ##

Connect to your RedPitaya as an Access Point.
As far as we know, RedPitaya will have the static IP adress `REDPITAYA_IP` set to 192.168.128.1
If not, use your OS common tools to get its IP on your network.

Suppose you want to run the `implementation`, then run the following command:

```bash
./run.sh `REDPITAYA_IP` `implementation`
```

The program will take the IP address and the given file. It will compile our srcbin/implementation.c to an executable, send it to a RedPitaya with the given IP and execute it. You will see a sample output in your console. You can also see the output given in /var/log/sdk_log/debug.
