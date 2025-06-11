## Deploy worldbank app to Heroku
1. Create a Python venv
    ```bash
    python3 -m venv worldbankvenv
    source worldbankenv/bin/activate
    ```
2. Install packages
   ```bash
   pip install flask pandas plotly gunicorn==23.0.0
   pip freeze > requirements.txt
   ```
3. Install and login Heroku
   ```bash
   curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
   heroku login
   ```
4. Create a `Procfile` and write:
   ```
   web: gunicorn worldbank:app
   ```
5. Create a Heroku app
   ```bash
   heroku create my-worldbank-app
   ```
6. Create git and push to heroku
   ```
   git init
   git add .
   git commit -m "first commit"
   git push heroku main
   ```
7. Check the app at `https://my-worldbank-app-<...>.herokuapp.com/ `