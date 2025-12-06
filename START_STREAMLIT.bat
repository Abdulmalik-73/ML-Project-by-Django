@echo off
echo ============================================================
echo    Starting Streamlit UI
echo ============================================================
echo.
echo Installing Streamlit if needed...
pip install streamlit --quiet
echo.
echo Starting Streamlit...
streamlit run streamlit.py
pause
