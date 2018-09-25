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

" ==== tags files  ==============================
" comma-separated options:
" - .tags in the same dir as current file
" - .tags in current dir and up to $HOME
set tags=./.tags,.tags;$HOME

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

set virtualedit=block               " in visual mode cursor goes beyond $

set hlsearch                        " highlight search matches

" ==== hotkeys for quick-fix window =============
if &term == "xterm"
	" for <shift-Fx> to work inside putty
	" http://vim.wikia.com/wiki/Mapping_fast_keycodes_in_terminal_Vim
	set<s-F5>=[28~
	set<s-F6>=[29~
	set<s-F7>=[31~
	set<s-F8>=[32~
endif

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
autocmd FileType ruby setlocal expandtab shiftwidth=2 softtabstop=2 tabstop=8
autocmd FileType vim setlocal iskeyword=@,48-57,_,192-255
autocmd FileType java setlocal shiftwidth=4 softtabstop=4 tabstop=4 noexpandtab
autocmd FileType go setlocal shiftwidth=4 softtabstop=4 tabstop=4 noexpandtab
autocmd FileType lsa setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2
autocmd FileType xml setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2
autocmd FileType html setlocal autoindent nosmartindent expandtab shiftwidth=2 softtabstop=2
autocmd FileType vimwiki setlocal shiftwidth=4 softtabstop=4 tabstop=4
autocmd BufNewFile,BufReadPost *.pl setlocal autoindent smartindent expandtab shiftwidth=2 softtabstop=2

filetype indent plugin on

" ==== helpers for manual shiftwidth modifications
function! ConfTabsWidths(if_expand, tab_width)
	" set consistent values for various shift-width-related options
	if a:if_expand
		setlocal expandtab
	else
		setlocal noexpandtab
	endif
	let &l:shiftwidth = a:tab_width
	let &l:softtabstop = a:tab_width
	let &l:tabstop = a:if_expand ? 8 : a:tab_width
endfunction

" commands to use in vim cmd line. Like `:Ss4`
command Ss2 call ConfTabsWidths(1, 2)  " pba cc code
command Ss4 call ConfTabsWidths(1, 4)  " standard python
command St2 call ConfTabsWidths(0, 2)  " stellart cc code
command St4 call ConfTabsWidths(0, 4)  " pem python
command St8 call ConfTabsWidths(0, 8)  " standard tab

" ==== python-syntax plugin configuraton ========
if !empty(glob("~/.vim/bundle/python-syntax"))
	let g:python_highlight_string_format=1
	let g:python_highlight_file_headers_as_comments=1
	let g:python_highlight_string_formatting=1
endif

" ==== syntastic plugin configuraton ============
if !empty(glob("~/.vim/bundle/syntastic"))
	let g:syntastic_enable_signs=0          " signs on the left side of window
	let g:syntastic_check_on_wq=0
	let g:syntastic_aggregate_errors=1      " run all checkers
	let g:syntastic_echo_current_error=0    " do not display msgs in command line
	let g:syntastic_mode_map = { 'mode': 'passive',
							   \ 'active_filetypes': [],
							   \ 'passive_filetypes': [] }
	let g:syntastic_always_populate_loc_list=1
	let g:syntastic_auto_loc_list=1         " auto open/close the loc list (0/1/2)

	let g:syntastic_python_python_exec = 'python'
	let g:syntastic_python_checkers = ['flake8', 'pylint']
endif

" ==== vim-json plugin configuraton =============
let g:vim_json_syntax_conceal = 0

" ==== ropevim plugin configuraton ==============
if !empty(glob("~/.vim/bundle/ropevim"))
	let g:ropevim_guess_project=1
	autocmd BufNewFile,BufReadPost *.py nnoremap <buffer> g] :RopeGotoDefinition<CR>
	autocmd BufNewFile,BufReadPost *.py nnoremap <buffer> g[ :RopeFindOccurrences<CR>
	autocmd BufNewFile,BufReadPost *.py nnoremap <buffer> gc :RopeShowDoc<CR>
endif

" hotkey to perform the syntax check
nnoremap <leader>s :w<CR>:SyntasticCheck<CR>
" toggle active/passive mode
nnoremap <leader>S :SyntasticToggleMode<CR>

" ==== finding syntax group of current word =====
" Usage:
" :call SynStack()

function! SynStack()
	" Display syntax group information for a character under coursor.
	" Fisrst display 'synstack' ...
	if !exists("*synstack")
		return
	endif
	echon map(synstack(line('.'), col('.')), 'synIDattr(v:val, "name")')
	" ... and now display 'translated syntax group'
	let l:s = synID(line('.'), col('.'), 1)
	echon ' -> ' . synIDattr(synIDtrans(l:s), 'name')
endfunction

" syntax-related hotkeys
" - info about current word:
nnoremap <s-F12> :call SynStack()<CR>
" - fix syntax for current buffer:
nnoremap <F12> :syntax sync fromstart<CR>
