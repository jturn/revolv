from django.contrib import admin

from .models import Category, DonationLevel, Project, ProjectUpdate, AnonymousUserDetail

admin.site.register(Category)
admin.site.register(DonationLevel)
admin.site.register(Project)
admin.site.register(ProjectUpdate)
admin.site.register(AnonymousUserDetail)
