#!/usr/bin/env python

import os.path
import subprocess

from all_plg_srcs import PLUGINS

_OPER_INSTALL_NEW, _OPER_UPDATE_EXISTING = 0, 1


class _CmdMaker(object):
    """Creates parameters for subprocess.call's
    for fetching/removal of plugins
    """

    _COMMANDS = {
        'git': {
            _OPER_INSTALL_NEW: (
                "%(PARENT_DIR)s", "git clone %(URL)s %(PKGNAME)s", ),
            _OPER_UPDATE_EXISTING: (
                "%(PKG_PATH)s", "git pull origin", )
        },
        'wget': {
            _OPER_INSTALL_NEW: (
                "%(PARENT_DIR)s", "wget %(URL)s -O %(PKGNAME)s", ),
            _OPER_UPDATE_EXISTING: (
                "%(PARENT_DIR)s", "wget %(URL)s -O %(PKGNAME)s", ),
        }
    }

    @classmethod
    def mkDirAndCmd(cls, src_type, oper_id, vim_plugin):
        assert src_type in cls._COMMANDS, (
            "Unknown plygin src_type: '%s'" % src_type)
        opid2ops = cls._COMMANDS[src_type]
        assert oper_id in opid2ops, (
            "Operation %s is not supported for '%s' plugins" % (
                oper_id, src_type))
        cmd_strings = opid2ops[oper_id]
        placeholders = cls._mk_placeholders(vim_plugin)
        cmds = [cls._str2cmds(s, placeholders) for s in cmd_strings]
        assert cmds
        dir_cmds = cmds[0]
        assert len(dir_cmds) == 1, (
            "Invalid working dir %s" % (dir_cmds,))
        wrk_dir = dir_cmds[0]
        return wrk_dir, cmds[1:]

    @staticmethod
    def _mk_placeholders(vim_plugin):
        return {
            "%(URL)s":        vim_plugin.url,
            "%(PARENT_DIR)s": vim_plugin._parent_dir,
            "%(PKG_PATH)s":   vim_plugin._tgt_path,
            "%(PKGNAME)s":    vim_plugin._pkg_name
        }

    @staticmethod
    def _str2cmds(s, placeholders):
        cmds = s.split()
        # substitute placeholders
        return [placeholders.get(c, c) for c in cmds]


class VimPlugin(object):
    def __init__(self, vim_dir, plug_id, **kwargs):
        self.vim_dir = vim_dir
        self.plug_id = plug_id
        self.name = kwargs.pop('name')
        self.src_type = kwargs.pop('src_type')
        self.url = kwargs.pop('URL')
        self.is_dir = kwargs.pop('is_dir')
        self.destination = kwargs.pop('destination')

        self._pkg_name = self._get_pkg_name()
        self._parent_dir = os.path.join(vim_dir, self.destination)
        self._tgt_path = os.path.join(self._parent_dir, self._pkg_name)
        self._prev_installed = os.path.exists(self._tgt_path)

    def update(self):
        if self._prev_installed:
            self._update_existing()
        else:
            self._install_new()

    def _install_new(self):
        self._make_tgt_dir()
        wrk_dir, cmds = _CmdMaker.mkDirAndCmd(
            self.src_type,
            _OPER_INSTALL_NEW,
            self)
        bk_cwd = os.getcwd()
        os.chdir(wrk_dir)
        for cmd in cmds:
            subprocess.call(cmd)
        os.chdir(bk_cwd)

    def _update_existing(self):
        wrk_dir, cmds = _CmdMaker.mkDirAndCmd(
            self.src_type,
            _OPER_UPDATE_EXISTING,
            self)
        bk_cwd = os.getcwd()
        os.chdir(wrk_dir)
        for cmd in cmds:
            subprocess.call(cmd)
        os.chdir(bk_cwd)

    def _get_pkg_name(self):
        pkg_name = os.path.basename(self.url)
        if self.is_dir:
            pkg_name = os.path.splitext(pkg_name)[0]
        return pkg_name

    def _make_tgt_dir(self):
        if not os.path.exists(self._parent_dir):
            os.mkdir(self._parent_dir)
        if not os.path.isdir(self._parent_dir):
            assert False


def main():
    #vim_dir = os.path.expanduser("~/.vim")
    vim_dir = os.path.expanduser(".")
    plugins_list = PLUGINS.keys()  # so far just install all the plugins
    for plugin_id in plugins_list:
        plg = VimPlugin(vim_dir, plugin_id, **PLUGINS[plugin_id])
        print("===== Processing plugin '%s' ..." % (plg.name, ) )
        plg.update()
        print("... done")

if __name__ == '__main__':
    main()
