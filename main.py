#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from register import Register

if __name__ == '__main__':
    args = argparse.ArgumentParser(description='Main')

    group = args.add_mutually_exclusive_group(required=True)
    group.add_argument('--register', nargs=1, help='Register a new user')

    if args.parse_args().register:
        file_name = args.parse_args().register[0]
        register = Register(file_name)
        register.new_user()
