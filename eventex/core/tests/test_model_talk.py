from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Titulo da Palestra',
            start='10:00',
            description='Descrição da palestra'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """talk has many speakers and vice-versa"""
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())
        
    