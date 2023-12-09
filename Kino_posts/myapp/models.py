from django.db import models


class Artiles(models.Model):
    title = models.CharField("Название страницы", max_length=20)
    name = models.CharField("Название (фильма / сериала)", max_length=20)
    image_film = models.ImageField("Изображение обложки фильма", upload_to='static/main/image')
    age = models.DateField("Дата выпуска")
    genre = models.CharField("Жанр", max_length=20)
    country = models.CharField("Страна", max_length=20)
    director = models.CharField("Режисер", max_length=20)
    cast = models.CharField("В ролях", max_length=90)
    description = models.TextField("Описание", max_length=537)
    trailer = models.FileField("Трейлер", upload_to='videos/')
    video_file = models.FileField("Видеофайл", upload_to='videos/')

    def __str__(self):
        return self.title
