# Test Stuff

Thoughts:

1. **Make the Setup VM**  
   - Part of the libvirt_packer_ansible playbook  
   [Pakr Vagr Libvirt](https://github.com/bvaughn123/Libvirt-Vagrant-Packer)  
   
2. **Create a testing workflow**
   - Part of the libvirt_packer_ansible playbook  
   [Pakr Vagr Libvirt](https://github.com/bvaughn123/Libvirt-Vagrant-Packer)  
     
3. **Packer Build w/ vagrant post provision**  

4. **Create Dynamic vagrantfile*** for use with vagrant box   

5. **Build Nested vm using libvirt and vagrant box**  


## Packer build

Packer Build w/ post vagrant provisioner to build box 

- [ ] Need to create a task to launch the packer build of the base vm.  
    - [todo] Need to come up with logic for choosing the pkr.hcl file...

- [ ] Need to ensure task for vagrant install libvirt plugin is done
     - Custom Plugin [todo] **inprogress** 
     [Custom Plugin Readme](ansible/plugins/Vagrant_Plugin.md)

## Dynamic Vagrantfile

Re-use and "agnosticize" a template vagrant file.

- [ ] Create a j2 template to generate vars for the vagrantfile
    > config.yaml  

- [ ] Create a Provision and Deploy variable in template  

    - Provision variable would be for utilization by packers post provision vagrant plugin
    > This would create the intial box to be reutilized by the proceeding vagrant builds

    - Deploy key would dictate the config.vm.box = "$var.BOXNAME"  
    > Imported from a key in the config.yaml file, essentially vm "flavor" ( from packer post-provisioner or the repackaged boxes )

- [ ] Decide vagrantfile Course of Action, Use an agnostic vagrant file w/ ruby logic
    >  [Stack Overflow example](https://stackoverflow.com/questions/16708917/how-do-i-include-variables-in-my-vagrantfile)

    ```
        # encoding: utf-8
        # -*- mode: ruby -*-
        # vi: set ft=ruby :

        require 'yaml'

        # Load Dynamic Vars from config.ymaml generated file
        current_dir    = File.dirname(File.expand_path(__FILE__))
        configs        = YAML.load_file("#{current_dir}/config.yaml")
        vagrant_config = configs['configs'][configs['configs']['select']]


        Vagrant.configure('2') do |config|
        
            mode_type == vagrant_config['mode']
            box_name == vagrant_config['base_box']
            if mode_type == ENV["deploy"]
              box_type == ENV["box_name"]
              config.vm.box = "file://boxes/" + ( box_name || default_box )
            end

    ```

- [ ] Template out the vagrant file based on the provision or deploy var via ansible task.


- [ ] Base.box optionally repackage to create staged boxes????
    **May solve the a backlog task of ovf creation, but will require a qemu-img convert task on the box.img file in the box package**     

### Template Creation

Create the Vars to be imported into the "agnosticized" vagrant file.  
> [config.yaml.j2 ](ansible\templates\config.yaml.j2)

- [x] Add lists to be used by the config.yaml creation....
      vars/vagrant_vm_vars.yaml
      ```yaml
         ---

        vm_selection: test1
        vagrant_file_vars:
          - ["test1","mode","base_box","public_ip","cpu_int","memory_int","default_driver_string","ethernet_string"]
          - ["test2","mode","base_box","public_ip","cpu_int","memory_int","default_driver_string","ethernet_string"]
          - ["test3","mode","base_box","public_ip","cpu_int","memory_int","default_driver_string","ethernet_string"]
      ```

- [ } Need to create the ansible provisioner portion for the vagrantfile.  Possibly use a key to dictate role, playbook, or whatever that will be tested.


### config.yaml example

Example with notes and possible todos.

```yaml
---
configs:
    select: 'test1'
    
    test1:
      mode: provision  # Vagrantfile for Packers post-provision vagrant plugin
      base_box: null   # box not yet created
      public_ip: '192.168.1.11'
      cpu_int: 2
      memory_int: 2048
      ethernet_string: "ens192"  # consider use gathered fact
      default_driver_string: "qemu"
    
    test2:
      mode: deploy
      base_box: libvirt-centos7
      public_ip: '192.168.2.22'
      cpu_int: 2
      memory_int: 2048
      default_driver_string: "qemu"
      ethernet_string: "ens192"

    test3:
      mode: deploy
      base_box: libvirt-rocky8
      public_ip: '192.168.3.33'
      cpu_int: 2
      memory_int: 2048
      default_driver_string: "kvm"
      ethernet_string: "ens192"

## Variables to consider
## Interface... ansible_default_ipv4.interface?
## ansible user / ssh pass for vagrant user/pass?
```






