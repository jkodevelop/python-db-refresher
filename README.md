# Flask-RESTX [database experimentation and refresher guides]

This project is for testing, experiments and guide for using different database in python projects. 
**RESTX** part is the framework on top of **Flask** to provide swagger auto API documentation.
**Flask-JWT-Extended** authentication is included. 

note: **This project is NOT for production usage**

### prerequisite:
1. python 3
2. pip
3. optional but HIGHLY recommended: virtual environment (venv)
guide for setting up venv is included in `./pythonENV-setup-%OS%.md`
4. make sure to install all required packages: `pip install -r requirements.txt`

### usage:
1. look into GIT **branches** for different database type and usage examples
   - example: branch: `feature/mysql` is example of using MySQl

2. `py api.py` then go to http://127.0.0.1:5000/ to see the swagger UI with routes definition and usage.
note: depending on environment and name of python installed, the command `py` could be `python` instead. 

3. rename `SAMPLEconfig.ini` to `config.ini` and change the settings based on environment

### neo4j specific

1. use `.\_neo4j_scripts_docs\db-data-setup.txt` to insert test data for use in projects

2. `.\_neo4j_scripts_docs\neo4j-cypher.md` have **cypher** examples