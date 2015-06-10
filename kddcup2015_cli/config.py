# -*- coding: utf-8 -*-
from cliff.command import Command
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import os


class Config(Command):
    'Set config.'

    def get_parser(self, prog_name):
        parser = super(Config, self).get_parser(prog_name)

        parser.add_argument('-u', '--username', help='username(email)')
        parser.add_argument('-p', '--password', help='password')

        return parser

    def take_action(self, parsed_args):
        config_dir = '~/.kddcup2015-cli'
        config_dir = os.path.expanduser(config_dir)

        if not os.path.isdir(config_dir):
            os.mkdir(config_dir)

        config = ConfigParser.ConfigParser(allow_no_value=True)

        if os.path.isfile(config_dir + '/config'):
            config.readfp(open(config_dir + '/config'))

        if not config.has_section('user'):
            config.add_section('user')

        if parsed_args.username:
            username = parsed_args.username
            config.set('user', 'username', username)

        if parsed_args.password:
            password = parsed_args.password
            config.set('user', 'password', password)

        config.write(open(config_dir + '/config', 'w'))
