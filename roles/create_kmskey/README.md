create_kmskey
=========

This role will create a Key Management Service (KMS) Key.

Requirements
------------

Amazon Web Console Account
Amazon Web Services Credential in Ansible Automation Platform

Role Variables
--------------

region: us-west-1  <br>
ansible_python_interpreter: /usr/bin/python3  <br>
key_purpose: hello-world  <br>
key_name: mickeys-key  <br>

Dependencies
------------

amazon.aws

Example Playbook
----------------

---
- name: Create KMS Key
  hosts: localhost
  connection: local

  roles:

    - name: create_kmskey

License
-------

https://spdx.org/licenses/GPL-3.0-only.html

Author Information
------------------

Eric C Ames
ericcames@msn.com
