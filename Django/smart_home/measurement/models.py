from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=False)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['pk']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    nullable = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True, blank=True)