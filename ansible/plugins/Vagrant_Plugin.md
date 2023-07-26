# vagrant custom plugin

## `vagrant.py`

Module takes two parameters: `path`, which is the path to the directory containing the Vagrantfile, and `command` to run  `up`, `halt`, `destroy`.

Use:

```yaml

- name: Start Vagrant
  vagrant:
    path: /path/to/Vagrantfile/
    command: up

- name: Start Vagrant
  vagrant:
    path: /path/to/Vagrantfile/
    command: destroy

- name: Start Vagrant
  vagrant:
    path: /path/to/Vagrantfile/
    command: up

```
.[TODO]
- [ ] need to add a provision key ( vagrant up --provision)
- [ ] need to add package and key for output path

Should be set in the if running the libvirt vagrant packer setup vm playbook;  
However, this assumes that `vagrant` is in PATH...Will not work if that's not


```python
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import subprocess

def run_module():
    # define available arguments/parameters a user can pass to the module
    # need to teststill compound comands [todo]
    module_args = dict(
        path=dict(type='str', required=True),
        command=dict(type='str', required=True),
    )

    # result dict seeed
    result = dict(
        changed=False,
        original_message='',
        message='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the working with  module in only check mode, do not
    # make any changes to the env...just return the current state
    if module.check_mode:
        return result

    try:
        # Vagrant command
        subprocess.check_call(['vagrant', module.params['command']], cwd=module.params['path'])
        result['changed'] = True
        result['message'] = 'Vagrant command ' + module.params['command'] + ' executed successfully'
    except subprocess.CalledProcessError as e:
        module.fail_json(msg='Vagrant command ' + module.params['command'] + ' failed', **result)


    if module.params['command']:
        result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
```  
 ---


[official Ansible documentation](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html) information on how to write a module.