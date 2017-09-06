#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zero控制台主程序

from __future__ import print_function       # python兼容性

import getopt                               # 命令行参数处理模块
import sys
import os
import base64

zero_man = """
Usage:
    ./zero_console -h
    ./zero_console -t
    ./zero_console [-s <script_file>]

Options:
    
    -h or --help
        显示帮助信息

    -s <script_file> or --script=<script_file>
        运行指定检测脚本

    -p <profile> or --profile=<profile>
        运行同指定的配置文件

    -v or --version
        显示版本信息

For more info use 'man zero'
"""
def _config_output_manager():
    """
    :return:
    """
    try:
        om.manager.set

def _usage():
    print (zero_man)


def _generate_run_commands(script_file, profile):
    """
    Given the user configuration, generate the commands to run in the console
    user interface at startup.

    :param script_file: The script (-s) file name
    :param profile: The profile (-p) name
    """
    commands_to_run = []

    if script_file is not None:
        try:
            fd = open(script_file)
        except IOError:
            print('Failed to open script file: "%s"' % script_file)
            sys.exit(2)
        else:
            for line in fd:
                line = line.strip()
                # if not a comment..
                if line != '' and line[0] != '#':
                    commands_to_run.append(line)
            fd.close()
    elif profile is not None:

        current_dir = os.getcwd()
        commands_to_run = ["profiles use %s %s" % (profile, current_dir)]

        if force_profile is not None:
            commands_to_run.append("start")
            commands_to_run.append("exit")

    return commands_to_run

def main():
    try:
        long_options = ['script=', 'help', 'version', 'profile=']
        opts, _ = getopt.getopt(sys.argv[1:], "ehvs:nfp:P:", long_options)

    except getopt.GetoptError:
        _usage()
        return -3

    script_file = None
    profile = None

    for o, a in opts:
        if o in ('-s', '--script'):
            script_file = a
        if o in ('-p', '--profile'):
            profile = a
        if o in ('-h', '--help'):
            _usage()
            return 0
        if o in ('-v', '--version'):
            print (get_zero_version())
            return 0

    commands_to_run = _generate_run_commands(script_file, profile)
    console = ConsoleUI(commands=commands_to_run)

    if not console.accept_disclaimer():
        return -4
    return console.sh()

def _main():
    _config_output_manager()
    sys.exit(main())

def if __name__ == '__main__':
    _main()
