delete_kmskey
=========

This role will delete a Key Management Service (KMS) Key.

Requirements
------------

Amazon Web Console Account
Amazon Web Services Credential in Ansible Automation Platform

Role Variables
--------------

region: us-west-1

Dependencies
------------

amazon.aws

Example Playbook
----------------

---
- name: Delete KMS Key
  hosts: localhost
  connection: local

  roles:

    - name: delete_kmskey

License
-------

https://spdx.org/licenses/GPL-3.0-only.html

Author Information
------------------

Eric C Ames
ericcames@msn.com
