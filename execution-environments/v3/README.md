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
```yaml
[Execution Environments Crash Course](https://docs.autodotes.com/EE%20Crash%20Course/01_overview/ "Execution Environments Crash Course")
[Execution environment definition](https://ansible.readthedocs.io/projects/builder/en/stable/definition/#dependencies "Execution environment definition")
```
License
-------

https://spdx.org/licenses/GPL-3.0-only.html

Author Information
------------------
```yaml
Eric C Ames
```
ericcames@msn.com
