create_vpc
=========

This role will create an Amazon Virtual Private Cloud (VPC).

Requirements
------------
```yaml
Amazon Web Console Account
Amazon Web Services Credential in Ansible Automation Platform
```
Role Variables
--------------
```yaml
vpc_name: your_vpc_name_goes_here
vpc_cidr: 172.16.3.0/24
region: us-west-1
user_name: first.last
alwaysup: false
deleteby: hercules
ec2_ansible_group: "{{ user_name }}"
ec2_security_group_name: "{{ vpc_name }}_SECGRP"
ec2_vpc_subnet_name: "{{ vpc_name }}_Subnet"
ec2_rt_name: "{{ vpc_name }}_RT_Internet"
ec2_igw_name: "{{ vpc_name }}_IGW"
my_email_address: "{{ user_name }}@redhat.com"
```
Dependencies
------------
```yaml
amazon.aws
```
Example Playbook
----------------
```yaml
---
- name: Create AWS VPC for Ansible Automation Platform deployment
  hosts: localhost
  connection: local

  roles:

    - name: create_vpc
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
