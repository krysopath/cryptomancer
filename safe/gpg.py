#!/usr/bin/env python3
# coding=utf-8
from pprint import pprint

import gnupg

__defaultkey__ = {'expire_date': '0',
                  'subkey_usage': 'encrypt,sign,auth',
                  'name_email': 'random@entropie.mooo.com',
                  'subkey_type': 'RSA',
                  'key_usage': '',
                  'name_real': 'random-client',
                  'key_length': 1024,
                  'name_comment': "With my brain and your brawn we'll make an excellent team!",
                  'subkey_length': 1024,
                  'key_type': 'RSA'}


class GPG:
    def __init__(self, home, opts=None):
        #print(' +++ init gpg for', home)
        self.vers = gnupg.__version__
        self.homedir = home
        if self.vers in ['2.0.2', '2.0.2-py3.4.egg', '2.3.0-py3.4.egg']:
            self.gpg = gnupg.GPG(
                homedir=self.homedir)
        elif self.vers == '0.3.6':
            self.gpg = gnupg.GPG(
                gnupghome=self.homedir)
        else:
            raise ImportError(
                ' --- unhandled gpg version: ' + self.vers
            )
        self.gpg.encoding = 'utf-8'

    def __make_a_new_key(self, keyinfo):
        pprint(keyinfo)
        print(' +++ collecting entropy...')
        key = self.gpg.gen_key(keyinfo)
        print(' +++ key finished', key.fingerprint)
        return key

    def new_key(self, keyopts):
        keyinfo = self.gpg.gen_key_input(**keyopts)
        return self.__make_a_new_key(keyinfo)

    def k_export(self, keyid, with_secret=False):
        return self.gpg.export_keys(
            keyid,
            secret=with_secret
        )

    def k_import(self, key_obj):
        return self.gpg.import_keys(key_obj)

    @property
    def keys(self):
        return self.gpg.list_keys()

    def encrypt(self, msg, recievers, signer=None, signer_pass=None, symmetric=False, trust=False):
        try:
            assert isinstance(msg, str)
            result = self.gpg.encrypt(
                msg,
                *recievers,
                default_key=signer,
                passphrase=signer_pass,
                symmetric=symmetric,
                always_trust=trust
            )

        except AssertionError:
            return False
        try:
            assert result
        except AssertionError:
            print(result)

        return result

    def decrypt(self, msg):
        return self.gpg.decrypt(
            msg
        )

    def decrypt_file(self, msg):
        return self.gpg.decrypt_file(
            msg
        )

    def sign(self, msg):
        return self.gpg.sign(
            msg,
        )

    def verify_file(self, infile):
        return self.gpg.verify_file(
            infile,
        )

    def verify(self, msg):
        return self.gpg.verify(
            msg,
        )

