#!/usr/bin/env python3
"""
Script de fusion pour intégrer le frontend React dans le backend Django
Usage: python fusion_script.py
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 Exécution: {command}")
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Succès: {command}")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ Erreur: {command}")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False
    return True

def main():
    print("🚀 Début de la fusion Frontend/Backend MOCESS")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    current_dir = Path.cwd()
    if not (current_dir / "backend").exists() or not (current_dir / "Frontend").exists():
        print("❌ Erreur: Ce script doit être exécuté depuis le répertoire racine du projet MOCESS")
        sys.exit(1)
    
    # Étape 1: Construire le frontend React
    print("\n📦 Étape 1: Construction du frontend React")
    frontend_dir = current_dir / "Frontend"
    
    # Installer les dépendances
    if not run_command("npm install", cwd=frontend_dir):
        print("❌ Échec de l'installation des dépendances npm")
        sys.exit(1)
    
    # Construire le projet
    if not run_command("npm run build", cwd=frontend_dir):
        print("❌ Échec de la construction du frontend")
        sys.exit(1)
    
    # Étape 2: Créer le dossier frontend dans le backend
    print("\n📁 Étape 2: Création de la structure de fusion")
    backend_dir = current_dir / "backend"
    frontend_dist_dir = backend_dir / "frontend"
    
    # Supprimer l'ancien dossier s'il existe
    if frontend_dist_dir.exists():
        shutil.rmtree(frontend_dist_dir)
    
    # Créer le nouveau dossier
    frontend_dist_dir.mkdir()
    
    # Étape 3: Copier les fichiers construits
    print("\n📋 Étape 3: Copie des fichiers frontend")
    source_dist = frontend_dir / "dist"
    if not source_dist.exists():
        print("❌ Erreur: Le dossier dist n'existe pas après la construction")
        sys.exit(1)
    
    # Copier tous les fichiers
    shutil.copytree(source_dist, frontend_dist_dir / "dist")
    print("✅ Fichiers frontend copiés avec succès")
    
    # Étape 4: Installer les dépendances Python
    print("\n🐍 Étape 4: Installation des dépendances Python")
    if not run_command("pip install -r requirements.txt", cwd=backend_dir):
        print("❌ Échec de l'installation des dépendances Python")
        sys.exit(1)
    
    # Étape 5: Appliquer les migrations
    print("\n🗄️ Étape 5: Application des migrations")
    if not run_command("python manage.py migrate", cwd=backend_dir):
        print("❌ Échec des migrations")
        sys.exit(1)
    
    # Étape 6: Collecter les fichiers statiques
    print("\n📦 Étape 6: Collecte des fichiers statiques")
    if not run_command("python manage.py collectstatic --noinput", cwd=backend_dir):
        print("❌ Échec de la collecte des fichiers statiques")
        sys.exit(1)
    
    print("\n🎉 Fusion terminée avec succès!")
    print("=" * 50)
    print("📋 Prochaines étapes:")
    print("1. Naviguez vers le dossier backend: cd backend")
    print("2. Lancez le serveur: python manage.py runserver")
    print("3. Ouvrez votre navigateur: http://localhost:8000")
    print("\n🔧 Pour la production:")
    print("- Configurez votre serveur web (Nginx/Apache)")
    print("- Utilisez Gunicorn: gunicorn mocess_backend.wsgi")
    print("- Configurez les variables d'environnement")

if __name__ == "__main__":
    main()
