create_kmskey
=========

This role will create a Key Management Service (KMS) Key.

Requirements
------------
```yaml
---
Amazon Web Console Account
Amazon Web Services Credential in Ansible Automation Platform
```
Role Variables
--------------
```yaml
---
region: us-west-1
ansible_python_interpreter: /usr/bin/python3
key_purpose: hello-world
key_name: mickeys-key
```
Dependencies
------------

amazon.aws

Example Playbook
----------------
```yaml
---
- name: Create KMS Key
  hosts: localhost
  connection: local

  roles:

    - name: create_kmskey
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
