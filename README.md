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
    [todo] Test the ruby if logic...  
    - Provision variable would be for utilization by packers post provision vagrant plugin
    > This would create the intial box to be reutilized by the proceeding vagrant builds

    - Deploy key would dictate the config.vm.box = "$var.BOXNAME"  
    > Imported from a key in the config.yaml file, essentially vm "flavor" ( from packer post-provisioner or the repackaged boxes )

- [ ] Base.box optionally repackage to create staged boxes? 
    - *** May solve the backlog task of ovf creation, but will require a qemu-img convert task on the box.img file in the box package ***    

### Template Creation

Create the Vars to be imported into the "agnosticized" vagrant file.  
> [config.yaml.j2 ](ansible\templates\config.yaml.j2)

- [ ] Add lists


### Outputted Config.yaml 

Example 
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






