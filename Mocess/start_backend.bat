@echo off
echo ========================================
echo   MOCESS Backend - Django Server
echo ========================================
echo.

cd backend

echo Activating virtual environment...
call venv\Scripts\Activate.ps1

echo.
echo Starting Django development server...
echo Backend will be available at: https://aide-deploiement.vercel.app
echo Admin interface: https://aide-deploiement.vercel.app/admin
echo API endpoints: https://aide-deploiement.vercel.app/api/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause 