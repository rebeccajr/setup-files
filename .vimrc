"_______________________________________________________________________________
" DESCRIPTION
" This file contains the setup commands for vim.
"_______________________________________________________________________________

"_______________________________________________________________________________
" LINE WRAPPING

"text will wrap in window if it goes beyond window width
set wrap

"text will wrap when a word breaks
set linebreak

"_______________________________________________________________________________
" NUMBERING

"shows line numbers
set number

"shows cursor location like row and column number
set ruler

"_______________________________________________________________________________
" WHITESPACE

" expand tabs unless in a makefile
let _curfile = expand("%:t")
if _curfile =~ "Makefile" || _curfile =~ "makefile" || _curfile =~ ".*\.mk"
set noexpandtab
else
set expandtab
set tabstop=4
set shiftwidth=4
endif

"_______________________________________________________________________________
" OTHER SETTINGS

"show syntax coloring
syntax on

highlight LineNr ctermfg=8

set formatoptions+=nrco

"_______________________________________________________________________________
" KEYMAPS

" remap :
nnoremap ;; :

" remap esc key
inoremap jk <esc>
inoremap JK <esc>
nnoremap jk <esc>
nnoremap JK <esc>

" remap save
inoremap fds <esc>:w<cr>
inoremap FDS <esc>:w<cr>
nnoremap fds      :w<cr>
nnoremap FDS      :w<cr>

" remap quit without save
inoremap dsa <esc> :q!
inoremap DSA <esc> :q!
nnoremap dsa       :q!
nnoremap DSA       :q!


"append a line of the next typed character below the current line.
inoremap Q yypv$r

