#!/usr/bin/env python3 -[v]-m unittest
import os
import sys
import unittest

curr = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(curr)
sys.path.append(parent)
from auth import User




class TestAuthMethods(unittest.TestCase):
    user = User()

    def test_check_email(self):
        """
        Testando a possibilidade de vazar senhas algum
        tipo nao pertitido de password
        """
        wrong_emails: list[str] = [
            'test_email_without_the_at_sign.error.py',
            'test_with@@error.py',
            'test_emai@_without_dot_py',
            'test_emai_with_two@_without_dot_py',
            'test_emai@_with_two..py',
            'test_emai@_with_two.py'
        ]

        for e in wrong_emails:
            print(f'Check E-mail: {e}')
            self.assertFalse(self.user.check_email(e))

        

    def test_check_passwd(self):
        """
        Testando a possibilidade de vazar senhas inválidas
        """
        print()
        wrong_passwd: list[str] = [
            'wrongpasswd',
            'wrongPasswd',
            'wrong9asswd',
            'wrong#asswd',
            'WRONGPASSWD',
            'WRONG9ASSWD',
            'WRONG#ASSWD',
            'wrong'      ,
            'WRONG'      ,
            'wrong1'     ,
            'WRONG1'     ,
            'wrong@'     ,
            'WRONG@'     ,
            '123456'     ,
            '12345678'   ,
            '123457#'    ,
            '1234567#'   ,
            '!@#$&&'     ,
            '!@#$&&*('   ,
            'wrong1@'    ,
            'wrong1@@'   ,
            'Wrong1@'   ,
        ]
        
        for p in wrong_passwd:
            print(f'Check Passwd: {p}')
            self.assertFalse(self.user.check_passwd(p))
              
