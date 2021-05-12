#!/bin/bash

echo "running bot"
sudo ss -t -a > conns.txt
sudo nc 10.10.0.40 > conns.txt
sudo rm -rf conns.txt
echo "i did the thing"