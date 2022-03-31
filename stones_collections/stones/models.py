from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Type_stones(models.Model):
    """Type_stones общий список типов камней с описанием"""
    type = models.CharField(max_length=100)
    text = models.TextField()


class Stone(models.Model):
    """камень созадет пользователь, выбирает его тип и описывает его сам"""
    image = models.ImageField(
        'Изображение',
        upload_to='tasks/',
        blank=True,
        null=True,
        help_text='Загрузите изображение'
    )
    type = models.ForeignKey(Type_stones, null=True,
                             on_delete=models.SET_NULL, related_name='stone')
    text = models.TextField('описание')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stone')
