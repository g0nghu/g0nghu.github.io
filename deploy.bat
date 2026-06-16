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
echo       OK.

echo [2/3] Push source to master...
set /p MSG="Commit message (default: Deploy): "
if "%MSG%"=="" set MSG=Deploy
git add -A
git commit -m "%MSG%" --allow-empty --quiet
git -c http.sslVerify=false push origin master
if %errorlevel% neq 0 (
    echo Push source failed!
    pause
    exit /b 1
)
echo       OK.

echo [3/3] Push site to gh-pages...
cd public
if not exist .git (
    git init
    git checkout -b gh-pages
    git remote add origin https://github.com/g0nghu/g0nghu.github.io.git
)
git add -A
git commit -m "%MSG%" --allow-empty --quiet
git -c http.sslVerify=false push -f origin gh-pages
cd ..
echo       OK.

echo.
echo Done! https://g0nghu.github.io/
pause
