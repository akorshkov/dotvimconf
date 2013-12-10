#!/usr/bin/env python

import sys
import os.path
import subprocess
from optparse import OptionParser

from all_plg_srcs import PLUGINS

_OPER_INSTALL_NEW, _OPER_UPDATE_EXISTING = 0, 1


class _CmdMaker(object):
    """Creates parameters for subprocess.call's
    for fetching/removal of plugins
    """

    _COMMANDS = {
        #        working dir    | the command or commands
        'git': {
            _OPER_INSTALL_NEW: (
                "%(PARENT_DIR)s", "git clone %(SRC)s %(PKGNAME)s", ),
            _OPER_UPDATE_EXISTING: (
                "%(PKG_PATH)s", "git pull origin", )
        },
        'wget': {
            _OPER_INSTALL_NEW: (
                "%(PARENT_DIR)s", "wget %(SRC)s -O %(PKGNAME)s", ),
            _OPER_UPDATE_EXISTING: (
                "%(PARENT_DIR)s", "wget %(SRC)s -O %(PKGNAME)s", ),
        },
        'local': {
            _OPER_INSTALL_NEW: (
                "%(PARENT_DIR)s", "cp -r %(SRC)s %(PKGNAME)s", ),
        },
    }

    @classmethod
    def mk_dir_and_cmds(cls, src_type, oper_id, vim_plugin):
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
        if vim_plugin.src_type == "local":
            src = os.path.join(vim_plugin.vim_dir, vim_plugin.src)
        else:
            src = vim_plugin.src

        return {
            "SRC":        src,
            "PARENT_DIR": vim_plugin.parent_dir,
            "PKG_PATH":   vim_plugin.pkg_path,
            "PKGNAME":    vim_plugin.pkg_name
        }

    @staticmethod
    def _str2cmds(cmd_str, placeholders):
        cmd_chunks = cmd_str.split()
        # substitute placeholders
        return [s % placeholders for s in cmd_chunks]


class VimPlugin(object):
    def __init__(self, vim_dir, plug_id, **kwargs):
        self.vim_dir = vim_dir
        self.plug_id = plug_id
        self.descr = kwargs.pop('descr')
        self.src_type = kwargs.pop('src_type')
        self.src = kwargs.pop('src')
        self.is_dir = kwargs.pop('is_dir', True)
        self.destination = kwargs.pop('destination', "bundle")

        self.pkg_name = self._get_pkg_name()
        self.parent_dir = os.path.join(self.vim_dir, self.destination)
        self.pkg_path = os.path.join(self.parent_dir, self.pkg_name)
        self.prev_installed = os.path.exists(self.pkg_path)

    def update(self, new_only):
        print("===== Processing plugin '%s' ..." % (self.descr, ))
        if self.prev_installed:
            if new_only:
                print("... skip, installed previously.")
            else:
                if self._update_existing():
                    print("... update failed.")
                else:
                    print("... updated successfully.")
        else:
            if self._install_new():
                print("... installation failed.")
            else:
                print("... done.")

    def _install_new(self):
        self._make_tgt_dir()
        wrk_dir, cmds = _CmdMaker.mk_dir_and_cmds(
            self.src_type,
            _OPER_INSTALL_NEW,
            self)
        bk_cwd = os.getcwd()
        os.chdir(wrk_dir)
        exit_status = self._run_commands(cmds)
        os.chdir(bk_cwd)
        return exit_status

    def _update_existing(self):
        wrk_dir, cmds = _CmdMaker.mk_dir_and_cmds(
            self.src_type,
            _OPER_UPDATE_EXISTING,
            self)
        bk_cwd = os.getcwd()
        os.chdir(wrk_dir)
        exit_status = self._run_commands(cmds)
        os.chdir(bk_cwd)
        return exit_status

    @staticmethod
    def _run_commands(cmds):
        for cmd in cmds:
            exit_status = subprocess.call(cmd)
            if exit_status:
                return exit_status
        return 0

    def _get_pkg_name(self):
        pkg_name = os.path.basename(self.src)
        if self.is_dir:
            pkg_name = os.path.splitext(pkg_name)[0]
        return pkg_name

    def _make_tgt_dir(self):
        if not os.path.exists(self.parent_dir):
            os.mkdir(self.parent_dir)
        if not os.path.isdir(self.parent_dir):
            assert False


def mk_new_sel_plugs_file(fname):
    cfg_file = open(fname, "w")
    for plug_id, plug_props in PLUGINS.items():
        cfg_file.write("#%(PLG_ID)-20s # %(PLG_DESCR)s\n" % {
            'PLG_ID': plug_id,
            'PLG_DESCR': plug_props['descr']})
    print("File with a list of awailable plugins created:")
    print(fname)
    print("Uncomment all the plugins you want to install")


def get_selected_plugins_list(vim_dir):
    fname = os.path.join(vim_dir, 'sel_plugs.cfg')
    if not os.path.isfile(fname):
        mk_new_sel_plugs_file(fname)
    plugs_list = [s[:s.find('#')].strip() for s in open(fname)]
    plugs_list = [s for s in plugs_list if s]
    return plugs_list


def process_options():
    parser = OptionParser(usage="usage: %prog [options] [plugin_names]")
    parser.add_option('-l', '--list', dest='print_list', default=False,
                      action='store_true',
                      help="print list of supported/installed plugins")
    parser.add_option('-N', '--new_only', dest='new_only', default=False,
                      action='store_true',
                      help="install new plugins only, do not update existing")

    return parser.parse_args()


def print_plugins_list(vim_dir, sel_plug_ids):
    all_plugins = [VimPlugin(vim_dir, id, **conf) for (id, conf) in PLUGINS.items()]
    for plugin in all_plugins:
        is_selected = plugin.plug_id in sel_plug_ids
        fmt = "%(ID)15s %(SELECTED)12s %(INSTALLED)-12s %(DESCR)s"
        statedescr = fmt % {
            'ID': plugin.plug_id,
            'SELECTED': "selected" if is_selected else "",
            'INSTALLED': "installed" if plugin.prev_installed else "",
            'DESCR': plugin.descr }
        print(statedescr)
    for plug_id in sel_plug_ids:
        if plug_id not in PLUGINS:
            print("WARNING: Unknown plugin '%s' is selected" % (plug_id,))


def check_args_plugins_selected(plug_ids, sel_plug_ids):
    for plug_id in plug_ids:
        if plug_id not in sel_plug_ids:
            print("Plugin '%s' is not selected. Include it into '~/.vim/sel_plugs.cfg' file")
            sys.exit(1)


def main():
    options, args = process_options()

    vim_dir = os.path.abspath(os.path.expanduser("~/.vim"))
    sel_plug_ids = get_selected_plugins_list(vim_dir)

    if options.print_list:
        print_plugins_list(vim_dir, sel_plug_ids)
        return

    if args:
        check_args_plugins_selected(args, sel_plug_ids)

    plugs_to_process = args or sel_plug_ids

    if plugs_to_process:
        for plugin_id in plugs_to_process:
            plg = VimPlugin(vim_dir, plugin_id, **PLUGINS[plugin_id])
            plg.update(options.new_only)
    else:
        print("Warning: No plugins selected.")

if __name__ == '__main__':
    main()
