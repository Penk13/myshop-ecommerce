from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'bio', 'address', 'birth_date', 'profile_pic')


admin.site.register(Profile, ProfileAdmin)
