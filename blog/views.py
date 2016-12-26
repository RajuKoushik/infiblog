from django.shortcuts import render
from django.utils import timezone
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader

from django.shortcuts import get_object_or_404 , render
from .models import Post , Projects


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def indi_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/indi_post.html', {'post' : post})


def project_list(request):
    projects = Projects.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/project_list.html', {'projects': projects})
