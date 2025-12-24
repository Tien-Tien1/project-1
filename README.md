python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install selenium pytest
git status
git add .
git commit -m "initial project "
git push

# to run test casses 
```
pytest .\test_login1.py
```
