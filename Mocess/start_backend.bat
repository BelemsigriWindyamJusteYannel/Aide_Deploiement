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
echo Backend will be available at: http://localhost:8000
echo Admin interface: http://localhost:8000/admin
echo API endpoints: http://localhost:8000/api/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause 