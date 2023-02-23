from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'message': 'Data received!',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': 'Data received!',
                              'director': DirectorSerializer(director).data})



@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        """ LIST """
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        """ CREATE """
        name = request.data.get('name')
        text = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(name=name, description=text, duration=duration,
                                     director=director)
        movie.save()
        return Response(data={'message': 'Data received!',
                              'movie': MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.name = request.data.get('name')
        movie.text = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.save()
        return Response(data={'message': 'Data received!',
                              'movie': MovieSerializer(movie).data})



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializere(review).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializere(review).data})


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieDetailSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
