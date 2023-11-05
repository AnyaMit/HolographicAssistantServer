# Introduction 
This repo is part of a Workshop and may not be very useful if you are not currently in that workshop!

# Prepping VS Code
1. Open the Exercise1 folder in VS Code, do not attempt to complete this exercise with Holographicassistantserver folder open, these instructions will not work.
2. Make sure that your Python Environment selected in your VS Code Task Bar shows the .VENV python environment created previously. (This is only visible if a python file is currently open.)
   
![image](https://github.com/CameronVetter/HolographicAssistantServer/blob/main/images/venv.png?raw=true)
   
# Exercise 1
1. Open the OpenAI Platform website and login with your account: [https://platform.openai.com/](https://platform.openai.com/)
2. In your account profile "View API Keys"
3. Click Create new secret key
4. Copy the secret key and paste it into setupenv.py, there is a place for it in the variable "OPENAI_API_KEY"
5. In the VS Code toolbar select Run and Debug and select the Python: Flask profile
6. In your browser go to the swagger ui: [http://127.0.0.1:5000/swagger/](http://127.0.0.1:5000/swagger/)
7. Open the Chat POST and click Try it out
8. Modify the JSON body to have a prompt of "Are you alive?"
9. You should receive a "200" response with a response from the GPT model if you did not pause here and make you get this working before continuing.

# Exercise 2
1. Ask the model "What is your name?"
2. Ask the model "What is your purpose?"
3. Notice that the responses are lacking.  Lets fix that by changing the prompt to make it more interesting. In AI.py change these two variables:

`    prefix = """You are an anthropomorphic elephant. Your name is Emily. You are a personal assistant to a human. You were created by Cameron Vetter. You are witty and funny and sometimes snarky, and answer questions as best you can. When you do not know the answer to a question you will state that you don't know."""
    suffix = """Begin!"

    Question: {input}"""`

4. Change my name to yours, *You are the creator*
5. Ask the model the same two questions.  Notice that the responses make much more sense.
6. Experiment with the model ask it interesting questions, figure where it succeeds and where it fails.
7. Please **flip your status indicator** from Red to Green, signifying you are done with the core section.
   
# Exercise EXTRA TIME
1. Change the prompt to make chat bot match the personality you want it to have. Try things you think are odd or could never work, experiment and have fun. (Save this prompt to bring with you to future exercises.)

# Exercise EXTRA EXTRA TIME
1. Think of something specific to your life that you wish you had an assitant for. Attempt to adjust the prompt to get the chat bot to perform as closely as possible to this idea.