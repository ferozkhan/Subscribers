# -*- encoding: utf-8 -*-

from ConfigParser import SafeConfigParser


def parse_config(config_file, section='mongo'):
    parser = SafeConfigParser()
    parser.read(config_file)
    return dict(parser._sections.get(section))

