#!/usr/bin/env python

import json
import argparse

def get_inventory_data():
    return {
        "centos": {
            "hosts": ["target1"],
            "vars": {
                "ansible_user": "ebi",
                "ansible_ssh_pass": "Password1",
                "ansible_become_pass": "Password1",
                "ansible_host": "192.168.56.101"
            }
        }
    }


def read_cli_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    args = parser.parse_args()


if __name__ == "__main__":
    global args
    read_cli_args()
    inventory_data = get_inventory_data()

    print(json.dumps(inventory_data))

    # if args and args.list:
    #     print(json.dumps(inventory_data))
    # elif args.host:
    #     print(json.dumps(inventory_data))
