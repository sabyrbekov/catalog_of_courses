from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseModel(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ('start_date', )
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f"{self.name} --> {self.start_date}"
