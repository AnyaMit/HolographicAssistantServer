# Introduction 
This repo is part of a Workshop and may not be very useful if you are not currently in that workshop!

# Prerequisites
**Windows Recommended (OS X should work but it is untested)**
- Visual Studio Code (https://code.visualstudio.com/download)
- Unity 2022.3 LTS Version Free version (https://unity.com/download)
- Valid Open AI Subscription or Azure Open AI Preview Access (https://openai.com/) 
- Python 3.10 (https://www.python.org/downloads/release/python-31011/)
- Looking Glass Bridge 2.3.2 (https://lookingglassfactory.com/software/looking-glass-bridge)


# Getting Started
1. Clone this repo. 
2. This folder contains the completed solution, **DO NOT** start here, but use this if you do not complete the exercises so you can continue.

# Prepping VS Code
1. Make sure the VS Code Extensions Pylance and Python are installed.  Restart VS Code after installing them.
2. Open VS Code in the root folder of this project.
3. Open example-setupenv.py, you may need to select python 3.10 as the interpreter.
4. Select Run and Debug in VS Code, Select Python Current File, Select the Green play button.

![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/runcurrentfile.png?raw=true)

5. This should execute correctly and do nothing, and open up a terminal.
6. In the Terminal window create a Python environment. `python -m venv .venv`
7. If successful you will see a new folder ".venv".
8. Change your current python environment to ".venv", the plugin may offer to do this for you, but if not select the python environment from the toolbar:

![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/venv.png?raw=true)

9. Close the terminal window (with the trash icon and not the x icon).
10. Run Current file again, this time you will notice it runs in (.venv)
11. Install the prerequisites with the command `pip install -r .\requirements.txt`
12. Once the install completes you are ready. Close VS Code.
   
# Exercises
1. Open the [Exercise 1 folder](https://github.com/CameronVetter/HolographicAssistantServer/tree/main/Exercise1) in Github and complete that exercise.
2. **WHEN INSTRUCTED** Open [Exercise 2 folder](https://github.com/CameronVetter/HolographicAssistantServer/tree/main/Exercise2) in Github and complete the exercise.

# Help we are moving on and I'm not done!
**Remember** If you do not complete Exercise 2, This folder contains the completed exercise!
1. Open this folder in VS Code
2. Add the keys into setupenv.py (as instructed in the exercises) 
3. Run the flask server.  
4. Verify you are able to open the swagger ui here: http://127.0.0.1:5000/swagger/ 