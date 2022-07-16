"""
테스트 코드입니다.
"""
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from .models import Vote


class VoteCrudTest(APITestCase):
    """Vote의 CRUD를 테스트합니다."""
    def setUp(self):
        self.list_url = reverse('vote:api-list')
        self.detail_url = reverse('vote:api-detail', args=[1])

    def test_read_vote_list(self):
        """전체 투표 리스트 읽기를 테스트합니다."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vote(self):
        """개별 투표 생성을 테스트합니다."""
        data = {
            'subject': '테스트 투표를 생성합니다',
            'password': '123456',
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # DB를 확인합니다.
        obj = Vote.objects.get()
        self.assertEqual(data['subject'], obj.subject)
        self.assertEqual(0, obj.yes)
        self.assertEqual(0, obj.no)
        self.assertEqual(data['password'], obj.password)
        self.assertEqual(True, obj.is_active)

    def test_read_vote(self):
        """개별 투표 읽기를 테스트합니다."""
        data = {
            'subject': '테스트 투표를 생성합니다',
            'password': '123456',
        }
        self.client.post(self.list_url, data=data, format='json')
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DB를 확인합니다.
        obj = Vote.objects.get()
        self.assertEqual(response.data['subject'], obj.subject)
        self.assertEqual(response.data['yes'], obj.yes)
        self.assertEqual(response.data['no'], obj.no)
        self.assertEqual(response.data['password'], obj.password)
        self.assertEqual(response.data['is_active'], obj.is_active)

    def test_update_vote(self):
        """개별 투표 수정을 테스트합니다."""
        data = {
            'subject': '테스트 투표를 생성합니다',
            'password': '123456',
        }
        data2 = {
            'subject': '테스트 투표를 수정합니다.',
            'yes': 1,
            'no': 1,
            'password': '654321',
            'is_active': False,
        }
        self.client.post(self.list_url, data=data, format='json')
        response = self.client.patch(self.detail_url, data=data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # DB를 확인합니다.
        obj = Vote.objects.get()
        self.assertEqual(data2['subject'], obj.subject)
        self.assertEqual(data2['yes'], obj.yes)
        self.assertEqual(data2['no'], obj.no)
        self.assertEqual(data2['password'], obj.password)
        self.assertEqual(data2['is_active'], obj.is_active)

    def test_delete_vote(self):
        """개별 투표 삭제를 테스트합니다."""
        data = {
            'subject': '테스트 투표를 생성합니다',
            'password': '123456',
        }
        self.client.post(self.list_url, data=data, format='json')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # DB를 확인합니다.
        obj = Vote.objects.all()
        self.assertEqual(0, obj.count())
        