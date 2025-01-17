from django.db.utils import IntegrityError
# from django.db import transaction
from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given: 테스트의 재료를 준비합니다
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When: 실제 테스트 대상(함수, api 등)을 실행합니다.
        like = do_like(user.id, article.id)

        # Then: 대상을 호출한 결과를 검증합니다.
        # 좋아요가 정말 데이터베이스에 생성되었는지 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_on_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect (When 과 Then 이 합쳐진 애매한 경우에 Expect 라고 합니다.
        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

