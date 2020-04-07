from django.test import TestCase

from app.models import Messages

class MessagesModelTest(TestCase):
    title = 'Big'
    message = 'Bob'

    @classmethod
    def setUpTestData(self):
        Messages.objects.create(title=self.title, message=self.message)

    def test_title(self):
        message = Messages.objects.get(id=1)
        self.assertEquals(message.title, self.title)

    def test_message(self):
        message = Messages.objects.get(id=1)
        self.assertEquals(message.message, self.message)

class MessagesViewTest(TestCase):
    def test_get_agilemanifesto(self):
        response = self.client.get('/agilemanifesto')
        self.assertEqual(response.status_code, 200)


    def test_get_agilemanifesto_values(self):
        response = self.client.get('/agilemanifesto/values')
        self.assertEqual(response.status_code, 200)


    def test_get_agilemanifesto_principles(self):
        response = self.client.get('/agilemanifesto/principles')
        self.assertEqual(response.status_code, 200)
