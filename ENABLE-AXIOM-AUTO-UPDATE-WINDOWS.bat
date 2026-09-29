@echo off
setlocal
set "AXIOM_PROJECT=%~dp0visionstudio"
set "AXIOM_FEED=https://raw.githubusercontent.com/balltro/AxiomVision-Releases/main/updates.json"

if not exist "%AXIOM_PROJECT%\scripts\visionstudio_updater.py" (
  echo Axiom Vision v0.18.0 was not found beside this file.
  echo Place this BAT next to RUN-SETUP-WINDOWS.bat in the installed folder.
  pause
  exit /b 1
)
if not exist "%AXIOM_PROJECT%\.venv\Scripts\python.exe" (
  echo Run RUN-SETUP-WINDOWS.bat first, then run this file again.
  pause
  exit /b 1
)
if not exist "%AXIOM_PROJECT%\controller" mkdir "%AXIOM_PROJECT%\controller"
> "%AXIOM_PROJECT%\controller\updates.json" echo {"feed_url":"%AXIOM_FEED%"}
echo Signed update feed configured.
"%AXIOM_PROJECT%\.venv\Scripts\python.exe" "%AXIOM_PROJECT%\scripts\visionstudio_updater.py" check
set "AXIOM_RESULT=%ERRORLEVEL%"
if not "%AXIOM_RESULT%"=="0" echo Update check failed; the installed game runtime was not changed.
pause
exit /b %AXIOM_RESULT%
