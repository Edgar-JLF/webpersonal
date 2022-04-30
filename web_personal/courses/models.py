from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateField(auto_now= True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'contenido'
        verbose_name_plural = 'contenidos'
        ordering = ['-created']

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField(max_length=200, null = False, blank = False, verbose_name='Titulo')
    image = models.ImageField(verbose_name='Imagen', upload_to = 'blog', null= True, blank = True)
    company = models.CharField(max_length = 200, null = False, blank = False, verbose_name='Empresa emisora')
    issue = models.DateField()
    credential = models.CharField(max_length=200, null=False, blank=False, verbose_name='ID de la credencial')
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['-issue']

    def __str__(self):
        return self.title