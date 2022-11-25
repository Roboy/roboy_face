#!/bin/bash

nmap -sn 192.168.1.0/24
faceip=$(arp -n | grep -w -i '00:0e:c6:ac:ca:2b' | awk 'NR==1{print $1}')
adb disconnect ${faceip}
adb connect ${faceip}
sleep 2
adb shell reboot -p
