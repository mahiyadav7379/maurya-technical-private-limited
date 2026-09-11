@echo off
title Pushing Maurya Technical to GitHub
color 0A
echo ========================================================
echo    Maurya Technical Private Limited - GitHub Push
echo ========================================================
echo.
cd /d "c:\Users\simiy_otrc7ib\Desktop\mauraya"
echo Current directory: %CD%
echo.
echo Running git push -u origin main...
echo (If a browser window opens, please click 'Authorize' to login to GitHub)
echo.
"C:\Program Files\Git\cmd\git.exe" push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================================
    echo  SUCCESS! Your code is now live on GitHub!
    echo  https://github.com/mahiyadav7379/maurya-technical-private-limited
    echo ========================================================
) else (
    echo.
    echo If login was required, please follow the prompt or use a GitHub Token.
)
echo.
pause
