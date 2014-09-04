" akorshkov's vimrc file.
"
" Author: akorshkov at parallels.com

" ==== No need compatibility with vi  ===========
set nocompatible

" ==== Use pathogen to manage plugins  ==========
call pathogen#infect()
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

if exists('*SyntasticStatuslineFlag')
	set statusline+=%#ToDo#                         " next line is read warn ...
	set statusline+=%{SyntasticStatuslineFlag()}    " msg from syntastic plugin
	set statusline+=%*                              " ... end of read warn
endif

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
nnoremap <F5> :lopen<CR>
nnoremap <s-F5> :lclose<CR>
nnoremap <F6> :copen<CR>
nnoremap <s-F6> :cclose<CR>
nnoremap <F7> :lnext<CR>
nnoremap <s-F7> :lprev<CR>
nnoremap <F8> :cnext<CR>
nnoremap <s-F8> :cprev<CR>

" ==== my favorite hotkeys ======================
" use space to replace a single character
nnoremap <Space> i_<Esc>r
" Q runs my 'hot' macro 'q'
nnoremap Q @q

" ==== autocommands =============================
"
" tabstop        - how tab looks
" softtabstop    - how tab counts when I push tab
" shiftwidth     - num spaces used for auto indents
" expandtab
"
" au BufNewFile,BufRead *.flex set filetype=lex
autocmd BufNewFile,BufReadPost *.py
	\ setlocal expandtab shiftwidth=4 softtabstop=4
autocmd BufNewFile,BufReadPost *.c,*.cc,*.h,*.cpp,*.hpp
	\ setlocal autoindent cindent expandtab shiftwidth=2 softtabstop=2 smartindent smarttab wrapmargin=1
autocmd BufNewFile,BufReadPost *.vim,vimrc,.vimrc
	\ setlocal shiftwidth=4 softtabstop=4 tabstop=4
autocmd FileType vim setlocal iskeyword=@,48-57,_,192-255
autocmd FileType lsa setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2
autocmd FileType xml setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2
autocmd BufNewFile,BufReadPost *.pl setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2

filetype indent plugin on

" ==== syntastic plugin configuraton ============
let g:syntastic_enable_signs=0          " signs on the left side of window
let g:syntastic_check_on_wq=0
let g:syntastic_aggregate_errors=1
let g:syntastic_echo_current_error=0    " do not display msgs in command line
let g:syntastic_mode_map = { 'mode': 'passive',
                           \ 'active_filetypes': [],
                           \ 'passive_filetypes': [] }
let g:syntastic_always_populate_loc_list=1
let g:syntastic_auto_loc_list=1         " auto open/close the loc list (0/1/2)

let g:syntastic_python_checkers = ['flake8', 'pylint']

" hotkey to perform the syntax check
nnoremap <leader>s :w<CR>:SyntasticCheck<CR>
" toggle active/passive mode
nnoremap <leader>S :SyntasticToggleMode<CR>
