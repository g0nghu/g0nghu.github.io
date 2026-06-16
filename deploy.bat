@echo off
cd /d %~dp0

echo === Hugo Deploy ===
echo [1/3] Building...
call hugo --minify
if %errorlevel% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)
echo       Build OK.

echo [2/3] Pushing...
set /p MSG="Commit message (default: Deploy): "
if "%MSG%"=="" set MSG=Deploy
git add -A
git commit -m "%MSG%" --allow-empty
git -c http.sslVerify=false push origin master
if %errorlevel% neq 0 (
    echo Push failed!
    pause
    exit /b 1
)
echo       Push OK.

echo [3/3] Monitoring Actions...
python deploy_monitor.py
pause
