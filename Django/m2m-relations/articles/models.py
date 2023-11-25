from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименовани')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-title']

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='topic')
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField()

    class Meta:
        ordering = ['-is_main']


