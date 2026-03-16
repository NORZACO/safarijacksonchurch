# pylint: disable=relative-beyond-top-level

from django.contrib import admin
from .models import (
    Post,
    AboutUs,
    Member, Gallery,
    MenuOver,
    EventMission,
    Album)  # noqa: E402
# Register your models here.


# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'category', 'publish_date', 'status')
#     list_filter = ('status', 'category', 'author', 'publish_date')
#     search_fields = ('title', 'category', 'author__name')
#     autocomplete_fields = ('author',)
#     prepopulated_fields = {'slug': ('title',)}

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.select_related('author')
#         return queryset

admin.site.register(EventMission)
admin.site.register(Post)  # , BlogPostAdmin)
admin.site.register(AboutUs)
admin.site.register(Member)
admin.site.register(Gallery)
admin.site.register(MenuOver)
admin.site.register(Album)
