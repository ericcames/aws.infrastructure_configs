get_kmskey_info
=========

This role will get all Key Management Service (KMS) Key info.

Requirements
------------

Amazon Web Console Account
Amazon Web Services Credential in Ansible Automation Platform

Role Variables
--------------

region: us-west-1
ansible_python_interpreter: /usr/bin/python3
ansible_python_interpreter: /usr/bin/python3
key_purpose: hello-world
key_name: mickeys-key

Dependencies
------------

amazon.aws

Example Playbook
----------------

---
- name: Get KMS Key info
  hosts: localhost
  connection: local

  roles:

    - name: get_kmskey_info

License
-------

https://spdx.org/licenses/GPL-3.0-only.html

Author Information
------------------

Eric C Ames
ericcames@msn.com
