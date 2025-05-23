from django.db import models
from django.urls import reverse

class CourseManager(models.Manager):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField('Imagem', upload_to='courses/images', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('courses:details_by_slug', kwargs={'slug': self.slug})

    @property
    def image_safe_url(self):
        try:
            return self.image.url
        except:
            return None

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
