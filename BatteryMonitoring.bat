@echo off
cd ./Windows-BatteryMonitoring

:loop
python new_version.py
timeout /t 900
goto loop
