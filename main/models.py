from django.db import models

# Create your models here.

class Subject(models.Model):
    sub_name = models.CharField('Subject name', max_length=50)
    les_name = models.CharField('Lesson name', max_length=50)
    les_dis = models.TextField('Lesson discription')
    photo = models.ImageField('')

    def __str__(self):
        return self.sub_name