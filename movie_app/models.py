from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    @property
    def movie_count(self):
        return self.movie_set.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def filtered_reviews(self):
        return self.movie_reviews.filter(stars__gte=4)

    @property
    def rating(self):
        count = self.movie_reviews.all().count()
        stars = sum([i.stars for i in self.movie_reviews.all()])
        if count == 0:
            return None
        return stars // count


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movie_reviews')
    stars = models.IntegerField(choices=(
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *'),
    ), default=5)

    def __str__(self):
        return f"{self.movie.name} - {self.text[:50]}..."
