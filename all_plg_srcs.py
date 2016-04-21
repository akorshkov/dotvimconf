
PLUGINS = {
    'pathogen': {
        'descr': "Pathogen",
        'src_type': 'wget',
        'src': 'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim',
        'is_dir': False,
        'destination': "autoload",
    },
    'py_indent': {
        'descr': "Python indent vim-python-pep8-indent",
        'src_type': "git",
        'src': "https://github.com/hynek/vim-python-pep8-indent.git",
    },
    'syntastic': {
        'descr': "Syntax checker for many languages",
        'src_type': "git",
        'src': "git://github.com/scrooloose/syntastic.git",
    },
    'lisa_syntax': {
        'descr': "Lisa syntax",
        'src_type': "git",
        'src': "https://github.com/akorshkov/lsa.git",
    },
    'vcscommand': {
        'descr': "vim - SVN integration",
        'src_type': "git",
        'src': "https://github.com/vim-scripts/vcscommand.vim",
    },
    'pba_cxx': {
        'descr': "Syntax highlitning for common pba constructs (cpp)",
        'src_type': "local",
        'src': "local_distr/pba_cxx",
    },
    'pbtst_py': {
        'descr': "Syntax highlitning for common pbtst constructs (python)",
        'src_type': "local",
        'src': "local_distr/pbtst_py",
    },
    'bmlog': {
        'descr': "Highliting and movements in pba log files",
        'src_type': "git",
        'src': "https://github.com/akorshkov/bmlog.git",
    },
    'textile': {
        'descr': "textile ft-plugin",
        'src_type': "git",
        'src': "https://github.com/timcharper/textile.vim",
    },
    'vimwiki': {
        'descr': "A Personal Wiki",
        'src_type': "git",
        'src': "https://github.com/vim-scripts/vimwiki",
    },
    'vimjson': {
        'descr': "vim - JSON syntax and formatter",
        'src_type': "git",
        'src': "https://github.com/elzr/vim-json",
    },
    'fugitive': {
        'descr': "Integration with git",
        'src_type': "git",
        'src': "https://github.com/tpope/vim-fugitive",
    },
}
