
### Virtualization Tools and Virtsh Cheatsheet
```
    guestfish
    virt-builder
    virt-builder-repository
    virt-copy-in
    virt-copy-out
    virt-customize
    virt-df
    virt-edit
    virt-filesystems
    virt-rescue
    virt-sparsify
    virt-sysprep
    virt-v2v
    virt-p2v
    qemu-img
    qemu-io
    qemu-nbd
```

### Basic structure
```
virsh [OPTION]... <command> <domain> [ARG]...
```

### Virsh display node information:
```
virsh nodeinfo
```

### list VM and fetch status
```
virsh list
virsh list --all
```

### get vm cpu and memory stats
```
virsh domstats --vcpu ubuntu14
virsh dommemstat  ubuntu14
```

### Virsh start vm
```
virtsh start ubuntu14
```

### virt sparsify shrink image
```
vi,virtshrt-sparsify /path/to/source.qcow2 \
    --compress /path/to/output.qcow2
```

### Virsh autostart disable
```
virsh autostart --disable test
```

### Virsh stop vm, virsh shutdown vm
```
virsh shutdown test
```

### Virsh force shutdown vm
```
virsh destroy test

```

### Virsh reboot vm
```
virsh reboot test
```

### Virsh remove vm
```
virsh destroy test 2> /dev/null
virsh undefine  test
virsh pool-refresh default
virsh vol-delete --pool default test.qcow2
```

### Virsh remove vm with storage
```
virsh undefine test --remove-all-storage
```

### Virsh create a vm
```
virt-install \
  --name centos7 \
  --description "Test VM with CentOS 7" \
  --ram=1024 \
  --vcpus=2 \
  --os-type=Linux \
  --os-variant=rhel7 \
  --disk path=/var/lib/libvirt/images/centos7.qcow2,bus=virtio,size=10 \
  --graphics none \
  --location $HOME/iso/CentOS-7-x86_64-Everything-1611.iso \
  --network bridge:virbr0 \
  --console pty,target_type=serial -x 'console=ttyS0,115200n8 serial'

```

### Create a domain and spawn a virtual machine
```
virt-install \
    --name oracle66-2 \
    --vcpus=1 \
    --ram=2048 \
    --disk path=/home/amol/Documents/ISO/oraclelinu66-2.qcow2,bus=virtio,cache=writeback \
    --graphics vnc,listen=0.0.0.0 \
    --network bridge:virbr0,model=virtio \
    --noautoconsole \
    --os-type=linux \
    --os-variant=rhel6 \
    --location=/home/amol/Documents/ISO/OracleLinux66_V52218-01.iso
```

### Virsh create volume
```
virsh vol-create-as default test_vol2.qcow2 2G
du -sh /var/lib/libvirt/images/test_vol2.qcow2
```

### List volumes
```
virsh vol-list --pool default
virsh vol-list --pool images
```

### Virsh attach a volume to vm
```

virsh attach-disk --domain test \
  --source /var/lib/libvirt/images/test_vol2.qcow2 \
  --persistent --target vdb

"    --persistent:
        Make live change persistent"
"    --target vdb:
        Target of a disk device"