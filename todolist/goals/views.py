from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals.filters import GoalDateFilter
from goals.models import GoalCategory, Goal, GoalComment, Board
from goals.permissions import BoardPermissions, GoalCategoryPermissions, GoalPermissions, CommentPermissions
from goals.serializers import GoalCreateSerializer, GoalCategorySerializer, GoalCategoryCreateSerializer, \
    GoalSerializer, GoalCommentCreateSerializer, GoalCommentSerializer, BoardListSerializer, BoardSerializer, \
    BoardCreateSerializer


# Вьюхи для работы с категориями целей
class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated, GoalCategoryPermissions]
    serializer_class = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['titte', 'created']
    ordering = ['title']
    search_fields = ['title', 'board']

    def get_queryset(self):
        return GoalCategory.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [permissions.IsAuthenticated, GoalCategoryPermissions]

    def get_queryset(self):
        return GoalCategory.objects.filter(board__participants__user=self.request.user,
                                           is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        #Goal.objects.filter(self.request)
        instance.save()
        return instance

# При удалении категории все цели переводятся в статус "Архив"
#     def delete_category(self):
#         self.status = self.Status.archived
#         self.save()


# Вьюхи для работы с целями
class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = GoalSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ['titte', 'created']
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user).exclude(status=Goal.Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(category__board__participants__user=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Goal.Status.archived
        instance.save()
        return instance


# Вьюхи для работы с комментариями к целям
class GoalCommentCreateView(CreateAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]
    serializer_class = GoalCommentCreateSerializer


class GoalCommentListView(ListAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ['goal']
    ordering = ['-created']

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


# Вью для работы с досками
class BoardListView(ListAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['title']

    def get_queryset(self):
        return Board.objects.filter(participants__user=self.request.user, is_deleted=False)


class BoardCreateView(CreateAPIView):
    model = Board
    permissions = [permissions.IsAuthenticated]
    serializer_class = BoardCreateSerializer


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self):
        # Обратите внимание на фильтрацию – она идет через participants
        return Board.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance: Board):
        # При удалении доски помечаем ее как is_deleted,
        # «удаляем» категории, обновляем статус целей
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance
