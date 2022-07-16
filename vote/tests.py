from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from .models import Vote


class VoteCrudTest(APITestCase):

    def setUp(self):
        self.url = reverse('vote:api-list')

    def test_create_vote(self):
        url = reverse('vote:api-list')
        data = {
            'subject': '테스트 투표를 생성합니다',
            'password': '123456',
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        obj = Vote.objects.get()
        self.assertEqual(data['subject'], obj.subject)
        self.assertEqual(data['password'], obj.password)

    def test_read_vote(self):
        pass

    def test_update_vote(self):
        pass

    def test_delete_vote(self):
        pass
