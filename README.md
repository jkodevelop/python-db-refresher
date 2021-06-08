# Flask-RESTX python starter [2021]
This repo is a simple starter for **Flask** developement, this provides a simple RESTful-API server.
**RESTX** part is the framework on top of **Flask** to provide swagger auto API documentation.

note: **This project is NOT production ready!** For production deployment please follow the official guide https://flask.palletsprojects.com/en/2.0.x/deploying/

```

Please fork the project to start a new project

```

### prerequisite:
1. python 3
2. pip
3. optional but HIGHLY recommended: virtual environment (venv)
guide for setting up venv is included in `./pythonENV-setup-%OS%.md`
4. make sure to install all required packages: `pip install -r requirements.txt`

## usage: Development
`py api.py` then go to http://127.0.0.1:5000/ to see the swagger UI with routes definition and usage.
note: depending on environment and name of python installed, the command `py` could be `python` instead. 

For development these package(s) are in place:
- Flask-RESTX
- Flask-JWT-Extended

Example/Reference routes added:
1. get/post with parameters and documentation decorators
2. authorization example
3. custom python decorator: `token_required()` for checking token auth for protected paths

Please go through git history for steps on what was changed and guide for functionality added and reorganization changes.

optional todos: 
- loggout API
- refresh/expire/customize JWT token

---
## further reading: Documentations
- https://flask-restx.readthedocs.io/en/latest/quickstart.html
- https://flask.palletsprojects.com/en/2.0.x/
- https://flask-jwt-extended.readthedocs.io/en/stable/