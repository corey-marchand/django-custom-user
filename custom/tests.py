from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from .models import CustomUser


# Create your tests here.


class TestCustomUser(TestCase):

    def test_creation(self):
        user = get_user_model().objects.create_user(
            username='corey',
            email='corey.marchand@me.com',
            password='Python1107!'
        )

        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.email, 'corey.marchand@me.com')
        self.assertIsNotNone(user.password)

    def test_no_duplicat_email(self):
        user_1 = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        try:
            user_2 = get_user_model().objects.create_user(
                username='nottester',
                email='tester@email.com',
                password='pass'
            )
        except IntegrityError:

            print('all good')

        else:
            self.fail('failed')
