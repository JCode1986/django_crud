from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('to_do_details',args=[str(self.id)])
