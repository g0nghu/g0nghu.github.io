@echo off
cd /d %~dp0

echo ========================================
echo   Hugo Deploy to GitHub Pages
echo ========================================
echo.

echo [1/3] Building site...
call hugo --minify
if errorlevel 1 (
    echo [FAIL] Hugo build failed!
    pause
    exit /b 1
)
echo       Build OK.
echo.

set /p MSG="Commit message (press Enter for default): "
if "%MSG%"=="" set MSG=Deploy
echo       Using: %MSG%
echo.

echo [2/3] Pushing source to master...
git add -A
git commit -m "%MSG%" --allow-empty
git push origin master
if errorlevel 1 (
    echo [FAIL] Push to master failed!
    pause
    exit /b 1
)
echo       Master OK.
echo.

echo [3/3] Pushing site to gh-pages...
cd public

if not exist .git (
    echo       First time: setting up gh-pages repo...
    git init
    git checkout -b gh-pages
    git remote add origin https://github.com/g0nghu/g0nghu.github.io.git
)

git add -A
git commit -m "%MSG%" --allow-empty
git push -f origin gh-pages
if errorlevel 1 (
    echo [FAIL] Push to gh-pages failed!
    echo       Check network connection to GitHub.
    cd ..
    pause
    exit /b 1
)

cd ..
echo       gh-pages OK.
echo.

echo ========================================
echo   Done! https://g0nghu.github.io/
echo ========================================
pause