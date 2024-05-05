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

export GIT_PATH=~/git
export RTOS_REPO_PATH=~/git/rtos

alias cds=' cd $GIT_PATH/setup-files'
alias cdg=' cd $GIT_PATH'
alias cdgr='cd $RTOS_REPO_PATH'
#_______________________________________________________________________________
# OTHER SHORTCUTS

alias gs='git status'
alias dsa='exit'

set -o vi

