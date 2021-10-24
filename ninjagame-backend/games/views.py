from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Game
from .permissions import IsOwnerOrReadOnly
from .serializers import GameSerializer
from .pagination import CustomPagination
from .filters import GameFilter


class ListCreateGameAPIView(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GameFilter

    def perform_create(self, serializer):
        # Assign the user who created the game
        serializer.save(creator=self.request.user)


class UpdateGameAPIView(UpdateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





