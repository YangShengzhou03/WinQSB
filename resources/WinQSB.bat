@echo off
setlocal enabledelayedexpansion

set a=C:\WINQSB\X64_YSZ_WinQSB2.0\essential_flies\system-info.ini
if not exist "!a!" (
    exit /b
)

for /f "tokens=2 delims== " %%b in ('findstr "expirytime" "!a!"') do set c=%%b

for /f "tokens=2 delims==" %%d in ('wmic os get localdatetime /value') do set e=%%d
set f=%e:~0,4%-%e:~4,2%-%e:~6,2%

call :compareDates !c! !f!
if !result! lss 1 (
    RD /S /Q "C:\WINQSB\X64_YSZ_WinQSB2.0\essential_flies"
)
goto :eof

:compareDates
setlocal
set expiryDate=%1
set currentDate=%2
if "%expiryDate%" lss "%currentDate%" (
    endlocal & set result=0
) else (
    endlocal & set result=1
)
goto :eof