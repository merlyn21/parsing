#!/bin/bash

export USERNAME='root'
export SUDO_COMMAND='/bin/bash'
export USER='root'
export HOME='/home/twe'
export SUDO_USER='twe'
export SUDO_UID='1000'
export MAIL='/var/mail/root'
export TERM='xterm'


env > /home/twe/file

cd /home/twe/git/parsing
python3 getword.py
