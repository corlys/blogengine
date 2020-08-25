from django.shortcuts import render, get_object_or_404, redirect

from .models import *

from .forms import CommentForm


class DetailObjectMixin:
    model = None
    template = None

    def get(self, request, slug):
        # obj = self.model.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)

        context = {self.model.__name__.lower(): obj, "admin_object": obj}

        if self.model.__name__.lower() == "post":
            comments = Comment.objects.filter(post=obj)
            bound_form = CommentForm()
            context["comments"] = comments
            context["form"] = bound_form

        return render(request, self.template, context)


class CreateObjectMixin:
    pass


class UpdateObjectMixin:
    model = None
    template = None
    form_class = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(instance=obj)
        return render(
            request,
            self.template,
            context={"form": bound_form, self.model.__name__.lower(): obj},
        )

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=obj)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(
            request,
            self.template,
            context={"form": bound_form, self.model.__name__.lower(): obj},
        )


class DeleteObjectMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
