# clarifai-image-recognition-skill
This skill enables Image Recognition for Mycroft based on Clarifai's free Image Recognition api.

#### Installation of skill:
* Download or Clone Git
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "clarifai-image-recognition-skill". (Clone does not require this step)
* Copy the clarifai-image-recognition-skill folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
- pip install clarifai

##### How To Use: 
- search image url {URL}

###### Note: To use your own API Key / Secret Key Pairs make the change in __init__.py.

## Current state

Working features:
* General model recognition 

Known issues:
* clarifai/rest/client.py needs to be modified with the following changes to work:
  Remove Lines: (Line Number: 2651) 
  
   "if platform.system() == 'Windows':
    homedir = os.environ.get('HOMEPATH', '.')
    else:"

TODO:
* None
