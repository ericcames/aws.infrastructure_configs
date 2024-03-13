inventory_remove_servers
=========

This role will remove servers from an inventory on your ansible controller

Requirements
------------

```yaml
Admin Account on your Ansible Controller
An inventory on your controller that matches the one set in your inventory_name variable
```

Role Variables
--------------
```yaml
controller_url: example.com
controller_user: mickey.mouse
controller_passwd: password
server_name: "Linux Demo Server"
inventory_name: "AWS Inventory - Managed"
```
Dependencies
------------

Example Playbook
----------------
```yaml
---
- name:
  hosts: localhost
  connection: local

  roles:

    - role: inventory_remove_servers
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