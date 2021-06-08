Start with python3, these steps show how to create and use virtual environment for python.
This is useful for isolating projects from each other since there are specific version of packages needed in a specific project.

note: This documentation is based on Windows OS env

##### prereq
1. install python 3+ 
(make sure the executable is set in system path to make it easier to use, this document assumes install python is linked in system path by name **py**)

### steps

1. create virtualEnvironment using built-in **venv**
- use `env` as the name of folder **venv**

```bash
py -m venv env
```
A folder named `env` will be created. This can be named based on the command above.


2. using/activating the virtual environment
- from previous step `env` is the folder where the activate script in
```bash
.\env\Scripts\activate
```
Once activated the python module being installed will be tide to this project and env. 

3. deactivate the virtual environment
- from inside an activated environment, this command will be available
```bash
deactivate
````
#### troubleshooting
###### 1 - problems with virtual environment and packages
After activating virtual environment, if running `deactivate` doesn't work. Should check if there is something wrong with the environment. Easiest way to check is if running `pip3 freeze > requirements.txt` and see a lot of unknown or unused python packages. There might be virtual environment corruption
*solution 1*: delete the virtual environment `env` and reinstate it `py -m venv env`
*solution 2*: check python system path, make sure the OS is running python3. Sometimes the system might have multiple version of python running. pip module gets kind of confused

### pip
pip used to manage and install python libraries. Helpful commands. Assumes package list name to be `requirements.txt` for example commands below


Once **venv** is activated list out all packages under this project
```bash
pip3 freeze
```

save package dependency list into a file: `requirements.txt`
```bash
pip3 freeze > requirements.txt
```

install packages in file: `requirements.txt`
```bash
pip3 install -r requirements.txt
```
