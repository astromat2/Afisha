from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def director_list_api_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data)
