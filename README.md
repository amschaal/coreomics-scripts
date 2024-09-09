## Description
This repository will contain scripts that may be useful for doing various tasks using submission system exports, or the API.

## Installation
If you plan on using these scripts locally, you'll need to install a couple of libraries as well as potentially jupyter for using the ipynb files.

### Create python virtual environment in current directory under ".venv"
```
python3 -m venv .venv
source .venv/bin/activate
```

### Install requirements.  If planning to use jupyter lab for ipynb files, make sure it is uncommented
```
pip install -r requirements.txt 
```

### If jupyter lab is installed, launch it and open the URL given in the console.
```
jupyter lab
```

### If running regular python scripts, ensure the virual enviroment is activated first:
```
source .venv/bin/activate
python analyse_sample_count.py
```