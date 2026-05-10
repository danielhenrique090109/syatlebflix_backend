from rest_framework.viewsets import ModelViewSet
from core.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all() # Busca todos os registros da tabela de usuários (User) no banco de dados e os armazena na variável queryset.
    serializer_class = UserSerializer