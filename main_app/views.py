from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Github
import requests

# Create your views here.

class GithubDelete(DeleteView):
    model = Github
    success_url = '/'

class GithubCreate(CreateView):
    model = Github
    fields = ('username',)
    success_url = '/'

    def find_user(self, username):
        response = requests.get(f'https://api.github.com/users/{username}')
        json = response.json()
        user_obj = {"username": username}
        user_obj["url"] = json.get('html_url')
        user_obj["repos"] = json.get('public_repos')
        return user_obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_info = self.find_user(form.instance.username)
        self.object.user = self.request.user
        self.object.url = user_info['url']
        self.object.repos = user_info['repos']
        self.object.save()
        return HttpResponseRedirect('/')


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def profile(request, username):
    user = User.objects.get(username=username)
    github = Github.objects.filter(user=user)
    return render(request, 'profile.html', {'users': [user], 'github': github})