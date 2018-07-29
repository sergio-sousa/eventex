from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        """valild POST should redirect to /inscricao/"""
        data = dict(name='Henrique Bastos', cpf = '12345678901', 
                    email='henrique@bastos.com.br',phone='21-99618-6180')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
    
    def test_subscrition_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscrition_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscrition_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678901',
            'henrique@bastos.com.br',
            '21-99618-6180',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
                