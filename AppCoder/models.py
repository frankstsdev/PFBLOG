from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class IMGUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='IMGUser', null = True, blank = True)

class IMGBlogs(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='IMGBlogs', null=True, blank=True)

class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,null = False, blank = False)
    subtitulo = models.CharField(max_length=100, null = True, blank = True)
    blogCompleto = models.TextField(max_length=100,null = False, blank = False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    imagenBlog = models.ForeignKey(IMGBlogs,null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.titulo} by {self.autor.first_name} {self.autor.last_name}'


