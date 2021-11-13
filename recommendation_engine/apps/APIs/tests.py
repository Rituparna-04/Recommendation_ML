from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "user_id": 37,
        }

        recommendation_url = "/api/v1/course_recommendation/predict"
        response = client.post(recommendation_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "OK")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
