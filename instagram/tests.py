from django.test import TestCase
from .models import Image,Profile

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(profile_photo="image.jpeg",bio="image")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()

    # def test_update_bio(self):
    #     self.new_profile.save_profile()
    #     self.new_profile = Profile.objects.get(id=50)
    #     profile = self.new_profile
    #     profile.update_bio('changed user bio')
    #     self.updated_profile = Profile.objects.get(id=50)
    #     self.assertEqual(self.updated_profile.bio,'changed user bio')


class ImageTestClass(TestCase):


    def setUp(self):
        self.new_image=Image(image="image.jpg",image_name="pheobe",image_caption="photo click",photo_date="last seen")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether an image can be deleted from the database
        '''
        self.new_image.save_image()
        self.new_image.delete_image()

    def test_update_caption(self):
        self.new_image.save_image()
        self.new_image = Image.objects.get(id = 3 )
        self.new_image.update_caption('changed Image caption')
        self.updated_image = Image.objects.get(id = 3)
        self.assertEqual(self.updated_image.image_caption,"changed Image caption")