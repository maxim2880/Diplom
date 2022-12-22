from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from django.db import models

from core.models import User


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField()
    tg_user_id = models.BigIntegerField(unique=True)
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=10, unique=True)

    def generate_verification_code(self) -> str:
        code = get_random_string(10)
        self.verification_code = code
        self.save()
        return code
