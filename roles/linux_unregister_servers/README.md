linux_unregister_servers
=========

This will unregister the server from Insights and the Customer Portal.

Requirements
------------

Role Variables
--------------
```yaml
username: customer_portal_username
password: customer_portal_password
```
Dependencies
------------

Example Playbook
----------------
```yaml
---
- name: Linux unregistration
  hosts: all
  connection: local

  roles:

    - role: linux_unregister_servers
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
