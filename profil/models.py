from django.db import models


class Profile(models.Model):
    full_name = models.CharField("Nom complet", max_length=120)
    headline = models.CharField("Titre", max_length=160, help_text="Ex : Étudiant M2 MIAGE")
    bio = models.TextField("À propos")
    hero_intro = models.TextField("Introduction du hero", blank=True,
                                  help_text="Texte court et distinct de la bio, affiché en page d'accueil.")
    photo_url = models.URLField("URL de la photo", blank=True)
    photo_asset = models.CharField("Photo (fichier statique)", max_length=200, blank=True,
                                   help_text="Ex : profil/images/photo-identite.jpeg")
    feature_image = models.CharField("Image de présentation (fichier statique)", max_length=200, blank=True,
                                     help_text="Ex : profil/images/miage-camso.jpeg")
    location = models.CharField("Ville / pays", max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField("Téléphone", max_length=30, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    cv_url = models.URLField("Lien du CV (PDF)", blank=True,
                             help_text="Lien Google Drive / Dropbox public")

    class Meta:
        verbose_name = "Profil"

    def __str__(self):
        return self.full_name

    @property
    def initials(self):
        return "".join(word[0] for word in self.full_name.split()[:2]).upper()


class Education(models.Model):
    school = models.CharField("Établissement", max_length=150)
    degree = models.CharField("Diplôme / filière", max_length=180)
    start_year = models.PositiveIntegerField("Année de tri")
    end_year = models.PositiveIntegerField("Fin", null=True, blank=True)
    period = models.CharField("Période affichée", max_length=60, blank=True,
                              help_text="Ex : Depuis oct. 2025 — laissé vide pour afficher les années")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_year"]
        verbose_name = "Formation scolaire"
        verbose_name_plural = "Parcours scolaire"

    def __str__(self):
        return f"{self.degree} - {self.school}"


class Project(models.Model):
    title = models.CharField("Titre", max_length=120)
    summary = models.TextField("Résumé")
    stack = models.CharField("Technologies", max_length=200, help_text="Séparées par des virgules")
    period = models.CharField("Période", max_length=60, blank=True)
    role = models.CharField("Rôle", max_length=120, blank=True)
    url = models.URLField("Démo en ligne", blank=True)
    repo_url = models.URLField("Code source", blank=True)
    featured = models.BooleanField("Mis en avant", default=False)
    order = models.PositiveIntegerField("Ordre", default=0)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "Projet"

    def __str__(self):
        return self.title

    def stack_list(self):
        return [s.strip() for s in self.stack.split(",") if s.strip()]


class Activity(models.Model):
    KINDS = [("conference", "Conférence"), ("formation", "Formation"),
             ("stage", "Stage"), ("certification", "Certification"),
             ("autre", "Autre")]
    kind = models.CharField("Type", max_length=20, choices=KINDS)
    title = models.CharField("Titre", max_length=160)
    organisation = models.CharField("Organisme / lieu", max_length=150, blank=True)
    date = models.DateField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Activité"
        verbose_name_plural = "Conférences, formations et expériences"

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField("Compétence", max_length=60)
    category = models.CharField("Catégorie", max_length=60, default="Technique")
    level = models.PositiveIntegerField("Niveau (0-100)", default=70)

    class Meta:
        ordering = ["category", "-level"]
        verbose_name = "Compétence"

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField("Langue", max_length=60)
    level = models.CharField("Niveau", max_length=60, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Langue"

    def __str__(self):
        return f"{self.name} ({self.level})" if self.level else self.name


class Interest(models.Model):
    name = models.CharField("Centre d'intérêt", max_length=80)

    class Meta:
        ordering = ["name"]
        verbose_name = "Centre d'intérêt"

    def __str__(self):
        return self.name
