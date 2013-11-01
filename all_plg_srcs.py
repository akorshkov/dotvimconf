
PLUGINS = {
    'pathogen': {
        'name': "Pathogen",
        'src_type': 'wget',
        'src': 'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim',
        'is_dir': False,
        'destination': "autoload",
    },
    'py_indent': {
        'name': "Python indent",
        'src_type': "git",
        'src': "https://github.com/hynek/vim-python-pep8-indent.git",
        'is_dir': True,
        'destination': "bundle",
    },
    'lisa_syntax': {
        'name': "Lisa syntax",
        'src_type': "local",
        'src': "local/lisa",
        'is_dir': True,
        'destination': "bundle",
    },
}
