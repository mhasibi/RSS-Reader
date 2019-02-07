from django.test import TestCase
from django.urls import reverse

class RssIndexViewTests(TestCase):
    def test_no_feed(self):
        """
        tests how the application should behave when there is no feed
        This test uses the client object supplied by the TestCase class to “mock” an HTTP request to the index view.
        After receiving the response, we use the assertEqual method of the TestCase class to test two things:

            1.	Whether or not the view responded successfully (HTTP 200)
            2.	Whether or not the feed object is None

        Note: This applies a restriction on our view that will come into play down the line (feed being None when
        no feed is supplied).

        This properly covers our bases for the index view having no user input.
        """

        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)

    def test_user_feed(self):
        """
        This test is very similar to the test_no_feed method with the difference being the url query parameter appended
        to the endpoint. Since we are supplying a feed in this use case, we instead use the assertNotEqual method to
        ensure that the feed object is not None.
        """
        response = self.client.get(reverse("index") + "?url=https://www.djangoproject.com/rss/weblog/")

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["feed"], None)

