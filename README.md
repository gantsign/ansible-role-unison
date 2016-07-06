Ansible Role: Unison
====================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-unison.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-unison)

Role to install and configure the Unison file synchromizer for a Vagrant managed guest VM
[https://www.cis.upenn.edu/~bcpierce/unison](https://www.cis.upenn.edu/~bcpierce/unison).

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Files to be synchronized
unison_include_files: []

# Directories to be synchronized
unison_include_directories: []

# Paths not to synchronize (in the include dirrectories)
unison_ignore_paths: []
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

Vagrant configuration
---------------------

You need to install the `vagrant-triggers` vagrant plugin and add the following
to your `Vagrantfile`.

```ruby
  # Ensure Unison service isn't started until Vagrant shared folders are mounted
  # and stopped before shared folders are unmounted (if we don't Unison will
  # assume all files have been deleted and cascade the delete to the client VM).
  config.trigger.after :up do
    run_remote "sudo systemctl start unison"
  end
  config.trigger.after :reload do
    run_remote "sudo systemctl start unison"
  end
  config.trigger.before :halt do
    run_remote "sudo systemctl stop unison"
  end
  config.trigger.before :reload do
    run_remote "sudo systemctl stop unison"
  end
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
