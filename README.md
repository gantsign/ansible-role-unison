Ansible Role: Unison
====================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-unison.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-unison)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-unison/master/LICENSE)

Role to install and configure the Unison file synchromizer for a Vagrant managed guest VM
[https://www.cis.upenn.edu/~bcpierce/unison](https://www.cis.upenn.edu/~bcpierce/unison).

Requirements
------------

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Files to be synchronized
unison_include_files: []

# Directories to be synchronized
unison_include_directories: []

# Paths not to synchronize (in the include directories)
unison_ignore_paths: []

# Path to root directory of files to be mirrored
unison_src_root: '/home/vagrant'

# Path to root directory of mirrored files
unison_mirror_root: '/vagrant/home'

# Make Unison work with the limitations of the Windows file system
unison_fat: yes

# Whether the Unison service should auto-start on startup
unison_service_auto_start: no
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.unison
      unison_include_directories:
        - .ssh
        - .gnupg
        - .m2
        - workspace
      unison_include_files:
        - .bash_history
        - .zsh_history
        - .gitconfig
      unison_ignore_paths:
        - Path .ssh/authorized_keys
        - BelowPath .m2/repository
        - Name target
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
