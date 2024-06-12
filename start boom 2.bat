@echo off
set "textfile=text.txt"

:start
start /B notepad %textfile%
timeout /t 1 /nobreak >nul
goto start

