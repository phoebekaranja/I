from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    @classmethod
    def search_by_username(cls,search_term):
        news = cls.objects.filter(user__username=search_term)
        return news

    def __str__(self):
        return self.bio
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True)
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField(max_length = 200)
    profile = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    photo_date = models.DateTimeField(auto_now_add=True)



    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def update_caption(self,image_caption):
        self.image_caption = image_caption
        self.save()

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image
