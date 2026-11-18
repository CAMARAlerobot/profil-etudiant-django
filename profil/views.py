from itertools import groupby
from django.shortcuts import render
from .models import Profile, Education, Project, Activity, Skill, Language, Interest


def index(request):
    skills = Skill.objects.all()
    grouped = [(cat, list(items)) for cat, items in groupby(skills, key=lambda s: s.category)]
    return render(request, "profil/index.html", {
        "profile": Profile.objects.first(),
        "educations": Education.objects.all(),
        "projects": Project.objects.all(),
        "activities": Activity.objects.all(),
        "skill_groups": grouped,
        "languages": Language.objects.all(),
        "interests": Interest.objects.all(),
    })
