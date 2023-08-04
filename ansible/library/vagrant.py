#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import subprocess
import shutil
import os

def init(command, path, output_box_name=None):
    try:
        
        vagrant_bin = shutil.which('vagrant')
        if not vagrant_bin:
            raise FileNotFoundError("Vagrant binary not found on the system.")

        full_command = [vagrant_bin, command]
        if command == 'package' and output_box_name:
            full_command.extend(['--output', output_box_name])

        subprocess.check_call(full_command, cwd=path)
        return True
    except subprocess.CalledProcessError as e:
        return False


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        command=dict(type='str', required=True),
        provision=dict(type='boolean', required=False),
        output_box_name=dict(type='str', required=False),
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        os.environ["VAGRANT_LOG"] = "info"
        if not shutil.which('vagrant'):
            module.fail_json(msg='Vagrant isnt found', **result)

        if module.params['command'] == 'package':
            if not module.params['output_box_name']:
                module.fail_json(msg='output_box_name is required for package command.', **result)

        if init(module.params['command'], module.params['path'], module.params['output_box_name']):
            result['changed'] = True
            result['message'] = 'Vagrant {} executed successfully'.format(module.params['command'])
        else:
            module.fail_json(msg='Vagrant {} failed'.format(module.params['command']), **result)

    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
