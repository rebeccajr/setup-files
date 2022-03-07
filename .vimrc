"-------------------------------------------------------------------------------
" DESCRIPTION
" This file contains the setup commands for vim.
"
"
"
"-------------------------------------------------------------------------------

"show syntax coloring
syntax on

"text will wrap in window if it goes beyond window width
set wrap

"text will wrap when a word breaks
set linebreak

"shows line numbers
set number

"shows cursor location like row and column number
set ruler

highlight LineNr ctermfg=8

:set formatoptions+=nrco

" expand tabs unless in a makefile
let _curfile = expand("%:t")
if _curfile =~ "Makefile" || _curfile =~ "makefile" || _curfile =~ ".*\.mk"
set noexpandtab
else
set expandtab
set tabstop=4
set shiftwidth=4
endif

"append a line of the next typed character below the current line.
:map Q yypv$r
