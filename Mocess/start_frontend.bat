@echo off
echo ========================================
echo   MOCESS Frontend - React Server
echo ========================================
echo.

cd Frontend

echo Installing dependencies (if needed)...
call npm install

echo.
echo Starting React development server...
echo Frontend will be available at: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo.

npm run dev

pause 