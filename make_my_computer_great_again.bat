@echo off
title Windows One-Shot Program Installer
color 0A

echo ==========================================
echo      MAKE MY COMPUTER GREAT AGAIN
echo ==========================================
echo.
echo Checking for Python...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3 from the Microsoft Store or python.org.
    echo.
    pause
    exit /b
)

echo Python found. Checking for Streamlit...
python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo Streamlit not found. Installing...
    pip install streamlit
    if %errorlevel% neq 0 (
        echo Failed to install Streamlit. Please check your internet connection.
        pause
        exit /b
    )
)

echo.
echo Launching Installer App...
echo.

streamlit run app.py

pause
