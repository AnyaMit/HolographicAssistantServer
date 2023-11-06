# Introduction 
This repo is part of a Workshop and may not be very useful if you are not currently in that workshop!

# Prepping VS Code
1. Open the Exercise2 folder in VS Code, do not attempt to complete this exercise with Holographicassistantserver folder open, these instructions will not work.
2. Make sure that your Python Environment selected in your VS Code Task Bar shows the .VENV python environment created previously. (This is only visible if a python file is currently open.)
   
![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/venv.png?raw=true)

3. You will have to navigate to python.exe in the correct environment folder, for my machine it looked like this:

![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/selectvenv.png?raw=true)

# Part 1
1. Lets get our first tool working.  GPT is very bad at math, so let's give it a tool to help it perform math.
2. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
4. Try the "Post Chat" method, and send the message "What is 1000 + 1234?".  Notice how it fails to get the right answer.
5. Open ai.py, replace the line `tools = []` with this code:

```
    import aitools
    tools = aitools.get_tools()
```
3. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
4. Try the "Post Chat" method, and send the message "What is 1000 + 1234?"
5. Try a much more complicated math problem "What is the square root of 300?"


