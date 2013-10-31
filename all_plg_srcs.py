
PLUGINS = {
    'pathogen': {
        'name': "Pathogen",
        'src_type': 'wget',
        'URL': 'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim',
        'is_dir': False,
        'destination': "autoload",
    },
    'py_indent': {
        'name': "Python indent",
        'src_type': "git",
        'URL': "https://github.com/hynek/vim-python-pep8-indent.git",
        'is_dir': True,
        'destination': "bundle",
    }
}
