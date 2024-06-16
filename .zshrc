#_______________________________________________________________
# This file defines configuration for zsh
#_______________________________________________________________

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
zstyle :compinstall filename '/home/flux/.zshrc'

#_______________________________________________________________
# THIS DOESN'T WORK
#_______________________________________________________________
# Function to get Git branch name
#_______________________________________________________________
# git_prompt_info() {
#     # Check if we are in a Git repository
#     if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
#         # Get the current branch name
#         local branch=$(git symbolic-ref --short HEAD 2>/dev/null)
#         if [ -n "$branch" ]; then
#             echo " ($branch)"
#         else
#             echo ""
#         fi
#     fi
# }
#_______________________________________________________________


#_______________________________________________________________
# Define prompt
#---------------------------------------------------------------
# %n          : Username of the current user.
# %m          : Hostname up to the first '.'.
# %~          : Current working directory
# $(git_prompt_info):
#---------------------------------------------------------------
# %D{format}  : Current date and time formatted according to format.
#               format ex: %D{%H:%M:%S}
#---------------------------------------------------------------
# Note: the git_prompt_info function is not working
# PS1='🐰 ⏲ %D{%H:%M} [%~] $(git_prompt_info)> '
#---------------------------------------------------------------
PS1='🐰 ⏲ %D{%H:%M} [%~] > '
#_______________________________________________________________

#_______________________________________________________________
# Enable menu selection in tab complete
#---------------------------------------------------------------
autoload -Uz compinit
compinit

# Enable menu selection
zstyle ':completion:*' menu select

#_______________________________________________________________
# Define a list-colors style for file completions
#---------------------------------------------------------------
# di: Directories                      
# fi: Regular files                    
# ln: Symbolic links                   
# pi: Named pipes                      
# so: Sockets                          
# bd: Block devices                    
# cd: Character devices                
# or: Orphaned symbolic links          
# mi: Missing files                    
# ex: Executable files                 
# mh: Multi-hard links                 
# su: Setuid files                     
# sg: Setgid files                     
# tw: Sticky directories               
# ow: Other writable files             
# st: Sticky and other writable files  
#_______________________________________________________________
# ANSI COLORS
#---------------------------------------------------------------
# Note: The ANSI colors are defined in the terminal profile.
#---------------------------------------------------------------
# Index   Color         Index   Color
#---------------------------------------------------------------
# 30      Black         90      Bright Black          
# 31      Red           91      Bright Red            
# 32      Green         92      Bright Green          
# 33      Yellow        93      Bright Yellow         
# 34      Blue          94      Bright Blue           
# 35      Magenta       95      Bright Magenta        
# 36      Cyan          96      Bright Cyan           
# 37      White         97      Bright White          
#
# 00      No color (default)
#---------------------------------------------------------------
# BACKGROUND COLORS
#---------------------------------------------------------------
# Index   Color
#---------------------------------------------------------------
# 40      Black   background
# 41      Red     background
# 42      Green   background
# 43      Yellow  background
# 44      Blue    background
# 45      Magenta background
# 46      Cyan    background
# 47      White   background
#---------------------------------------------------------------
zstyle ':completion:*:default' list-colors "di=32"  # Directories                      
zstyle ':completion:*:default' list-colors "fi=32"  # Regular files                    
zstyle ':completion:*:default' list-colors "ln=36"  # Symbolic links                   
zstyle ':completion:*:default' list-colors "pi=33"  # Named pipes                      
zstyle ':completion:*:default' list-colors "so=35"  # Sockets                          
zstyle ':completion:*:default' list-colors "bd=33"  # Block devices                    
zstyle ':completion:*:default' list-colors "cd=31"  # Character devices                
zstyle ':completion:*:default' list-colors "or=31"  # Orphaned symbolic links          
zstyle ':completion:*:default' list-colors "mi=00"  # Missing files                    
zstyle ':completion:*:default' list-colors "ex=32"  # Executable files                 
zstyle ':completion:*:default' list-colors "mh=00"  # Multi-hard links                 
zstyle ':completion:*:default' list-colors "su=37"  # Setuid files                     
zstyle ':completion:*:default' list-colors "sg=37"  # Setgid files                     
zstyle ':completion:*:default' list-colors "tw=37"  # Sticky directories               
zstyle ':completion:*:default' list-colors "ow=37"  # Other writable files             
zstyle ':completion:*:default' list-colors "st=37"  # Sticky and other writable files  
#_______________________________________________________________



 source ~/.bash_profile
