from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag

from .utils import DetailObjectMixin, UpdateObjectMixin, DeleteObjectMixin

from .forms import PostForm, TagForm

# Create your views here.


# class PostList(ListView):
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "blog/index.html"


# class PostDetail(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"


def post_list(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags,
    }
    return render(request, "blog/tags_list.html", context)


class PostDetail(DetailObjectMixin, View):
    model = Post
    template = "blog/post_detail.html"
    # def get(self, request, slug):
    #     obj = Post.objects.get(slug__iexact=slug)
    #     context = {"post": obj}
    #     return render(request, "blog/post_detail.html", context)


class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = "blog/tags_detail.html"

    # def tags_detail(self, request, slug):
    #     obj = Tag.objects.get(slug__iexact=slug)
    #     context = {
    #         "tag": obj,
    #     }
    #     return render(request, "blog/tags_detail.html", context)


class TagCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = TagForm()
        context = {
            "form": form,
        }
        return render(request, "blog/tags_create.html", context)

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        context = {
            "form": bound_form,
        }
        return render(request, "blog/tags_create.html", context)


class PostCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            "form": form,
        }
        return render(request, "blog/post_create.html", context)

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            new_post.author = request.user
            new_post.save()
            return redirect(new_post)
        context = {
            "form": bound_form,
        }
        return render(request, "blog/post_create.html", context)


class TagUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Tag
    template = "blog/tags_update.html"
    form_class = TagForm


class PostUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Post
    template = "blog/post_update.html"
    form_class = PostForm


class TagDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Tag
    template = "blog/tags_delete.html"
    redirect_url = "tags_list"


class PostDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Post
    template = "blog/post_delete.html"
    redirect_url = "home"

