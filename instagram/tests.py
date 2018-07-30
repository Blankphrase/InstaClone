from django.test import TestCase

from .models import Image,Category,Location
# Test for Profile

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User.objects.create_user('testuser','password')
        self.profile = Profile(bio='I am a testcase',photo='', user=self.user)
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profiel) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Donholm')
        location = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Donholm')

# Test for Image class
class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

        self.loc = Location(name="Africa")
        self.loc.save_location()

        self.image = Image(name='image test', description='my test',image_location=self.loc, image_category=self.cat)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.cat.delete_category()
        self.loc.delete_location()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('fashion')
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        images = Image.fil0ter_by_location('1')
        print(images)
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.image.save_image()
        image = Image.update_image( self.image.id, 'test update', 'my test',self.loc, self.cat)
        upimage = Image.objects.filter(id = self.image.id)
        print(upimage)
        self.assertTrue(Image.name == 'test update')
