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
        os.environ["VAGRANT_LOG"] = "1"
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