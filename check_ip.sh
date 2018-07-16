#!/bin/bash
ip=$(curl ipinfo.io/ip)
if [ $ip == "207.237.45.181" ]
then
 echo "Ip is same"
else
 echo "IP changed"
fi

