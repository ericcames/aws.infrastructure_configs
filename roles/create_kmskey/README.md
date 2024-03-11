create_kmskey
=========

This role will create a Key Management Service (KMS) Key.

Requirements
------------

<br>Amazon Web Console Account<br/>
<br>Amazon Web Services Credential in Ansible Automation Platform<br/>

Role Variables
--------------

<br>region: us-west-1<br/>
<br>ansible_python_interpreter: /usr/bin/python3<br/>
<br>key_purpose: hello-world<br/>
<br>key_name: mickeys-key<br/>

Dependencies
------------

amazon.aws

Example Playbook
----------------

<br>---<br/>
<br>- name: Create KMS Key<br/>
  <br>hosts: localhost<br/>
  <br>connection: local<br/>

  <br>roles:<br/>

    <br>- name: create_kmskey<br/>

License
-------

https://spdx.org/licenses/GPL-3.0-only.html

Author Information
------------------

Eric C Ames
ericcames@msn.com
