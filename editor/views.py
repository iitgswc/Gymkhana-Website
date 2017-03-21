from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View

from .forms import EditForm,EditBoardForm,UserForm
from .models import Clubs,Boards,Achivements,Announcements

from django.http import Http404
import calendar
from datetime import datetime

class editBoard(View):
    form_class = EditBoardForm
    template_name = 'editor/editboard.html'


    def get(self, request,board_name):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if board_name == "Hostel Affairs Board":
            if request.user.username != "HAB" and request.user.username != "admin":
                return redirect('editor:editIndex')
        else:
            if request.user.username + " Board" != board_name and request.user.username != "admin":
                return redirect('editor:editIndex')


        try:
            board = Boards.objects.get(name=board_name)
        except Boards.DoesNotExist:
            raise Http404("Not found :( ");

        form = self.form_class(initial={
                  'chairman_details': board.chairman_details,
                  'gensec_details': board.gensec_details,
                  'eventManager_details': board.eventManager_details,
                  'announcements': board.announcements,
                  'about_us': board.about_us,
                  'extra': board.extra,

                  'event1_name': board.event1_name,
                  'event1_details': board.event1_details,
                  'event2_name': board.event2_name,
                  'event2_details': board.event2_details,
                  'event3_name': board.event3_name,
                  'event3_details': board.event3_details,
                  'event4_name': board.event4_name,
                  'event4_details': board.event4_details,
                  'event5_name': board.event5_name,
                  'event5_details': board.event5_details,
        })

        return render(request, self.template_name, {'form': form,'board': board})

    def post(self, request,board_name):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if board_name == "Hostel Affairs Board":
            if request.user.username != "HAB" and request.user.username != "admin":
                return redirect('editor:editIndex')
        else:
            if request.user.username + " Board" != board_name and request.user.username != "admin":
                return redirect('editor:editIndex')


        try:
            board = Boards.objects.get(name=board_name)
        except Boards.DoesNotExist:
            raise Http404("Not found :( ");

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            chairman_details = form.cleaned_data['chairman_details']
            gensec_details = form.cleaned_data['gensec_details']
            eventManager_details = form.cleaned_data['eventManager_details']
            announcements = form.cleaned_data['announcements']
            about_us = form.cleaned_data['about_us']
            extra = form.cleaned_data['extra']

            event1_name = form.cleaned_data['event1_name']
            event1_details = form.cleaned_data['event1_details']

            event2_name = form.cleaned_data['event2_name']
            event2_details = form.cleaned_data['event2_details']

            event3_name = form.cleaned_data['event3_name']
            event3_details = form.cleaned_data['event3_details']

            event4_name = form.cleaned_data['event4_name']
            event4_details = form.cleaned_data['event4_details']

            event5_name = form.cleaned_data['event5_name']
            event5_details = form.cleaned_data['event5_details']

            setattr(board,'chairman_details',chairman_details)
            setattr(board, 'gensec_details', gensec_details)
            setattr(board, 'eventManager_details', eventManager_details)
            setattr(board, 'announcements', announcements)
            setattr(board, 'about_us', about_us)
            setattr(board, 'extra', extra)


            setattr(board, 'event1_name', event1_name)
            setattr(board, 'event1_details', event1_details)


            setattr(board, 'event2_name', event2_name)
            setattr(board, 'event2_details', event2_details)


            setattr(board, 'event3_name', event3_name)
            setattr(board, 'event3_details', event3_details)

            setattr(board, 'event4_name', event4_name)
            setattr(board, 'event4_details', event4_details)

            setattr(board, 'event5_name', event5_name)
            setattr(board, 'event5_details', event5_details)


            if(form.cleaned_data['chairman_pic']):
                board.chairman_pic = form.cleaned_data['chairman_pic']

            if (form.cleaned_data['gensec_pic']):
                board.gensec_pic = form.cleaned_data['gensec_pic']

            if (form.cleaned_data['eventManager_pic']):
                board.eventManager_pic = form.cleaned_data['eventManager_pic']



            if (form.cleaned_data['car_pic1']):
                board.car_pic1 = form.cleaned_data['car_pic1']

            if (form.cleaned_data['car_pic2']):
                board.car_pic2 = form.cleaned_data['car_pic2']

            if (form.cleaned_data['car_pic3']):
                board.car_pic3 = form.cleaned_data['car_pic3']

            if (form.cleaned_data['car_pic4']):
                board.car_pic4 = form.cleaned_data['car_pic4']

            board.save()

            return render(request, self.template_name, {'form': form,'board': board,'msg': "Changes saved!"})
        else:
            return render(request, self.template_name, {'form': form,'board': board,'msg': "Invalid details"})


class viewBoard(View):
    def get(self, request,board_name):
        try:
            board = Boards.objects.get(name=board_name)
        except Boards.DoesNotExist:
            raise Http404("Not found :( ");

        return render(request, 'editor/viewboard.html', {'board': board})

class editClub(View):
    form_class = EditForm
    template_name = 'editor/editclub.html'


    def get(self, request,club_name):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        try:
            club = Clubs.objects.get(name=club_name)
        except Clubs.DoesNotExist:
            raise Http404("Not found :( ");

        form = self.form_class(initial={'secy_details': club.secy_details,
                  'up_events': club.up_events,
                  'about_us': club.about_us,
                  'past_events': club.past_events,
                  'projects': club.projects,
                  'links': club.links,
                  'achievements': club.achievements,
                  'contact': club.contact,
                  'extra': club.extra,
                })

        return render(request, self.template_name, {'form': form,'club': club})

    def post(self, request,club_name):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        try:
            club = Clubs.objects.get(name=club_name)
        except Clubs.DoesNotExist:
            raise Http404("Not found :( ");

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            secy_details = form.cleaned_data['secy_details']
            up_events = form.cleaned_data['up_events']
            about_us = form.cleaned_data['about_us']
            past_events = form.cleaned_data['past_events']
            projects = form.cleaned_data['projects']
            links = form.cleaned_data['links']
            achievements = form.cleaned_data['achievements']
            contact = form.cleaned_data['contact']
            extra = form.cleaned_data['extra']


            setattr(club,'secy_details',secy_details)
            setattr(club, 'up_events', up_events)
            setattr(club, 'about_us', about_us)
            setattr(club, 'past_events', past_events)
            setattr(club, 'projects', projects)
            setattr(club, 'links', links)
            setattr(club, 'achievements', achievements)
            setattr(club, 'contact', contact)
            setattr(club, 'extra', extra)


            if(form.cleaned_data['secy_pic']):
                club.secy_pic = form.cleaned_data['secy_pic']

            if (form.cleaned_data['car_pic1']):
                club.car_pic1 = form.cleaned_data['car_pic1']

            if (form.cleaned_data['car_pic2']):
                club.car_pic2 = form.cleaned_data['car_pic2']

            if (form.cleaned_data['car_pic3']):
                club.car_pic3 = form.cleaned_data['car_pic3']

            club.save()

            return render(request, self.template_name, {'form': form,'club': club,'msg': "Changes saved!"})
        else:
            return render(request, self.template_name, {'form': form,'club': club,'msg': "Invalid details"})


class viewClub(View):
    def get(self, request,club_name):
        try:
            club = Clubs.objects.get(name=club_name)
        except Clubs.DoesNotExist:
            raise Http404("Not found :( ");

        return render(request, 'editor/viewclub.html', {'club': club})

class editIndex(View):
    template_name = 'editor/editindex.html'

    def get(self, request):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        latestAchieve = Achivements.objects.all().order_by('-Postdate')[:2]
        if latestAchieve.exists() == False:
            latestAchieve = "No achievements"

        latestAnnounce = Announcements.objects.all().order_by('-Postdate')[:2]
        if latestAnnounce.exists() == False:
            latestAnnounce = "No announcements"

        return render(request, self.template_name, {'latestAchieve':latestAchieve,'latestAnnounce':latestAnnounce})

class viewIndex(View):
    template_name = 'editor/viewindex.html'

    def get(self, request):

        latestAchieve = Achivements.objects.all().order_by('-Postdate')[:2]
        if latestAchieve.exists() == False:
            latestAchieve = "No achievements"

        latestAnnounce = Announcements.objects.all().order_by('-Postdate')[:2]
        if latestAnnounce.exists() == False:
            latestAnnounce = "No announcements"

        return render(request, self.template_name, {'latestAchieve':latestAchieve,'latestAnnounce':latestAnnounce})


class editAchievements(View):
    template_name = 'editor/editachievements.html'

    def get(self, request):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if request.user.username != "admin":
            return redirect('editor:editIndex')

        listAchieve = Achivements.objects.all().order_by('-Postdate')
        return render(request, self.template_name, {'listAchieve':listAchieve})

    def post(self, request):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if request.user.username != "admin":
            return redirect('editor:editIndex')

        listAchieve = Achivements.objects.all().order_by('-Postdate')

        for i in range(1,listAchieve.__len__()+1,1):
            if 'delete'+str(i) in request.POST:
                listAchieve[i-1].delete();
                listAchieve = Achivements.objects.all().order_by('-Postdate')
                return render(request, self.template_name, {'listAchieve': listAchieve})

            if 'update'+str(i) in request.POST:
                listAchieve[i-1].Title = request.POST['Title'];
                listAchieve[i-1].Description = request.POST['Description'];
                listAchieve[i-1].Postdate = datetime.now();
                listAchieve[i-1].Link = request.POST['Link'];
                listAchieve[i-1].save();

                listAchieve = Achivements.objects.all().order_by('-Postdate')
                return render(request, self.template_name, {'listAchieve': listAchieve})

        Achivements.objects.create(Title = request.POST['Title'],Description = request.POST['Description'],Link = request.POST['Link'],Postdate = datetime.now())
        listAchieve = Achivements.objects.all().order_by('-Postdate')

        return render(request, self.template_name, {'listAchieve':listAchieve})

class viewAchievements(View):
    template_name = 'editor/viewachievements.html'

    def get(self, request):
        listAchieve = Achivements.objects.all().order_by('-Postdate')
        return render(request, self.template_name, {'listAchieve':listAchieve})



class editAnnouncements(View):
    template_name = 'editor/editannouncements.html'

    def get(self, request):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if request.user.username != "admin":
            return redirect('editor:editIndex')

        listAnnounce = Announcements.objects.all().order_by('-Postdate')
        return render(request, self.template_name, {'listAnnounce': listAnnounce})

    def post(self, request):
        if request.user.is_authenticated() == False:
            return redirect('editor:Login')

        if request.user.username != "admin":
            return redirect('editor:editIndex')

        listAnnounce = Announcements.objects.all().order_by('-Postdate')

        for i in range(1, listAnnounce.__len__() + 1, 1):
            if 'delete' + str(i) in request.POST:
                listAnnounce[i - 1].delete();
                listAnnounce = Announcements.objects.all().order_by('-Postdate')
                return render(request, self.template_name, {'listAnnounce': listAnnounce})

            if 'update' + str(i) in request.POST:
                listAnnounce[i - 1].Title = request.POST['Title'];
                listAnnounce[i - 1].Description = request.POST['Description'];
                listAnnounce[i - 1].Postdate = datetime.now();
                listAnnounce[i - 1].Link = request.POST['Link'];
                listAnnounce[i - 1].save();

                listAnnounce = Announcements.objects.all().order_by('-Postdate')
                return render(request, self.template_name, {'listAnnounce': listAnnounce})

        Announcements.objects.create(Title=request.POST['Title'], Description=request.POST['Description'],Link=request.POST['Link'], Postdate=datetime.now())
        listAnnounce = Announcements.objects.all().order_by('-Postdate')

        return render(request, self.template_name, {'listAnnounce': listAnnounce})


class viewAnnouncements(View):
    template_name = 'editor/viewannouncements.html'

    def get(self, request):
        listAnnounce = Announcements.objects.all().order_by('-Postdate')
        return render(request, self.template_name, {'listAnnounce': listAnnounce})


class Login(View):
	form_class = UserForm
	template_name = 'editor/login.html'

	def  get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def  post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			checkUser = authenticate(username=username,password=password)

			if checkUser is not None:
				if checkUser.is_active:
					login(request,checkUser)
					return redirect('editor:editIndex')
			else:
				return render(request, self.template_name, {'form': form,'msg':'Invalid Credentials'})
		else:
			return render(request, self.template_name, {'form': form,'msg':'Some error occured'})

def Logout(request):
	if request.user.is_authenticated():
		logout(request)
	return redirect('editor:viewIndex')

