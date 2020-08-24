from django.contrib import admin

from .models import Post, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "created_on",
    )
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulation_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

admin.site.register(Tag)