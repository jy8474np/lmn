import tempfile
import filecmp
import os

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User 
from django.db import IntegrityError


import datetime

from ..models import Show, UserDetails

# Create your tests here.
import tempfile
import filecmp
import os 

from django.urls import reverse
from django.test import override_settings

from ..models import Note

from PIL import Image

# Create your tests here.

class TestUser(TestCase):

    def test_create_user_duplicate_username_fails(self):

        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='another_bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()

    def test_create_user_duplicate_email_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()

class TestUserDetails(TestCase):
    
    fixtures = ['testing_users']

    def test_user_details_fails_without_user(self):
        userDetails = UserDetails(display_name='Display Name', location='Location', favorite_genres='Favorite, Genres, Here', bio='Bio')
        with self.assertRaises(IntegrityError):
            userDetails.save()

    def test_user_details_accepts_empty_values(self): #users do not add details immediately upon registering, therefore values will be null
        user = User.objects.get(pk=1)
        userDetails = UserDetails(user=user, display_name='', location='', favorite_genres='', bio='')
        userDetails.save()

'''
class TestImageUpload(TestCase):

    fixtures = ['testing_users', 'testing_artists', 'testing_shows', 'testing_venues', 'testing_notes']

    def setUp(self):
        user = User.objects.get(note_pk=1)
        self.client.force_login(user)
        self.MEDIA_ROOT = tempfile.mkdtemp()

    def tearDown(self):
        print('Deletes temporary directory and temporary image.')

    def create_temp_image(self):
        handle, tmp_img = tempfile.mkstemp(suffix='.jpg')
        img = Image.new('RGB', (10, 10) )
        img.save(tmp_img, format='JPEG')
        return tmp_img

    def test_new_image_upload(self):
        
        img_path = self.create_temp_image()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
        
            with open(img_path, 'rb') as img_file:
                resp = self.client.post(reverse('note_detail', kwargs={'note_pk': 1} ), {'photo': img_file }, follow=True)
                
                self.assertEqual(200, resp.status_code)

                note_1 = Note.objects.get(note_pk=1)
                img_name = os.path.basename(img_path)
                expected_uploaded_path = os.path.join(self.MEDIA_ROOT, 'user_images', img_name)

                self.assertTrue(os.path.exists(expected_uploaded_path))
                self.assertIsNotNone(note_1.photo)
                self.assertTrue(filecmp.cmp( img_path,  expected_uploaded_path ))

    def test_change_image_delete_old(self):
        
        first_img_path = self.create_temp_image()
        second_img_path = self.create_temp_image()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
        
            with open(first_img_path, 'rb') as first_img:

                resp = self.client.post(reverse('note_detail', kwargs={'note_pk': 1} ), {'photo': first_img }, follow=True)

                note_1 = Note.objects.get(note_pk=1)

                first_uploaded_image = note_1.photo.name

                with open(second_img_path, 'rb') as second_img:
                    resp = self.client.post(reverse('note_detail', kwargs={'note_pk':1}), {'photo': second_img}, follow=True)

                    # first image file should be deleted 
                    # second image file should replace first image file

                    note_1 = Note.objects.get(note_pk=1)

                    second_uploaded_image = note_1.photo.name

                    first_path = os.path.join(self.MEDIA_ROOT, first_uploaded_image)
                    second_path = os.path.join(self.MEDIA_ROOT, second_uploaded_image)

                    self.assertFalse(os.path.exists(first_path))
                    self.assertTrue(os.path.exists(second_path))

    # Will likely have to integrate with Alicia's delete note function
    def test_delete_note_with_image_delete(self):
        
        img_path = self.create_temp_image()

        with self.settings(MEDIA_ROOT=self.MEDIA_ROOT):
        
            with open(img_path, 'rb') as img_file:
                resp = self.client.post(reverse('note_detail', kwargs={'note_pk': 1} ), {'photo': img_file }, follow=True)
                
                self.assertEqual(200, resp.status_code)

                note_1 = Note.objects.get(note_pk=1)
                img_name = os.path.basename(img_path)
                
                uploaded_img_path = os.path.join(self.MEDIA_ROOT, 'user_images', img_name)

                note_1 = Note.objects.get(note_pk=1)
                note_1.delete()

                self.assertFalse(os.path.exists(uploaded_img_path))

'''