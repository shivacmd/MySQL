from django.db import models

class  TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class State(TimestampModel):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    
class City(TimestampModel):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Cities'
        unique_together = (
            ('name', 'state'),
        )

    def __str__(self):
        return self.name
    
    
