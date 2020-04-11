#!/usr/bin/env python

try:
    import json
except ImportError:
    import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

DOCUMENTATION = '''
---
module: custome_debug
xxxxxxx

'''


EXAMPES = '''
#Example
custome_debug:
    msg: This is a message.
'''

def main():
    module = AnsibleModule(
        argument_spec = dict(
            msg=dict(required=True, type='str')
        )
    )

    msg = module.params['msg']

    if True: 
        module.exit_json(changed=True, msg='%s - %s' % (time.strftime("%c"), msg))
    else:
        module.fail_json(msg="Error message")

if __name__ == '__main__':
    main()