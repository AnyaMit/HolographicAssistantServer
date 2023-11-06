# Introduction 
This repo is part of a Workshop and may not be very useful if you are not currently in that workshop!

# Prepping VS Code
1. Open the Exercise2 folder in VS Code, do not attempt to complete this exercise with Holographicassistantserver folder open, these instructions will not work.
2. Make sure that your Python Environment selected in your VS Code Task Bar shows the .VENV python environment created previously. (This is only visible if a python file is currently open.)
   
![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/venv.png?raw=true)

3. You will have to navigate to python.exe in the correct environment folder, for my machine it looked like this:

![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/selectvenv.png?raw=true)

# Part 1
1. Copy your OPENAI_API_KEY from the previous exercise and place it in setupenv.py
2. Lets get our first tool working.  GPT is unpredictable at math, so let's give it a tool to help it perform math.
3. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
4. Open ai.py, replace the line `tools = []` with this code:

```
    import aitools
    tools = aitools.get_tools()
```

5. Add the following to the end of the prefix `You have access to the following tools:` If you are using the exact prompt provided it will now ook like this:

```
    prefix = """You are an anthropomorphic elephant. Your name is Emily. You are a personal assistant to a human. You were created by Cameron Vetter. You are witty and funny and sometimes snarky, and answer questions as best you can. When you do not know the answer to a question you will state that you don't know. You have access to the following tools:"""
```

6. Run the flask server and open the swagger ui: http://127.0.0.1:5000/swagger/
7. Try the "Post Chat" method, and send the message "What is 1000 + 1234?"
8. Try a much more complicated math problem "What is the square root of 300?"


