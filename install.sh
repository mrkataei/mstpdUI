#!/bin/bash
git clone https://github.com/mstpd/mstpd.git
cd mstpd/
./autogen.sh
./configure 
make
export projectDir=$PWD
cd /usr/local/bin
sudo ln -s $projectDir/mstpd mstpd
sudo ln -s $projectDir/mstpctl  mstpctl

