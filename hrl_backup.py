from configparser import ConfigParser, ExtendedInterpolation
import os
import shutil
import platform


class HrlBackup:

    def __init__(self, config, log_section='logs', backup_section='backups'):
        self.config = config
        self.log_section = log_section
        self.backup_section = backup_section

        self.cfg = self._cfg_read()

        self.os_name = platform.system().lower()

    def _cfg_read(self) -> ConfigParser:
        try:
            if not os.path.exists(self.config):
                raise FileNotFoundError('%s not found!' % self.config)
        except FileNotFoundError as err:
            exit(err)

        cfg = ConfigParser(interpolation=ExtendedInterpolation())
        cfg.read(self.config)

        return cfg

    def _get_section(self, name: str):
        return self.cfg[self.os_name + '-' + name]

    def _get_paths(self, section) -> list:
        path_list = []
        for path in section.values():
            if os.path.exists(path):
                path_list.append(path)
                print('    found %s' % path)
            else:
                print('    not found %s' % path)
        return path_list

    def backup(self) -> None:
        print('Search logs:')
        logs = self._get_paths(hrl._get_section(self.log_section))

        print('\n\r', 'Search backups:')
        backups = self._get_paths(hrl._get_section(self.backup_section))

        print('\n\r','Copied:')
        for log in logs:
            for backup in backups:
                print('    %s' % shutil.copy(log, backup))


if __name__ == '__main__':

    hrl = HrlBackup('hrl_backup.cfg', 'logs', 'backups')
    hrl.backup()
