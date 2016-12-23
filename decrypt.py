# -*- coding: utf-8 -*-
import logging
import yaml
import os

log = logging.getLogger(__name__)
config = {
    'homedir': '/etc/salt/gpgkeys',
}

def ext_pillar(minion_id, pillar, *args, **kwargs):
    for obj in args:
        for k,v in obj.items():
            config.update({k: v})

    return _check_encryption(pillar)

def _decrypt_value(encrypted_string):
    try:
        import gnupg
        if not os.path.isdir(config['homedir']):
            raise
        gpg = gnupg.GPG(**config)
        gpg.encoding = 'utf-8'
        decrypted_string =  gpg.decrypt(encrypted_string)
        if decrypted_string.data == '':
            raise
        return yaml.safe_load(decrypted_string.data)
    except:
        log.error('Could not decrypt string. Using its encrypted representation.')
        return encrypted_string


def _check_encryption(obj):
    if isinstance(obj, dict):
        return {key: _check_encryption(val) for key, val in obj.items()}
    elif isinstance(obj, list):
        return [_check_encryption(val) for val in obj]
    elif type(obj) is str and obj.find('-----BEGIN PGP MESSAGE-----') == 0:
        return _decrypt_value(obj)
    return obj
