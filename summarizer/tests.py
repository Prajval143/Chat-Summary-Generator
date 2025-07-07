from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SummarizerAPITest(APITestCase):

    def test_chat_summary(self):
        url = reverse('summarize-chat')
        data = {
            "chat": [
                {"role": "user", "message": "Hi, I need help with my order."},
                {"role": "bot",  "message": "Sure, can you provide your order ID?"},
                {"role": "user", "message": "Yes, it's #ORD12345."},
                {"role": "bot",  "message": "Thank you. I see that your order was placed two days ago and is currently in transit."},
                {"role": "user", "message": "Can you tell me the expected delivery date?"},
                {"role": "bot",  "message": "The estimated delivery date is July 10th."},
                {"role": "user", "message": "Can I change the delivery address?"},
                {"role": "bot",  "message": "Unfortunately, the order has already been shipped and we can't change the address now."},
                {"role": "user", "message": "Okay, no problem. Can I at least track the shipment?"},
                {"role": "bot",  "message": "Yes, here's your tracking link: https://courier.example.com/track/ORD12345"},
                {"role": "user", "message": "Thanks for the help."},
                {"role": "bot", "message": "You're welcome! Let me know if you need anything else."}
            ]

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("summary", response.data)
        print("Summary:", response.data["summary"])
