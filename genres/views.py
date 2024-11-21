from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from .models import Genre
from .serializers import GenreSerializer


# Create your views here.
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


'''@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "GET":
        data = {"id": genre.id, "name": genre.name}
        return JsonResponse(data)

    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data["name"]
        genre.save()
        return JsonResponse(
            {"id": genre.id, "name": genre.name}
        )

    elif request.method == "DELETE":
        genre.delete()
        return JsonResponse(
            {"message": "Gênero excluido com sucesso."}, status=204,
        )
'''
