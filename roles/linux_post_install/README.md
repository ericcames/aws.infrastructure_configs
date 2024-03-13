linux_post_install
=========

This role will run a linux post install

Requirements
------------

Root access on the machines in the inventory

Role Variables
--------------
```yaml
username: customer_portal_username
password: customer_portal_password
controller_url: aap.example.com
```
Dependencies
------------

Example Playbook
----------------
```yaml
---
- name: Linux post install
  hosts: all
  connection: local

  roles:

    - role: linux_post_install
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
