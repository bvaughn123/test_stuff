from ansible.module_utils.basic import AnsibleModule
import subprocess

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        command=dict(type='str', required=True),
        provision=dict(type='boolean', required=False)
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
        return result

    try:
        if module.params['command'] == 'package':
            if module.params['output_box_name']:
                subprocess.check_call(['vagrant ', module.params['command'], '--output', module.params['output_box_name']], cwd=module.params['path'])
            else:
                module.fail_json(msg='output_box_name is required for package command', **result)
        result['changed'] = True
        result['message'] = 'Vagrant' + module.params['command'] + ' executed successfully'
    except subprocess.CalledProcessError as e:
        module.fail_json(msg='Vagrant ' + module.params['command'] + ' failed', **result)

        if module.params['provision] == 'true':
            if module.params['output_box_name']:
                subprocess.check_call(['vagrant ', module.params['command'], '--provision'])
            else:
                module.fail_json(msg='Should be ran with up command', **result)
        result['changed'] = True
        result['message'] = 'Vagrant' + module.params['command'] + ' executed successfully'
    except subprocess.CalledProcessError as e:
        module.fail_json(msg='Vagrant ' + module.params['command'] + ' failed', **result)


    if module.params['command']:
        result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()