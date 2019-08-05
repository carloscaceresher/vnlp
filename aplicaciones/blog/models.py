from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria No Activada', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del autor', max_length = 255 ,null = False, blank = False)
    apellidos = models.CharField('Apellidos del autor', max_length = 255 ,null = False, blank = False)
    facebook = models.URLField('Facebook',null = True, blank = True)
    twitter = models.URLField('Twitter',null = True, blank = True)
    instagram = models.URLField('Instagram',null = True, blank = True)
    web = models.URLField('Web',null = True, blank = True)
    correo = models.URLField('Email',null = True, blank = True)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título',max_length = 90, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripcion', max_length = 110, null = False, blank = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length = 255, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/NoPublicado', default = True)
    fecha_creacion = models.DateField('Fecha_creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
