from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

#book

class Model_all_books(models.Model):
    name_of_book = models.CharField(max_length=30)
    description_of_book = models.TextField()
    image_of_book = models.ImageField(upload_to='')
    author_of_book = models.CharField(max_length=50)
    course_of_book = models.IntegerField()
    short_description_of_book = models.TextField(max_length=100)

    def __str__(self):
        return self.name_of_book


class Model_notes_of_user(models.Model):
    title_note = models.CharField(max_length=200)
    text_note = models.TextField()
    date_note = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_note
