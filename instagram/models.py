from django.db import models
import datetime as dt
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    bio = models.TextField()
    photo = models.ImageField(upload_to = 'uploads/')
    photo = ImageField( blank = True, manual_crop = '1920x1080')
    # user = modelsmodels.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_category(self, update):
        self.bio = update
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile



    def __str__(self):
        return self.bio

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads/')
    picture = ImageField( blank = True, manual_crop = '1920x1080')
    caption = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(self, caption):
        update_img = cls.objects.filter(id = id).update(caption = caption)
        return update_img

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['posted']




class Comments(models.Model):
    comment = models.TextsaField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
