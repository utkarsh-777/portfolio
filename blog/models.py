from django.db import models

class BlogModel(models.Model):
    Blogtitle = models.CharField(max_length = 200)
    Blogdescription = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to = 'blog/images/',blank = True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.Blogtitle
