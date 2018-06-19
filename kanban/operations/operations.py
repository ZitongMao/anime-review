from django.shortcuts import render, redirect
from django.http import HttpResponse
from kanban.forms import TitleForm
from kanban.models import Title
from datetime import datetime

def delete(request, id):
    if request.user.is_authenticated():
        Title.objects.filter(user=request.user,id=id).delete()
        titles = Title.objects.all().filter(user=request.user).order_by("status")
        context = {
            'titles':titles,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/accounts/login')

# def done(request, id):
#     if request.user.is_authenticated():
#         title = Title.objects.filter(user=request.user,id=id)
#         if title[0].done == False:
#             title.update(done=True)
#         else:
#             title.update(done=False)
#         titles = Title.objects.all().filter(user=request.user).order_by("done")
#         context = {
#             'titles':titles,
#         }
#         return render(request, 'dashboard.html', context)
#     else:
#         return redirect('/accounts/login')

def edit(request, id):
    if request.user.is_authenticated():
        title = Title.objects.filter(user=request.user,id=id)[0]
        form = TitleForm(request.POST or None, instance=title)
        context = {
    		"form": form
    	}
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        return render(request, 'edit.html', context)
    else:
        return redirect('/accounts/login')
