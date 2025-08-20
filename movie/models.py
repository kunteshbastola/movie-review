from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/',blank=True, null=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.movie.title} by {self.user.username}'
