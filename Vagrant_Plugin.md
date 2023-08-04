# vagrant custom plugin

## `vagrant.py`


Module takes two required parameters: `path` and `command`

Options for Command are any vagrant commands that do not require options, such as `up`, `halt`, and `destroy`.
Additionally, `provision` is a valid command, for the equivalent `vagrant up --provision` CLI command.

The command `package` will require the `output_box_name: name_of_box.box` (see below examples).

- [ ] Review [Molecule-Vagrant](https://github.com/ansible-community/molecule-vagrant/blob/main/molecule_vagrant/modules/vagrant.py)

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
- [x] need to add package and key for output path

Should be set in the if running the libvirt vagrant packer setup vm playbook;  
However, this assumes that `vagrant` is in PATH...Will not work if that's not


```python
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import subprocess

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        command=dict(type='str', required=True),
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
                subprocess.check_call(['vagrant', module.params['command'], '--output', module.params['output_box_name']], cwd=module.params['path'])
            else:
                module.fail_json(msg='output_box_name is required for package command', **result)
        else:
           if module.params['command'] == 'provision':
                subprocess.check_call(['vagrant', module.params['command'], 'up --provision', cwd=module.params['path'])
        else:
            subprocess.check_call(['vagrant', module.params['command']], cwd=module.params['path'])
        result['changed'] = True
        result['message'] = 'Vagrant command ' + module.params['command'] + ' executed successfully'
    except subprocess.CalledProcessError as e:
        module.fail_json(msg='Vagrant command ' + module.params['command'] + ' failed', **result)
    if module.params['command']:
        result['changed'] = True

def main():
    run_module()

if __name__ == '__main__':
    main()
```

Ansible Module Vagrant usage:

```yaml

- name: Vagrant Up
  vagrant:
    path: /path/to/your/vagrantfile/
    command: up

- name: Vagrant Provision
  vagrant:
    path: /path/to/your/vagrantfile/
    command: provision

- name: Package Vagrant
  vagrant:
    path: /path/to/your/vagrantfile/
    command: halt

- name: Package Vagrant
  vagrant:
    path: /path/to/your/vagrantfile/
    command: package
    output_box_name: boxname.box

- name: Destroy Vagrant
  vagrant:
    path: /path/to/your/vagrantfile/
    command: destroy

```

[official Ansible documentation](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html) information on how to write a module.