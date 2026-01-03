@echo off
REM Script to create ZIP file for Overleaf upload
REM This includes all necessary files for your paper

echo Creating paper.zip for Overleaf...

cd paper

REM Check if 7z is available
where 7z >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    7z a paper.zip main.tex references.bib output1.png output2.png output3.png output4.png output5.png output6.png output7.png
    echo.
    echo ✓ paper.zip created successfully using 7z!
    goto :end
)

REM Check if tar is available (Windows 10+)
where tar >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    tar -a -cf paper.zip main.tex references.bib output1.png output2.png output3.png output4.png output5.png output6.png output7.png
    echo.
    echo ✓ paper.zip created successfully using tar!
    goto :end
)

REM If no compression tool available
echo.
echo ✗ No compression tool found (7z or tar)
echo.
echo Please manually create a ZIP file with:
echo   - main.tex
echo   - references.bib
echo   - output1.png through output7.png
echo.
echo Then upload to https://www.overleaf.com/
echo.

:end
pause
