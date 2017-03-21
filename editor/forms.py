from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class meta:
        model = User
        fields = ['username','password']

class EditForm(forms.Form):
    secy_details = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '160px',
        'height': '180px',
    }), )
    secy_pic = forms.ImageField(required=False)
    up_events = forms.CharField(required=False,widget=SummernoteWidget(attrs={
            'width':'350px',
            'height': '300px',
    }),)
    about_us = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '100%',
        'height': '300px',
    }), )
    past_events = forms.CharField(required=False,widget=SummernoteWidget(attrs={

        'height': '300px',
    }), )
    projects = forms.CharField(required=False,widget=SummernoteWidget(attrs={

        'height': '300px',
    }), )
    links = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '350px',
        'height': '300px',
    }), )
    achievements = forms.CharField(required=False,widget=SummernoteWidget(attrs={
         'height': '300px',
    }), )
    contact = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '350px',
        'height': '300px',
    }), )
    extra = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    car_pic1 = forms.ImageField(required=False)
    car_pic2 = forms.ImageField(required=False)
    car_pic3 = forms.ImageField(required=False)

class EditBoardForm(forms.Form):
    chairman_details = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '210px',
        'height': '180px',
    }), )
    chairman_pic = forms.ImageField(required=False)

    gensec_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'width': '210px',
        'height': '180px',
    }), )
    gensec_pic = forms.ImageField(required=False)

    eventManager_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'width': '210px',
        'height': '180px',
    }), )
    eventManager_pic = forms.ImageField(required=False)


    announcements = forms.CharField(required=False,widget=SummernoteWidget(attrs={
            'width':'350px',
            'height': '300px',
    }),)


    about_us = forms.CharField(required=False,widget=SummernoteWidget(attrs={
        'width': '100%',
        'height': '300px',
    }), )

    extra = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    event1_name = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '100px',
        'toolbar': [
           ['style', ['bold', 'italic', 'underline', 'clear']],
           ['color', ['color']],
        ],
    }),)


    event1_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    event2_name = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '100px',
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['color', ['color']],
        ],
    }), )
    event2_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    event3_name = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '100px',
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['color', ['color']],
        ],
    }), )
    event3_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    event4_name = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '100px',
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['color', ['color']],
        ],
    }), )
    event4_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    event5_name = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '100px',
        'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['color', ['color']],
        ],
    }), )
    event5_details = forms.CharField(required=False, widget=SummernoteWidget(attrs={
        'height': '300px',
    }), )

    car_pic1 = forms.ImageField(required=False)
    car_pic2 = forms.ImageField(required=False)
    car_pic3 = forms.ImageField(required=False)
    car_pic4 = forms.ImageField(required=False)


