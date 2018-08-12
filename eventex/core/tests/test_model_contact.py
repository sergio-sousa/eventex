from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact 

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create (
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

    def test_emial(self):
        contact = Contact.objects.create(speaker = self.speaker, kind = Contact.EMAIL,
                                         value = 'hentique@bastos.net')

        self.assertTrue(Contact.objects.exists())

    def test_emial(self):
        contact = Contact.objects.create(speaker = self.speaker, kind = Contact.PHONE,
                                         value = '21-99686180')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E(email) or P(phone)"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker = self.speaker, kind = Contact.EMAIL, value = 'hentique@bastos.net')
        self.assertEqual('hentique@bastos.net', str(contact))

        