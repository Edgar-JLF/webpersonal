from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(max_length=200, null=False, blank=False, verbose_name='Titulo')
    content=RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='portfolio')
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['created']

    def __str__(self):
        return self.title