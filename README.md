Pillarcrypt
=======

Decrypt gpg secrets stored in any ext_pillar. The implementation is more or less identical to the one used in [varstack](https://github.com/conversis/varstack).

Make sure you have a keypair available on the salt master. Follow this guide to set it up:
https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html#setup



Installation
------------

Pillarcypt is installed by

1. placing the `decrypt.py` in the `pillar` extension module subfolder. The tree should look like this:

  ```
  extension_modules/
  └── pillar
      └── decrypt.py
  ```

  For more information, see http://docs.saltstack.com/en/latest/ref/configuration/master.html#extension-modules

2. Adding decrypt to the `ext_pillar` directive in the salt master config:

  ```
  ext_pillar:
    - decrypt: {}
  ```

Configuration
--------------

By default the module will look for your keys under `/etc/salt/gpgkeys`, per the salt gpg renderer documentation:
https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html#setup

If you want to change that (or any other parameter), you can pass in options to gnupg in the salt master config like so:
```
ext_pillar:
  - decrypt:
    - homedir: /path/to/gnupg/homedir
    - verbose: True
```

All available options can be found in the gnupg documenation:
http://pythonhosted.org/gnupg/gnupg.html#gnupg-module

Dependency
------------

Install python-gnupg - https://pythonhosted.org/python-gnupg/

```
pip install python-gnupg
```
