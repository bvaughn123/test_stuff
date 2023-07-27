# config.yaml creation

```
---
configs:
    select: 'test1'
    
    test1:
      mode: provision  # Vagrantfile for Packers post-provision vagrant plugin
      base_box: null   # box not yet created
      public_ip: '192.168.1.11'
      cpu_int: 2
      memory_int: 2048
      ethernet_string: "ens192"
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
```

### Variables to consider

- vagrant user/pass

Option 1: `ansible user / ssh pass`
Option 2: `set as extra vars`

| :important:   | must be consitant across the packer build |
|---------------|:------------------------|

