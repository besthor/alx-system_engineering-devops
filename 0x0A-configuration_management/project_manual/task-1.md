#1. Install a package
mandatory
Using Puppet, install flask from pip3.

Requirements:

- Install flask
- Version must be 2.1.0
Example:
#
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
## Repo:

- GitHub repository: alx-system_engineering-devops
- Directory: 0x0A-configuration_management
- File: 1-install_a_package.pp
