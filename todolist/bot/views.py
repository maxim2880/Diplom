from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient
from todolist import settings
from todolist.settings import env


class BotVerifyView(generics.UpdateAPIView):
    """Представление для верификации бота"""
    model = TgUser
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        tg_client = TgClient(settings.TG_BOT_API_TOKEN)
        tg_user = TgUser.objects.filter(verification_code=data['verification_code']).first()
        if not tg_user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        tg_user.user = request.user
        tg_user.save()
        tg_client.send_message(chat_id=tg_user.tg_chat_id, text='Успешно')
        return Response(data=data, status=status.HTTP_201_CREATED)
