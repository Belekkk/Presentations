## About Me

-  Based in Washington D.C
-  Former Military
-  StartUp Developer
-  DevOps @ NASA WESTPrime
-  Ansible as of yesterday

---

### **What are we going to discuss?**
![hmmm](http://user-cdn.spring.me/photos/20120509/n4faa1ff76b6a9.jpg)
---
	
![Ansible Logo](https://avatars3.githubusercontent.com/u/1507452?v=3&s=200) 
#+
![NASA Logo](http://bolo.berkeley.edu/drupal/sites/default/files/AboutUs/NASALogo.jpg)

---

## Biggest Lessons
- Access Control
- Speed
- Directory Structure & Style-Guide
- Bastion/Jump Servers ⇒ To Not
- Upgrading Ansible w/o losing your Custom Hacks
- AWS Tags to boost efficiency

---

##Access Control
![Old Rusty Lock](http://srpearceart.com/wp-content/uploads/2013/11/Old-Lock2.jpg)
--

## Ansible-Core Only
- Key-based SSH Access into Servers
- Ansible then works only on servers you have access to
- Ops & Security Access to Everything. Not Devs.
- Bastion Access Point
- Ansible installed on bastion
- Ppl could also run locally
 - Playbooks stored on a shared directory/git
- Cron...lots of cron

--

# **There were problems**
![Angry Spongebob](http://media.giphy.com/media/90FH7I3McAQ7u/giphy.gif)

--

## Painful Compliance
![Baby crying](http://www.shoestringmarketinguniversity.com/wp-content/uploads/2013/10/painful-emotions1.jpg)

--

## Trust Issues
![Fine in Dev](http://www.globalnerdy.com/wordpress/wp-content/uploads/2012/09/worked-fine-in-dev.jpg)

--

## Managment != Help
![Manager](http://www.youngandprosperous.com/wp-content/uploads/2010/09/middle-manager1.jpg)

--

## Cron =! Good Scheduler

--

### Solution?
# Ansible Tower

--

##  RBAC
** Beautiful for Multi-Tenancy **

-  Organizations
-  Teams
-  Users

--

## Built-in Logging

- Who
- What
- When
- Success/Failure

--

## Non-Techie Friendly

- One-click Updates

--

## Tower Scheduler > Cron

---

# Speed
![Speed](http://www.alejandrobarros.com/media/users/1/50369/images/public/4363/fast.gif?v=1310340865696)

--

### 2x Performance with Pipelining

- !Requiretty
- Modify ansible.cfg

--

# ansible.cfg

```
# By default, this option is disabled to preserve compatibility with
# sudoers configurations that have requiretty (the default on many distros).
# 
#pipelining = False

# if True, make ansible use scp if the connection type is ssh 
# (default is sftp)
#scp_if_ssh = True
```

--

## Disable requiretty for sudo
Sample { Jinja2 } Template file for a SysAdmin
```
%{{ item }} ALL=(ALL) NOPASSWD: ALL
%{{ item }} ALL=(ALL) NOPASSWD:/bin/*sh *, !/bin/bash
%{{ item }} ALL=(ALL) NOPASSWD:/usr/bin/sudoedit, !/usr/bin/vi*, !/usr/bin/emacs
Defaults:%{{ item }} !requiretty
```

--

## Control Machine Linux Flavor
- Easier with Debian family OS
- Opted for Ubuntu
- RHEL Machines < 7 known to have ControlPersist issues
  - Patched?

---

## Style & Uniformity
![Military Formation](http://randommization.com/wp-content/uploads/2011/11/10000-toy-soldier-installation.jpg)

--

## Why?
- YAML != Strict syntax
- 100+ Playbooks w/o a Standard is Hell

--

## Style-Guide
- Borrowed from edx
- Covers Formatting ==> Security Guidelines
- Available on GH

---

# Architecture
![nice house](http://cdn.designhomes.pics/design/www.free3dmodelz.com/wp-content/uploads/Three-fan-style-architecture-490x367.jpg)

--

## Core Only:
- Bastion Setup
  - Ansible installed
  - Inside of various VPCs

--

## Pain in the ass
- Patching across env required SSHing multiple times
- Helping devs connect through bastions sucked
- Just simply inefficient
- Created more snowflakes

--

# Simple Solution

--

## Rennovated the Environment
- Created a Single Managment VPC
  - VPC Peered into all the other VPCs
  - Home for all tools
- Tower connected via private IP addresses (faster)

---

# Upgrading & Custom Hacks

--

## My Mods
- More detail in RAM
- List of apt/yum installed packages
- Also available on GH

--

## Realized that Upgrading Ansible Removed my mods

--

## Solution:
### An ansible playbook to reapply my modifications
On GH soon...
**Note:** Requires a quick check on release notes

---

## AWS Tagging
![tags](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/images/AddEdit-Tags.png)

--

## Basic Tagging Scheme
-  op_env: prod/staging/dev
-  Name: ansible-webapp-1-prod-mgmt
-  Windows:

--

## Name Tag Technique enables

```yaml
hosts: *_webapp_*_dev_*
```

Or...

```
hosts: *_prod_*_mgmt
```

Dynamic Inventory Script does all the heavy lifting

---

# Thank You!
## Questions?