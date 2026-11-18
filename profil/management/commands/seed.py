import datetime

from django.core.management.base import BaseCommand
from profil.models import (
    Profile, Education, Project, Activity, Skill, Language, Interest,
)


class Command(BaseCommand):
    help = "Charge les données du portfolio (remplace les données existantes)"

    def handle(self, *args, **opts):
        for model in (Profile, Education, Project, Activity, Skill, Language, Interest):
            model.objects.all().delete()

        Profile.objects.create(
            full_name="CAMARA MAMADOU",
            headline="Développeur web full-stack",
            hero_intro=(
                "Développeur en formation, je donne vie à des projets web et desktop concrets. "
                "Parcourez mon itinéraire, découvrez mes réalisations et les technologies "
                "que je maîtrise."
            ),
            bio=(
                "Étudiant en Master 2 MIAGE à l'Université Nangui Abrogoua, j'aime "
                "transformer des idées en applications web et desktop simples à utiliser. "
                "Je m'attache à concevoir des outils qui facilitent le travail des équipes, "
                "en soignant autant l'interface que la partie invisible. Curieux et rigoureux, "
                "je cherche à rendre chaque projet clair, fiable et agréable à utiliser."
            ),
            location="Abidjan, Côte d'Ivoire",
            email="camsocamara0757@gmail.com",
            phone="+225 07 09 75 67 61",
            github="https://github.com/CAMARAlerobot",
            photo_asset="profil/images/portfolio-avatar.jpeg",
            feature_image="profil/images/miage-camso.jpeg",
        )

        Education.objects.create(
            school="Université Nangui Abrogoua, Abidjan",
            degree="Master MIAGE (Master 2) — Méthodes informatiques appliquées à la gestion des entreprises",
            start_year=2025, period="Depuis oct. 2025",
            description="Formation avancée en génie logiciel, bases de données et gestion de projets.",
        )
        Education.objects.create(
            school="Université Nangui Abrogoua, Abidjan",
            degree="Licence en Sciences Fondamentales et Appliquées — Mathématiques et Informatique, spécialité Informatique",
            start_year=2025, period="2025",
        )
        Education.objects.create(
            school="Lycée Moderne Dominique Ouattara, Séguéla",
            degree="Baccalauréat série D", start_year=2022, period="2022",
        )

        projects = [
            dict(title="Gestion d'une école primaire", period="Janv. – Mars 2026",
                 role="Développeur (Master 1)", order=1, featured=True,
                 summary="Plateforme unique reliant parents, enseignants et administration. Gestion des élèves, des classes, des enseignants et des bulletins.",
                 stack="Django, Python, MySQL, Bootstrap"),
            dict(title="Cam-Soro Cloud", period="Janv. – Mars 2025",
                 role="Responsable backend (Licence 3)", order=2, featured=True,
                 summary="Site web de restauration en équipe : utilisateurs, authentification et commandes. Interaction avec la base de données et sécurisation des actions de commande.",
                 stack="Django, Python, JavaScript"),
            dict(title="Gestion des factures", period="Oct. – Déc. 2025",
                 role="Développeur (Master 1)", order=3,
                 summary="Version web (Django) à partir d'une base de données fournie et version desktop (JavaFX) sur la même logique métier.",
                 stack="Django, JavaFX, MySQL"),
            dict(title="Gestion des locations d'appartements", period="Oct. – Déc. 2025",
                 role="Développeur (Master 1)", order=4,
                 summary="Gestion des appartements, des locataires et des contrats de bail. Exploitation de l'interface d'administration Django ; versions web et desktop.",
                 stack="Django, JavaFX, MySQL"),
            dict(title="Banque de CV", period="Oct. 2024 – Janv. 2025",
                 role="Développeur (Licence 3)", order=5,
                 summary="Gestion et génération automatique de CV étudiants au format PDF, envoyés par e-mail. Espace administrateur et trombinoscope.",
                 stack="Django, Python, MySQL, PDF, E-mail"),
            dict(title="PresenceApp", period="Projet personnel", order=6,
                 summary="Application mobile de gestion des présences.",
                 stack="Flutter, Firebase"),
            dict(title="Prédiction Titanic", period="Projet personnel", order=7,
                 summary="Application web de prédiction de survie avec plusieurs modèles de machine learning.",
                 stack="Django, scikit-learn, JavaScript"),
        ]
        for project in projects:
            Project.objects.create(**project)

        Activity.objects.create(
            kind="formation", title="L'ingénierie du prompt et Agent IA",
            organisation="Formation en ligne", date=datetime.date(2026, 11, 12),
            description="Prise en main d'OpenCode et des agents IA.",
        )

        skills = [
            ("Python", "Backend", 90), ("Django", "Backend", 85),
            ("Java", "Backend", 70), ("JavaFX", "Backend", 70),
            ("JavaScript", "Frontend", 75), ("React", "Frontend", 70),
            ("TypeScript", "Frontend", 60), ("Tailwind CSS", "Frontend", 65),
            ("Bootstrap", "Frontend", 80),
            ("SQL", "Bases de données", 85), ("MySQL", "Bases de données", 80),
            ("PostgreSQL / PostGIS", "Bases de données", 75),
            ("Merise (MCD, MLD, MPD)", "Bases de données", 80),
            ("Administration réseau", "Réseaux / Systèmes", 30),
            ("Gestion des droits", "Réseaux / Systèmes", 30),
            ("Pare-feu", "Réseaux / Systèmes", 30),
            ("Linux (ligne de commande)", "Réseaux / Systèmes", 30),
            ("Git", "Outils", 85), ("GitHub", "Outils", 85),
        ]
        for name, category, level in skills:
            Skill.objects.create(name=name, category=category, level=level)

        Language.objects.create(name="Français", level="Langue maternelle")
        Language.objects.create(name="Anglais", level="Courant")

        for name in ("Football", "Lecture", "Jeux vidéo (PSP)"):
            Interest.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS("Portfolio enrichi depuis le CV."))
