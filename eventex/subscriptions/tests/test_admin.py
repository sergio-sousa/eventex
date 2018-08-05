from django.test import TestCase
from unittest.mock import Mock, patch, call
from eventex.subscriptions.admin import SubscriptionModelAdmin
from eventex.subscriptions.admin import Subscription
from eventex.subscriptions.admin import admin

class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Henrique Bastos', cpf = '12345678901', 
                                    email='henrique@bastos.com.br',phone='21-99618-6180')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """action make_as paid should be installed """
        self.assertIn('mark_as_paid', self.model_admin.actions)
    
    def test_mark_all(self):
        """ Is should mark all selected subscriptions as piad """
        self.call_action()

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    
    def test_message(self):
        """it should send a message to the user. """
        mock = self.call_action()

        mock.assert_called_once_with(None, '1 Inscrição foi marcada como paga.')


    def call_action(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock



