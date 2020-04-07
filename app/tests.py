import json

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
    title = 'Big'
    message = 'Bob'

    @classmethod
    def setUpTestData(self):
        self.data = {
            'title': self.title,
            'message': self.message
        }


    def test_get_agilemanifesto(self):
        response = self.client.get('/agilemanifesto')
        self.assertEqual(response.status_code, 200)


    def test_get_agilemanifesto_values(self):
        response = self.client.get('/agilemanifesto/values')
        self.assertEqual(response.status_code, 200)


    def test_post_agilemanifesto_values(self):
        response = self.client.post('/agilemanifesto/values',
            json.dumps(self.data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def test_post_agilemanifesto_values_400(self):
        response = self.client.post('/agilemanifesto/values')
        self.assertEqual(response.status_code, 400)


    def test_get_agilemanifesto_principles(self):
        response = self.client.get('/agilemanifesto/principles')
        self.assertEqual(response.status_code, 200)


    def test_post_agilemanifesto_principles(self):
        response = self.client.post('/agilemanifesto/principles',
            json.dumps(self.data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def test_post_agilemanifesto_principles_400(self):
        response = self.client.post('/agilemanifesto/principles')
        self.assertEqual(response.status_code, 400)
