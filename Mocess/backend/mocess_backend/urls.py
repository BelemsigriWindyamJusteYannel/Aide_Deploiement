"""
URL configuration for mocess_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import FileResponse, HttpResponse
import os

def home_page(request):
    """Page d'accueil - sert directement le frontend React"""
    return serve_react_app(request)

def serve_react_app(request):
    """Vue pour servir l'application React"""
    file_path = os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'index.html')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Corriger les chemins des assets pour l'accueil
        content = content.replace('./assets/', '/assets/')
        return HttpResponse(content, content_type='text/html')
    except FileNotFoundError:
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MOCESS - React App</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(135deg, #064e3b 0%, #0f766e 50%, #166534 100%); color: white; }
                .container { max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; text-align: center; }
                h1 { color: #4ade80; }
                .error { background: #ef4444; padding: 15px; border-radius: 10px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>⚛️ Frontend React MOCESS</h1>
                <div class="error">
                    ❌ Le fichier index.html du frontend React n'a pas été trouvé.<br>
                    Veuillez construire le frontend avec : npm run build
                </div>
                <p><a href="/" style="color: #4ade80;">← Retour à l'accueil</a></p>
            </div>
        </body>
        </html>
        """)

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Ajouter les URLs pour les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Servir les fichiers statiques du frontend React
    urlpatterns += static('/assets/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'assets'))
    # Servir les images des projets
    urlpatterns += static('/projects/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'projects'))
    urlpatterns += static('/team/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'team'))
    urlpatterns += static('/partenaires/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'partenaires'))
    urlpatterns += static('/logos/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'logos'))
    urlpatterns += static('/actualites/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'actualites'))
    urlpatterns += static('/evenements/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'evenements'))
    urlpatterns += static('/universites/', document_root=os.path.join(settings.BASE_DIR, 'frontend', 'dist', 'universites'))
