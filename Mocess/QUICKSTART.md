# 🚀 Guide de démarrage rapide - MOCESS

Ce guide vous permettra de démarrer rapidement le projet MOCESS en quelques minutes.

## ⚡ Démarrage ultra-rapide

### Option 1: Scripts automatiques (Recommandé)

1. **Démarrer le backend Django**
   ```bash
   # Double-cliquer sur le fichier
   start_backend.bat
   ```
   Ou en ligne de commande :
   ```bash
   cd backend
   .\venv\Scripts\Activate.ps1
   python manage.py runserver
   ```

2. **Démarrer le frontend React**
   ```bash
   # Double-cliquer sur le fichier
   start_frontend.bat
   ```
   Ou en ligne de commande :
   ```bash
   cd Frontend
   npm install
   npm run dev
   ```

### Option 2: Installation manuelle

#### Backend Django
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_data
python manage.py runserver
```

#### Frontend React
```bash
cd Frontend
npm install
npm run dev
```

## 🌐 Accès aux applications

- **Frontend React**: http://localhost:5173
- **Backend Django**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin
- **API REST**: http://localhost:8000/api/

## 📊 Données d'exemple

Le système est pré-configuré avec des données d'exemple :
- 2 projets (WomATLAS, PEAR-HAOUZ)
- 2 actualités
- 2 publications
- 2 ressources
- 2 membres d'équipe
- 3 partenaires
- Formulaires de contact et partenariat fonctionnels

## 🔧 Premiers pas

### 1. Se connecter à l'admin Django
- Aller sur http://localhost:8000/admin
- Utiliser les identifiants créés lors de l'installation

### 2. Tester les formulaires
- Aller sur http://localhost:5173/contact
- Remplir et soumettre le formulaire de contact
- Vérifier dans l'admin Django que le message apparaît

### 3. Ajouter du contenu
- Dans l'admin Django, aller dans "Projets"
- Cliquer sur "Ajouter un projet"
- Remplir les informations et sauvegarder

## 🐛 Résolution de problèmes

### Erreur "Module not found"
```bash
# Réinstaller les dépendances
cd backend
pip install -r requirements.txt

cd ../Frontend
npm install
```

### Erreur de base de données
```bash
cd backend
python manage.py migrate
python manage.py populate_data
```

### Erreur CORS
Vérifier que les deux serveurs sont démarrés :
- Backend sur le port 8000
- Frontend sur le port 5173

### Port déjà utilisé
```bash
# Changer le port du backend
python manage.py runserver 8001

# Changer le port du frontend
npm run dev -- --port 3000
```

## 📝 Prochaines étapes

1. **Personnaliser le contenu** via l'admin Django
2. **Modifier le design** dans les composants React
3. **Ajouter de nouvelles fonctionnalités**
4. **Configurer pour la production**

## 📞 Support

- Consulter le README.md complet
- Vérifier les logs dans la console
- Contacter l'équipe de développement

---

**Bon développement ! 🎉** 