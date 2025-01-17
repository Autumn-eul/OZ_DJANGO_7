from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
        # raise Exception
        return Like.objects.create(user_id=user_id, article_id=article_id)
