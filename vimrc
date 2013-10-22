call pathogen#runtime_append_all_bundles()
call pathogen#helptags()

let mapleader=","
let maplocalleader="\\"

colorscheme peachpuff

au BufNewFile,BufRead *.flex set filetype=lex

set cin
set sw=4
set tabstop=4
set expandtab

" Status Line
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

" autocomplete filenames in command line
set wildmode=longest,list,full

" use space to replace a single character
nnoremap <Space> i_<Esc>r

" Q runs my 'hot' macro 'q'
nnoremap Q @q

" hotkeys for quick-fix window
nnoremap <F8> :cnext<CR>
nnoremap <s-F8> :cprev<CR>
nnoremap <F7> :cnfile<CR>
nnoremap <s-F7> :cpfile<CR>
nnoremap <F6> :copen<CR>
nnoremap <s-F6> :cclose<CR>
