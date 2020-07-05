from django.db import models

# Create your models here.
from emp_DRF import settings


class User(models.Model):
    sex_choice = (
        (0, 'male'),
        (1, 'female')
    )
    username=models.CharField(max_length=20)
    real_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    sex=models.SmallIntegerField(choices=sex_choice,default=0)
    class Meta:
        db_table='emp_user'
        verbose_name='用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

class Emploee(models.Model):

    name=models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pic', default='pic/right.jpg')
    salary=models.IntegerField()
    age=models.SmallIntegerField()

    class Meta:
        db_table='emp_emplist'
        verbose_name='员工'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

    # @property
    # def get_photo(self):
    #     return  ("http://127.0.0.1:8000"+settings.MEDIA_URL + str(self.photo))
    #
