Container Creation Steps
=========
```yaml
ansible-builder create
ansible-builder build -t ee-aws
podman login https://quay.io
podman push localhost/ee-aws quay.io/zigfreed/ee-aws
```
Documentation
------------
- [Execution Environments Crash Course](https://docs.autodotes.com/EE%20Crash%20Course/01_overview/ "Execution Environments Crash Course")
- [Execution environment definition](https://ansible.readthedocs.io/projects/builder/en/stable/definition/#dependencies "Execution environment definition")

Container
------------
- [Custom Execution Environment](https://quay.io/repository/zigfreed/ee-aws "Custom Execution Environment")
