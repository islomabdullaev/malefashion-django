from django.contrib import admin

from blogs.models import AuthorModel, CommentModel, TagModel, PostModel

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(TagModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)