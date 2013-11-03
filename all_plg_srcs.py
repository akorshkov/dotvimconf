
PLUGINS = {
    'pathogen': {
        'name': "Pathogen",
        'src_type': 'wget',
        'src': 'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim',
        'is_dir': False,
        'destination': "autoload",
    },
    'py_indent': {
        'name': "Python indent vim-python-pep8-indent",
        'src_type': "git",
        'src': "https://github.com/hynek/vim-python-pep8-indent.git",
    },
    'syntastic': {
        'name': "Syntax checker for many languages",
        'src_type': "git",
        'src': "git://github.com/scrooloose/syntastic.git",
    },
    'lisa_syntax': {
        'name': "Lisa syntax",
        'src_type': "git",
        'src': "https://github.com/akorshkov/lsa.git",
    },
    'vcscommand': {
        'name': "vim - SVN integration",
        'src_type': "git",
        'src': "https://github.com/vim-scripts/vcscommand.vim",
    },
    'pba_cxx': {
        'name': "Syntax highlitning for common pba constructs (cpp)",
        'src_type': "local",
        'src': "local_distr/pba_cxx",
    },
    'pbtst_py': {
        'name': "Syntax highlitning for common pbtst constructs (python)",
        'src_type': "local",
        'src': "local_distr/pbtst_py",
    },
    'bmlog': {
        'name': "Syntax highlitning for pba logs",
        'src_type': "local",
        'src': "local_distr/bmlog",
    },
}
