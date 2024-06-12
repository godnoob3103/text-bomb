@echo off

rem Number of worker threads
set num_threads=10

rem Number of iterations per worker
set num_iterations=100

for /l %%i in (1, 1, %num_threads%) do (
    start "Thread %%i" cmd /c worker_loop.bat %num_iterations%
)

exit /b
