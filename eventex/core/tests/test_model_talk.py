from django.test import TestCase
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Titulo da Palestra',
           
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
        
    def test_description_blanck(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)
    
    def test_speakers_blanck(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)
    
    def test_start_blanck(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Titulo da Palestra', str(self.talk))
