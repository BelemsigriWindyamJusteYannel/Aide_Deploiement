# 🔄 Guide de Fusion Frontend/Backend MOCESS

Ce guide explique comment fusionner le frontend React et le backend Django en un seul projet pour faciliter l'hébergement.

## 📋 Prérequis

- Python 3.8+
- Node.js 16+
- npm ou yarn

## 🚀 Méthodes de Fusion

### Méthode 1: Script Automatique (Recommandée)

```bash
# Depuis le répertoire racine du projet
python fusion_script.py
```

### Méthode 2: Commande Django

```bash
# Depuis le dossier backend
cd backend
python manage.py build_frontend
```

### Méthode 3: Manuel

#### Étape 1: Construire le Frontend
```bash
cd Frontend
npm install
npm run build
```

#### Étape 2: Copier les Fichiers
```bash
# Créer le dossier dans le backend
mkdir backend/frontend
# Copier les fichiers construits
cp -r Frontend/dist backend/frontend/
```

#### Étape 3: Configurer Django
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

## 🏗️ Structure Après Fusion

```
Mocess/
├── backend/                    # Projet Django principal
│   ├── frontend/              # Frontend React intégré
│   │   └── dist/              # Fichiers construits
│   ├── api/                   # API Django
│   ├── mocess_backend/        # Configuration Django
│   ├── manage.py
│   └── requirements.txt
└── Frontend/                  # Code source React (développement)
    ├── src/
    ├── package.json
    └── ...
```

## 🌐 Démarrage

### Développement
```bash
cd backend
python manage.py runserver
# Ouvrir http://localhost:8000
```

### Production
```bash
cd backend
python manage.py collectstatic --noinput
gunicorn mocess_backend.wsgi
```

## ⚙️ Configuration

### Variables d'Environnement
Créer un fichier `.env` dans le dossier `backend/` :

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/mocess_db
```

### Serveur Web (Nginx)
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location /static/ {
        alias /path/to/mocess/backend/staticfiles/;
    }
    
    location /media/ {
        alias /path/to/mocess/backend/media/;
    }
    
    location / {
        proxy_pass https://aide-deploiement.vercel.app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🔧 Avantages de la Fusion

### ✅ Avantages
- **Déploiement simplifié** : Un seul serveur
- **Gestion des routes** : Django gère tout le routing
- **Fichiers statiques** : Servis par Django/WhiteNoise
- **SEO amélioré** : Meilleur référencement
- **Performance** : Moins de requêtes HTTP

### ⚠️ Considérations
- **Développement** : Nécessite de reconstruire le frontend
- **Cache** : Gestion du cache des fichiers statiques
- **Debugging** : Plus complexe en développement

## 🛠️ Développement

### Workflow Recommandé
1. **Développement Frontend** : Travailler dans `Frontend/`
2. **Test Backend** : Utiliser l'API séparément
3. **Intégration** : Construire et fusionner
4. **Test Complet** : Tester l'application fusionnée

### Commandes Utiles
```bash
# Reconstruire le frontend
cd Frontend && npm run build

# Intégrer dans Django
cd backend && python manage.py build_frontend

# Redémarrer le serveur
python manage.py runserver
```

## 🚀 Déploiement

### Heroku
```bash
# Créer Procfile
echo "web: gunicorn mocess_backend.wsgi" > backend/Procfile

# Déployer
heroku create your-app-name
git push heroku main
```

### VPS/Dedicated
```bash
# Installer les dépendances système
sudo apt update
sudo apt install python3 python3-pip nginx

# Configurer l'application
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Configurer Gunicorn
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

## 🔍 Dépannage

### Problèmes Courants

#### Frontend non trouvé
```bash
# Vérifier que les fichiers sont copiés
ls -la backend/frontend/dist/

# Reconstruire si nécessaire
python manage.py build_frontend
```

#### Erreurs de fichiers statiques
```bash
# Recueillir les fichiers statiques
python manage.py collectstatic --noinput

# Vérifier les permissions
chmod -R 755 backend/staticfiles/
```

#### Erreurs de base de données
```bash
# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser
```

## 📞 Support

Pour toute question ou problème :
1. Vérifier les logs Django
2. Consulter la documentation Django/React
3. Contacter l'équipe de développement

---

**Note** : Cette fusion simplifie grandement l'hébergement en unifiant le frontend et le backend dans un seul projet Django.
