from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
from .models import *


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DirectorValidatorCreate
        return self.serializer_class


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return DirectorValidatorCreate
        return self.serializer_class


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieValidatorsCreate
        return self.serializer_class


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MovieDetailValidatorCreate
        return self.serializer_class


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer