from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            # author=cls.user,
            text='Текст поста оказался слишком коротким,'
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        error_str_post = f'Вывод не имеет {settings.INTRODUCTION} символов'
        self.assertEqual(
            self.post.__str__(),
            self.post.text[:settings.INTRODUCTION],
            error_str_post
        )

