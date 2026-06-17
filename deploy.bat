@echo off
setlocal enabledelayedexpansion
cd /d %~dp0

echo ========================================
echo   Hugo Deploy to GitHub Pages
echo ========================================
echo.

rem ── Step 1: Build ────────────────────────
echo [1/3] Building site...
call hugo --minify
if %errorlevel% neq 0 (
    echo [FAIL] Hugo build failed!
    pause
    exit /b 1
)
echo       Build OK.
echo.

rem ── Commit message ───────────────────────
set /p MSG="Commit message (press Enter for default): "
if "%MSG%"=="" (
    for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set DT=%%I
    set "MSG=Deploy %DT:~0,8%-%DT:~8,4%"
)
echo       Using: %MSG%
echo.

rem ── Step 2: Push source to master ────────
echo [2/3] Pushing source to master...
git add -A
git commit -m "!MSG!" --allow-empty 2>&1
if %errorlevel% neq 0 (
    rem commit can fail if nothing to commit, that's OK
    echo       (nothing new to commit)
)
git push origin master 2>&1
if %errorlevel% neq 0 (
    echo [FAIL] Push to master failed! Check network / auth.
    pause
    exit /b 1
)
echo       Master OK.
echo.

rem ── Step 3: Push site to gh-pages ────────
echo [3/3] Pushing site to gh-pages...
cd public

rem     Ensure gh-pages branch exists
if not exist .git (
    echo       Initializing gh-pages repo...
    git init
    git checkout -b gh-pages
    git remote add origin https://github.com/g0nghu/g0nghu.github.io.git
)

rem     Fetch latest gh-pages first (avoid conflicts)
git fetch origin gh-pages 2>nul
git reset --soft origin/gh-pages 2>nul

git add -A
git commit -m "!MSG!" --allow-empty 2>&1
if %errorlevel% neq 0 (
    echo       (nothing new to commit)
)

git push origin gh-pages 2>&1
if %errorlevel% neq 0 (
    echo [FAIL] Push to gh-pages failed!
    echo       Try: git -c http.sslVerify=false push -f origin gh-pages
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
endlocal
