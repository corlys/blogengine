from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    # commented code are for manual Forms not ModelForm
    class Meta:
        model = Tag
        fields = ["title", "slug"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
        }

    # title = forms.CharField(max_length=150)
    # slug = forms.SlugField(max_length=150)

    # title.widget.attrs.update({"class": "form-control"})
    # slug.widget.attrs.update({"class": "form-control"})

    def clean_slug(self):
        new_slug = self.cleaned_data.get("slug").lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be created")
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f"Slug should be UNIQUE. We already have {new_slug}")
        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data.get("title"), slug=self.cleaned_data.get("slug"),
    #     )
    #     return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "tags", "content", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.RadioSelect(attrs={"class": "form-check-input"}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get("slug").lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be created")
        return new_slug
