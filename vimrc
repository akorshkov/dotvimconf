" akorshkov's vimrc file.
" Author: akorshkov at parallels.com

" ==== No need compatibility with vi  ===========
set nocompatible

" ==== Use pathogen to manage plugins  ==========
call pathogen#runtime_append_all_bundles()
call pathogen#helptags()

" ==== colorscheme  =============================
colorscheme peachpuff

" ==== mapleaders  ==============================
let mapleader=","
let maplocalleader="\\"

" ==== Status Line ==============================
set statusline=
set statusline+=%-2.2n\                       " buffer number
set statusline+=%f\                           " file name
set statusline+=%h%m%r%w                      " status flag
set statusline+=\[%{strlen(&ft)?&ft:'none'}]  " file type
set statusline+=%=                            " right align remainder
set statusline+=0x%-8B                        " character value
set statusline+=%-10(%l,%c%V%)                " line character
set statusline+=%<%P                          " file position

set laststatus=2    " always display statusline

" ==== misc options  ============================
set wildmode=longest,list,full      " affects filemnames autocompletion
set wildmenu                        " affects commands autocompletion

set splitbelow                      " affect split
set splitright                      " and vsplit commands

" ==== hotkeys for quick-fix window =============
nnoremap <F8> :cnext<CR>
nnoremap <s-F8> :cprev<CR>
nnoremap <F7> :cnfile<CR>
nnoremap <s-F7> :cpfile<CR>
nnoremap <F6> :copen<CR>
nnoremap <s-F6> :cclose<CR>

" ==== my favorite hotkeys ======================
" use space to replace a single character
nnoremap <Space> i_<Esc>r
" Q runs my 'hot' macro 'q'
nnoremap Q @q

" ==== autocommands =============================
" au BufNewFile,BufRead *.flex set filetype=lex
autocmd BufNewFile,BufReadPost *.py set expandtab shiftwidth=4 tabstop=4 softtabstop=4
autocmd BufNewFile,BufReadPost *.c,*.-c,*.h,*.cpp,*.hpp set autoindent cindent expandtab shiftwidth=2 smartindent smarttab wrapmargin=1
