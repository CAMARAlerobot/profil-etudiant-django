from django.contrib import admin
from .models import Profile, Education, Project, Activity, Skill, Language, Interest

admin.site.site_header = "Administration de mon profil"
for model in (Profile, Education, Project, Activity, Skill, Language, Interest):
    admin.site.register(model)
