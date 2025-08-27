#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import shutil
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mocess_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ajouter une commande personnalisée pour la fusion
    if len(sys.argv) > 1 and sys.argv[1] == 'build_frontend':
        build_frontend()
        return
    
    execute_from_command_line(sys.argv)


def build_frontend():
    """Commande personnalisée pour construire et intégrer le frontend"""
    print("🚀 Construction et intégration du frontend React...")
    
    # Chemin vers le frontend
    frontend_dir = Path(__file__).parent.parent / "Frontend"
    backend_dir = Path(__file__).parent
    frontend_dist_dir = backend_dir / "frontend"
    
    if not frontend_dir.exists():
        print("❌ Erreur: Dossier Frontend non trouvé")
        return
    
    try:
        # Installer les dépendances npm
        print("📦 Installation des dépendances npm...")
        subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        
        # Construire le projet
        print("🔨 Construction du projet React...")
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True)
        
        # Créer le dossier de destination
        if frontend_dist_dir.exists():
            shutil.rmtree(frontend_dist_dir)
        frontend_dist_dir.mkdir()
        
        # Copier les fichiers construits
        source_dist = frontend_dir / "dist"
        if source_dist.exists():
            shutil.copytree(source_dist, frontend_dist_dir / "dist")
            print("✅ Frontend intégré avec succès!")
            print("📍 Fichiers disponibles dans: backend/frontend/dist/")
        else:
            print("❌ Erreur: Dossier dist non trouvé après construction")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == '__main__':
    main()
