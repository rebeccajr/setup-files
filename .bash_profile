#_______________________________________________________________________________
# .bash_profile
# 
# This file contains aliases and environment variables.
#_______________________________________________________________________________

alias src='source ~/.bash_profile'

#_______________________________________________________________________________
# EDIT SETTINGS

alias vimb='vim ~/.bash_profile; src'
alias vimv='vim ~/.vimrc'
alias vimt='vim ~/.tmux.conf'
alias vimz='vim ~/.zshrc'


#_______________________________________________________________________________
# NAVIGATION

alias save='export TEMP_DIR=$PWD'
alias return=' cd $TEMP_DIR'

export GIT_PATH=~/git
export RTOS_REPO_PATH=~/git/rtos

alias cds=' cd $GIT_PATH/setup-files'
alias cdg=' cd $GIT_PATH'
alias cdgr='cd $RTOS_REPO_PATH'

#_______________________________________________________________________________
# OTHER SHORTCUTS

alias gs='git status'
alias dsa='exit'

alias la='ls -lah'

set -o vi

#_______________________________________________________________________________
# ARDUINO
export NANO_ESP32=esp32:esp32:nano_nora
export MKR1000=arduino:samd:mkr1000
export ARDUINO_BOARD=$MKR1000
export ARDUINO_BOARD=$NANO_ESP32
export ARDUINO_COMM_PORT=/dev/ttyACM0
export ARDUINO_COMM_PORT=/dev/ttyACM1

alias ac='arduino-cli compile -b $ARDUINO_BOARD'
alias au='arduino-cli upload ./ -p $ARDUINO_COMM_PORT -b $ARDUINO_BOARD'
