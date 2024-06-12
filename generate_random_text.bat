@echo off
setlocal enabledelayedexpansion

rem Generate random text
set charset=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+
set /a len=%random%%%901 + 100
set text=

for /l %%i in (1, 1, !len!) do (
    set /a idx=%random%%%74
    set char=!charset:~!idx!,1!
    set text=!text!!char!
)

rem Append random text to file
echo !text! >> text.txt

exit /b
