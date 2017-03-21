from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class Achivements(models.Model):
    Title = models.CharField(max_length=100,default="Title here",blank=False);
    Description = models.CharField(max_length=10000,default="Description here",blank=True);
    Link = models.CharField(max_length=100,default="Link here",blank=True);

    Postdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Title

class Announcements(models.Model):
    Title = models.CharField(max_length=100,default="Title here");
    Description = models.CharField(max_length=10000,default="Description here");
    Link = models.CharField(max_length=100,default="Link here");

    Postdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Title


class Clubs(models.Model):
    name = models.CharField(max_length=50,default="Club Name")
    secy_details = models.CharField(max_length=500000,default="",blank=True)
    secy_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    up_events = models.CharField(max_length=500000,default="",blank=True)
    about_us = models.CharField(max_length=500000,default="",blank=True)
    past_events = models.CharField(max_length=500000,default="",blank=True)
    projects = models.CharField(max_length=500000,default="",blank=True)
    links = models.CharField(max_length=500000,default="",blank=True)
    achievements = models.CharField(max_length=500000, default="",blank=True)
    contact = models.CharField(max_length=500000, default="",blank=True)
    extra = models.CharField(max_length=500000, default="",blank=True)

    car_pic1 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    car_pic2 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    car_pic3 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')

    def __str__(self):
        return self.name

class Boards(models.Model):
    name = models.CharField(max_length=50,default="Board Name")

    chairman_details = models.CharField(max_length=500000,default="",blank=True)
    chairman_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')

    gensec_details = models.CharField(max_length=500000, default="", blank=True)
    gensec_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')


    eventManager_details = models.CharField(max_length=500000, default="", blank=True)
    eventManager_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')

    announcements = models.CharField(max_length=500000,default="",blank=True)

    about_us = models.CharField(max_length=500000,default="",blank=True)
    extra = models.CharField(max_length=500000, default="",blank=True)

    event1_name = models.CharField(max_length=500000, default="", blank=True)
    event1_details = models.CharField(max_length=500000, default="", blank=True)

    event2_name = models.CharField(max_length=500000, default="", blank=True)
    event2_details = models.CharField(max_length=500000, default="", blank=True)

    event3_name = models.CharField(max_length=500000, default="", blank=True)
    event3_details = models.CharField(max_length=500000, default="", blank=True)

    event4_name = models.CharField(max_length=500000, default="", blank=True)
    event4_details = models.CharField(max_length=500000, default="", blank=True)

    event5_name = models.CharField(max_length=500000, default="", blank=True)
    event5_details = models.CharField(max_length=500000, default="", blank=True)


    car_pic1 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    car_pic2 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    car_pic3 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')
    car_pic4 = models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img2.jpg')

    def __str__(self):
        return self.name