from datetime import datetime

from django.utils import timezone

import factory


from pytest_factoryboy import register

from goals import models

pytest_plugins = "tests.fixtures"


@register
class BoardFactory(factory.django.DjangoModelFactory):
    """board class"""

    class Meta:
        model = models.Board

    title = 'test_board_title'


@register
class CategoryFactory(factory.django.DjangoModelFactory):
    """category class"""

    class Meta:
        model = models.GoalCategory

    title = 'test_category_title'


@register
class GoalFactory(factory.django.DjangoModelFactory):
    """goal class"""

    class Meta:
        model = models.Goal

    due_date = datetime.now(tz=timezone.utc)
    description = 'some description'


@register
class CommentFactory(factory.django.DjangoModelFactory):
    """comment factory"""

    class Meta:
        model = models.GoalComment
