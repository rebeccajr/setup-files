#_______________________________________________________________________________
# .bash_profile
# 
# This file contains aliases and environment variables.
#_______________________________________________________________________________

alias src='source ~/.bash_profile'

#_______________________________________________________________________________
# ARDUINO
export MKR1000=arduino:samd:mkr1000

export NANO_ESP32=esp32:esp32:nano32
export NANO_ESP32=esp32:esp32:esp32c3
export NANO_ESP32=esp32:esp32:lolin_c3_mini
export NANO_ESP32=esp32:esp32:nano_nora
export NANO_ESP32=arduino:esp32:nano_nora

export ARDUINO_BOARD=$NANO_ESP32
export ARDUINO_BOARD=$MKR1000

export ARDUINO_COMM_PORT=/dev/ttyACM0
export ARDUINO_COMM_PORT=/dev/ttyACM2
export ARDUINO_COMM_PORT=/dev/ttyACM1

alias ac='arduino-cli compile -b $ARDUINO_BOARD'
alias au='arduino-cli upload ./ -p $ARDUINO_COMM_PORT -b $ARDUINO_BOARD'


export ESP_PATH=~/.arduino15/packages/arduino/hardware/esp32/2.0.13/
alias cde='cd $ESP_PATH'


#_______________________________________________________________________________
# PATH
export PATH=~/local/bin:$PATH

#_______________________________________________________________________________
# EDIT SETTINGS

alias vimb='vim ~/.bash_profile; src'
alias vimv='vim ~/.vimrc'
alias vimt='vim ~/.tmux.conf'
alias vimz='vim ~/.zshrc'


#_______________________________________________________________________________
# NAVIGATION

export GIT_PATH=~/git
export RTOS_REPO_PATH=~/git/rtos
export COLOR_CLOCK_PATH=$GIT_PATH/color-clock
export CRNT_WORK=$COLOR_CLOCK_PATH/sw/arduino/examples/rtc-time-display-example
export CRNT_WORK=$COLOR_CLOCK_PATH/sw/arduino/examples/simple

alias cdc=' cd $CRNT_WORK'
alias cds=' cd $GIT_PATH/setup-files'
alias cdg=' cd $GIT_PATH'
alias cdgr='cd $RTOS_REPO_PATH'

#_______________________________________________________________________________
# GIT

alias gs='  git status'
alias glo=' git log --oneline'

#_______________________________________________________________________________
# OTHER SHORTCUTS

alias dsa='exit'
set -o vi

#_______________________________________________________________________________
alias save='export TEMP_DIR=$PWD'
alias return=' cd $TEMP_DIR'

alias la='ls -lah'
