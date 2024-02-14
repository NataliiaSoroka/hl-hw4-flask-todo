# Development environment setup

```sh
sqlite3 -version # Check that you have sqlite installed
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
flask db upgrade
flask run
```
