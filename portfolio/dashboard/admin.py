from django.contrib import admin
from .models import AboutUser, UserProject, LinksToSocialMedia


@admin.register(AboutUser)
class AboutUserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['created_by', 'phone_number', 'created_at']
    list_filter = ['phone_number', 'created_at']

@admin.register(UserProject)
class UserProjectAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['project_name', 'created_by', 'created_at']
    list_filter = ['project_name', 'created_by', 'created_at']

# admin.site.register(UserProject)

@admin.register(LinksToSocialMedia)
class LinksToSocialMedia(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name_social_media', 'created_by', 'created_at']
    list_filter = ['name_social_media', 'created_by', 'created_at']
# admin.site.register(LinksToSocialMedia)
