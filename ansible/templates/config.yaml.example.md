# config.yaml creation

```yaml

---
configs:
  select: "test1"

    test1:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      driver: "driver"

    test2:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      driver: "driver"

    test3:
      base_box: "base_box"
      cpu: "cpu"
      memory: "memory"
      driver: "driver"
```

### Variables to consider

- Task to change root user/pass update needed

Option 1: `ansible user / ssh pass vars`
Option 2: `set as extra vars`

| :important:   | must be consitant across the ks and packer build |
|---------------|:------------------------|

