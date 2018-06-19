from kanban.models import Title
from rest_framework import viewsets
from kanban.serializers import TitleSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from kanban.forms import TitleForm
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics

INCREASE = ''
DECREASE = '-'
sort_by = {'rating':INCREASE, 'status':INCREASE}

def about(request):
    return render(request, 'about.html',{})

def home(request):
    global sort_by, INCREASE, DECREASE
    KEY = ''
    if request.method == "POST":
        KEY = request.POST.get("rating")
        if KEY is None:
            KEY = request.POST.get("status")
        if KEY == 'rating' or KEY == 'status':
            if sort_by[KEY] == INCREASE:
                sort_by[KEY] = DECREASE
            else:
                sort_by[KEY] = INCREASE
        else:
            KEY = ''
    if KEY != '':
        print(sort_by[KEY] + KEY)
        titles = Title.objects.all().filter(user=1).order_by("status", sort_by[KEY] + KEY)
    else:
        titles = Title.objects.all().filter(user=1).order_by("created_at","status")
    context = {
        'titles':titles,
    }
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html',{})


def index(request):
    if request.user.is_authenticated():
        titles = Title.objects.all().filter(user=request.user).order_by("created_at","status")
        context = {
            'titles':titles,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('/accounts/login')

def details(request, id):
    if request.user.is_authenticated():
        title = Title.objects.get(id=id)
        context = {
            'title':title,
        }
        return render(request, 'details.html', context)
    else:
        return redirect('/accounts/login')

def add(request):
    if request.user.is_authenticated():

        form = TitleForm(request.POST or None)
        context = {
    		"form": form
    	}
        if form.is_valid():
            # form.data.update(user=request.user)
            form.save()
            title = Title.objects.filter(title=form.data['title'])
            title.update(user=request.user)
            print(form.data)
            return redirect('/dashboard')
    		# instance = form.save(commit=False)
    		# # if not instance.full_name:
    		# # 	instance.full_name = "Justin"
    		# instance.save()
        return render(request, 'add.html', context)
    else:
        return redirect('/accounts/login')

def dashboard(request):
    global sort_by, INCREASE, DECREASE
    if request.user.is_authenticated():
        KEY = ''
        if request.method == "POST":
            KEY = request.POST.get("rating")
            if KEY is None:
                KEY = request.POST.get("status")
            if KEY == 'rating' or KEY == 'status':
                if sort_by[KEY] == INCREASE:
                    sort_by[KEY] = DECREASE
                else:
                    sort_by[KEY] = INCREASE
            else:
                KEY = ''
        if KEY != '':
            print(sort_by[KEY] + KEY)
            titles = Title.objects.all().filter(user=request.user).order_by("status", sort_by[KEY] + KEY)
        else:
            titles = Title.objects.all().filter(user=request.user).order_by("created_at","status")
        context = {
            'titles':titles,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')


class TitleList(generics.ListCreateAPIView):
    def get(self, request, format=None):
        title = Title.objects.all().order_by('-created_at')
        serializer = TitleSerializer(title, many=True)
        return Response(serializer.data)
    @permission_classes((IsAdminUser, ))
    def Title(self, request, format=None):
        user = request.user
        serializer = TitleSerializer(data=request.data, context={'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_REQUEST)

    serializer_class = TitleSerializer


class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
