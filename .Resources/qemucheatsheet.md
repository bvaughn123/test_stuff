
### Covert image
```
qemu-img convert -p -f qcow2 -O qcow2 /path/to/image.qcow2 /path/to/image.qcow2
```
### Covert image with compression
```
qemu-img convert -p -f vmdk -O qcow2 -c /path/to/image.vmdk /path/to/image.cow2
```
### get qemu image info
```
qemu-img info /path/to/image.qcow2
```
### get qemu image info with json format
```
qemu-img info --output=json /path/to/image.qcow2
```
### get qemu image info with json format and pretty print
```
qemu-img info --output=json /path/to/image.qcow2 | jq .
```
### resize grow qemu image
```
qemu-img resize /path/to/image.qcow2 +10G
```
### resize shrink qemu image
```
qemu-img resize /path/to/image.qcow2 -10G
```
### resize qemu image to 10G
```
qemu-img resize /path/to/image.qcow2 10G
```
### resize qemu image to 10G with force
```
qemu-img resize -f /path/to/image.qcow2 10G
```
### resize qemu image to 10G with force and preallocation disabled
```
qemu-img resize -f /path/to/image.qcow2 10G --preallocation=off
```
### resize qemu image to 10G with force and preallocation metadata
```
qemu-img resize -f /path/to/image.qcow2 10G --preallocation=metadata
```
### resize qemu image to 10G with force and preallocation full
```
qemu-img resize -f /path/to/image.qcow2 10G --preallocation=full
```