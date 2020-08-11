from configparser import ConfigParser, ExtendedInterpolation
import os
import shutil


def get_paths(logs):
    log_path_list = []
    for log_path in logs.values():
        if os.path.exists(log_path):
            log_path_list.append(log_path)
            print('    found %s' % log_path)
        else:
            print('    not found %s' % log_path)
    return log_path_list


def make_backup(logs, backups):
    for log in logs:
        for backup in backups:
            print('    %s' % shutil.copy(log, backup))


if __name__ == '__main__':
    CONFIG = 'hrl_backup.cfg'

    cfg = ConfigParser(interpolation=ExtendedInterpolation())

    try:
        if not os.path.exists(CONFIG):
            raise FileNotFoundError('%s not found!' % CONFIG)
    except FileNotFoundError as err:
        exit(err)

    cfg.read(CONFIG)

    print('Search logs:')
    logs_section = cfg['windows-logs']
    logs_list = get_paths(logs_section)

    print('Search backups:')
    backups_section = cfg['windows-backups']
    backups_list = get_paths(backups_section)

    print('Copied:')
    make_backup(logs_list, backups_list)
