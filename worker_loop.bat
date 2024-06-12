@echo off
setlocal enabledelayedexpansion

rem Number of iterations each worker will perform
set num_iterations=%1

for /l %%i in (1, 1, !num_iterations!) do (
    call generate_random_text.bat
)

exit /b
