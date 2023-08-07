# config.yaml creation

Select variable chooses the VM to build, and the VM settings are defined in yaml block named accordingly.


-  [todo?] include the vagrant-disksizek plugin and add a key with a default to the template file.
-  [todo?] include distro key, RHEL, DEB, ect.
-  [todo?] include flavor similiar to AMI instances, and appropriate mapping of settings for rapid dev env spin ups.


```yaml

---
configs:
  select: "centos7"

    centos7:
      base_box: "centos7.box"
      cpu: "2"
      memory: "2048"
      driver: "qemu"

    rocky8:
      base_box: "rocky8.box"
      cpu: "2"
      memory: "2048"
      driver: "qemu"
```

secec




