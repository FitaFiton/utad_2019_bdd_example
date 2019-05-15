from django.test import TestCase


# Create your tests here.
class SomeFunnyTest(TestCase):

    def test_string_pass(self):
        self.assertEqual("a", "a")

    def test_string_fail(self):
        self.assertEqual("a", "b")
