# Mini profil étudiant en ligne (Django + Bootstrap + PostgreSQL + Vercel)

Site one-page : à propos, parcours, projets, conférences/formations, compétences, contact.
Tout le contenu se modifie dans `/admin` (aucun code à toucher).

## 1. Lancer en local
```bash
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed            # données d'exemple (optionnel)
python manage.py createsuperuser
python manage.py runserver
```
Site : http://127.0.0.1:8000 - Admin : http://127.0.0.1:8000/admin

En local, c'est SQLite. PostgreSQL est utilisé dès que `DATABASE_URL` est défini.

## 2. Créer la base PostgreSQL gratuite
Crée une base sur **Neon** (neon.tech) ou **Supabase** et copie l'URL de connexion :
`postgresql://user:motdepasse@hote/base?sslmode=require`

## 3. Préparer la base distante (depuis ton PC)
```bash
# Windows (PowerShell) : $env:DATABASE_URL="..."    Linux/Mac : export DATABASE_URL="..."
python manage.py migrate
python manage.py createsuperuser
python manage.py seed            # optionnel
```
Vercel n'exécute pas les migrations : on les fait toujours depuis ton PC.

## 4. Déployer sur Vercel
1. Pousse le projet sur GitHub (le dossier `staticfiles/` doit être inclus).
2. Sur vercel.com : **Add New > Project**, importe le dépôt.
3. Variables d'environnement :
   - `SECRET_KEY` : une longue chaîne aléatoire
   - `DATABASE_URL` : l'URL PostgreSQL (le fichier `db.sqlite3` ne fonctionne pas sur Vercel)
   - `DEBUG` : `0`
   - Si tu as un domaine personnalisé : `EXTRA_HOSTS` et `CSRF_TRUSTED_ORIGINS` (voir `.env.example`)
4. **Deploy**. Ton site sera sur `https://ton-projet.vercel.app`.

## À savoir
- Après toute modification de CSS/static : `python manage.py collectstatic --noinput` puis recommit.
- Vercel ne conserve pas les fichiers envoyés : la photo et le CV sont donc des **liens** (Google Drive public, GitHub, etc.).
- Pour ton propre domaine, ajoute-le dans Vercel puis dans la variable `EXTRA_HOSTS`.
