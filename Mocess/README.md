# MOCESS - Centre Marocain des Études et de Recherches sur le Développement Durable

Ce projet comprend un frontend React et un backend Django pour le site web du Centre Marocain des Études et de Recherches sur le Développement Durable (MOCESS).

## 🏗️ Architecture

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Django + Django REST Framework
- **Base de données**: SQLite (développement) / PostgreSQL (production)

## 📁 Structure du projet

```
SiteMocess/
├── Frontend/          # Application React
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── sections/
│   │   ├── services/
│   │   └── hooks/
│   └── public/
└── backend/           # Application Django
    ├── api/
    ├── mocess_backend/
    └── manage.py
```

## 🚀 Installation et configuration

### Prérequis

- Node.js (v16 ou supérieur)
- Python (v3.8 ou supérieur)
- pip
- npm ou yarn

### Backend Django

1. **Naviguer vers le dossier backend**
   ```bash
   cd backend
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

7. **Peupler la base de données avec des données d'exemple**
   ```bash
   python manage.py populate_data
   ```

8. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

Le backend sera accessible sur `http://localhost:8000`
L'interface d'administration sera accessible sur `http://localhost:8000/admin`

### Frontend React

1. **Naviguer vers le dossier Frontend**
   ```bash
   cd Frontend
   ```

2. **Installer les dépendances**
   ```bash
   npm install
   ```

3. **Lancer le serveur de développement**
   ```bash
   npm run dev
   ```

Le frontend sera accessible sur `http://localhost:5173`

## 📊 Fonctionnalités

### Backend Django

#### Modèles de données
- **Projets**: Gestion des projets de recherche et développement
- **Actualités**: Articles et événements
- **Publications**: Articles scientifiques, rapports, etc.
- **Ressources**: Documents, vidéos, liens
- **Équipe**: Membres de l'équipe
- **Partenaires**: Organisations partenaires
- **Formulaires**: Contact et partenariat
- **Newsletter**: Abonnements

#### API REST
- Endpoints pour tous les modèles
- Filtrage et recherche
- Pagination
- Gestion des fichiers média

#### Interface d'administration
- Interface Django Admin personnalisée
- Gestion complète des données
- Actions en lot
- Filtres avancés

### Frontend React

#### Pages
- **Accueil**: Page d'accueil avec sections principales
- **Projets**: Affichage des projets avec filtres
- **Actualités**: Articles et événements
- **Publications**: Bibliothèque de publications
- **Ressources**: Centre de ressources
- **Équipe**: Présentation de l'équipe
- **Partenaires**: Liste des partenaires
- **Contact**: Formulaire de contact

#### Fonctionnalités
- **Formulaires fonctionnels**: Contact et partenariat
- **Recherche**: Recherche globale
- **Filtrage**: Par catégories, types, etc.
- **Responsive**: Design adaptatif
- **Multilingue**: Support français/arabe/anglais
- **Animations**: Transitions fluides

## 🔧 Configuration

### Variables d'environnement

Créer un fichier `.env` dans le dossier backend :

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### Configuration de la base de données

Pour la production, modifier `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mocess_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📝 Utilisation

### Ajouter un nouveau projet

1. Se connecter à l'admin Django (`http://localhost:8000/admin`)
2. Aller dans "Projets"
3. Cliquer sur "Ajouter un projet"
4. Remplir les informations :
   - Titre et description
   - Thème et objectifs
   - Partenaires (JSON)
   - Résultats (JSON)
   - ODD (JSON)
   - Dates et statut
   - Images (optionnel)

### Ajouter une actualité

1. Dans l'admin Django, aller dans "Actualités"
2. Cliquer sur "Ajouter une actualité"
3. Remplir :
   - Titre et description
   - Type d'actualité
   - Date de l'événement
   - Lieu et organisateurs
   - Images (optionnel)

### Gérer les formulaires

Les formulaires de contact et de partenariat sont automatiquement traités :
- Les messages apparaissent dans l'admin Django
- Possibilité de marquer comme lu/traité
- Actions en lot disponibles

## 🚀 Déploiement

### Backend (Production)

1. **Configurer les variables d'environnement**
2. **Installer les dépendances de production**
3. **Configurer la base de données PostgreSQL**
4. **Collecter les fichiers statiques**
   ```bash
   python manage.py collectstatic
   ```
5. **Configurer un serveur web (Nginx + Gunicorn)**

### Frontend (Production)

1. **Construire l'application**
   ```bash
   npm run build
   ```
2. **Servir les fichiers statiques**
3. **Configurer un serveur web (Nginx)**

## 🔍 API Endpoints

### Projets
- `GET /api/projects/` - Liste des projets
- `GET /api/projects/{slug}/` - Détail d'un projet
- `GET /api/projects/featured/` - Projets en vedette

### Actualités
- `GET /api/news/` - Liste des actualités
- `GET /api/news/{slug}/` - Détail d'une actualité
- `GET /api/news/recent/` - Actualités récentes

### Publications
- `GET /api/publications/` - Liste des publications
- `GET /api/publications/{slug}/` - Détail d'une publication

### Ressources
- `GET /api/resources/` - Liste des ressources
- `GET /api/resources/{slug}/` - Détail d'une ressource
- `POST /api/resources/{id}/download/` - Télécharger une ressource

### Formulaires
- `POST /api/contact/` - Soumettre un formulaire de contact
- `POST /api/partnership/` - Soumettre un formulaire de partenariat
- `POST /api/newsletter/` - S'abonner à la newsletter

### Statistiques
- `GET /api/stats/dashboard/` - Statistiques du tableau de bord

## 🛠️ Développement

### Ajouter un nouveau modèle

1. **Créer le modèle dans `api/models.py`**
2. **Créer le sérialiseur dans `api/serializers.py`**
3. **Créer la vue dans `api/views.py`**
4. **Ajouter l'URL dans `api/urls.py`**
5. **Créer et appliquer les migrations**
6. **Ajouter dans l'admin Django**

### Ajouter une nouvelle page React

1. **Créer le composant dans `src/pages/`**
2. **Ajouter la route dans `src/App.jsx`**
3. **Créer les hooks API nécessaires**
4. **Tester la fonctionnalité**

## 📞 Support

Pour toute question ou problème :
- Consulter la documentation Django et React
- Vérifier les logs du serveur
- Contacter l'équipe de développement

## 📄 Licence

Ce projet est développé pour le Centre MOCESS. Tous droits réservés. 