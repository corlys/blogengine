from django.contrib import admin

from .models import Post, Tag, Comment

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


class CommentAdmin(admin.ModelAdmin):
    list_display = ("commenter", "content", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("commenter", "content")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)

admin.site.register(Tag)

admin.site.register(Comment, CommentAdmin)
