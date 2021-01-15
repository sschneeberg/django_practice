from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Github

# Create your views here.

class GithubDelete(DeleteView):
    model = Github
    success_url = '/'

class GithubCreate(CreateView):
    model = Github
    fields = 'username'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print('FORM----------------', form)
        return HttpResponseRedirect('/')


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def profile(request, username):
    user = User.objects.get(username=username)
    github = Github.objects.filter(user=user)
    return render(request, 'profile.html', {'users': [user], 'github': github})