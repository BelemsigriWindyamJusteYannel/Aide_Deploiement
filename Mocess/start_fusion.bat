@echo off
echo 🚀 Début de la fusion Frontend/Backend MOCESS
echo ================================================

REM Vérifier que nous sommes dans le bon répertoire
if not exist "backend" (
    echo ❌ Erreur: Dossier backend non trouvé
    pause
    exit /b 1
)

if not exist "Frontend" (
    echo ❌ Erreur: Dossier Frontend non trouvé
    pause
    exit /b 1
)

echo 📦 Étape 1: Construction du frontend React
cd Frontend

echo 🔄 Installation des dépendances npm...
call npm install
if errorlevel 1 (
    echo ❌ Échec de l'installation des dépendances npm
    pause
    exit /b 1
)

echo 🔨 Construction du projet React...
call npm run build
if errorlevel 1 (
    echo ❌ Échec de la construction du frontend
    pause
    exit /b 1
)

cd ..

echo 📁 Étape 2: Création de la structure de fusion
if exist "backend\frontend" (
    echo 🗑️ Suppression de l'ancien dossier frontend...
    rmdir /s /q "backend\frontend"
)

echo 📋 Création du nouveau dossier...
mkdir "backend\frontend"

echo 📋 Étape 3: Copie des fichiers frontend
if not exist "Frontend\dist" (
    echo ❌ Erreur: Le dossier dist n'existe pas après la construction
    pause
    exit /b 1
)

echo 🔄 Copie des fichiers...
xcopy "Frontend\dist" "backend\frontend\dist" /E /I /Y
if errorlevel 1 (
    echo ❌ Erreur lors de la copie des fichiers
    pause
    exit /b 1
)

echo ✅ Fichiers frontend copiés avec succès

echo 🐍 Étape 4: Installation des dépendances Python
cd backend

echo 🔄 Installation des dépendances Python...
call pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Échec de l'installation des dépendances Python
    pause
    exit /b 1
)

echo 🗄️ Étape 5: Application des migrations
call python manage.py migrate
if errorlevel 1 (
    echo ❌ Échec des migrations
    pause
    exit /b 1
)

echo 📦 Étape 6: Collecte des fichiers statiques
call python manage.py collectstatic --noinput
if errorlevel 1 (
    echo ❌ Échec de la collecte des fichiers statiques
    pause
    exit /b 1
)

echo.
echo 🎉 Fusion terminée avec succès!
echo ================================================
echo 📋 Prochaines étapes:
echo 1. Le serveur est prêt à être lancé
echo 2. Lancez: python manage.py runserver
echo 3. Ouvrez votre navigateur: http://localhost:8000
echo.
echo 🔧 Pour la production:
echo - Configurez votre serveur web (Nginx/Apache)
echo - Utilisez Gunicorn: gunicorn mocess_backend.wsgi
echo - Configurez les variables d'environnement
echo.
pause
