# config.yaml creation

```yaml

---
configs:
  select: "test1"

    test1:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      default_driver: "default_driver"

    test2:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      default_driver: "default_driver"

    test3:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      default_driver: "default_driver"
```

### Variables to consider

- vagrant user/pass

Option 1: `ansible user / ssh pass`
Option 2: `set as extra vars`

| :important:   | must be consitant across the packer build |
|---------------|:------------------------|

