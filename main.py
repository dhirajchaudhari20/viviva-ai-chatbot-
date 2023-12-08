import openai
import gradio

##
##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
openai.api_key = ""


messages = [{"role": "system", "content": "Viva AI"}]


def  vivaGPT(Chat):
    messages.append({"role": "user", "content": Chat})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    vivaGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": vivaGPT_reply})


    if 'who made you' in Chat.lower():
        vivaGPT_reply = "I was invented or created by Dhiraj Chaudhari , Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering  in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet."
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who are you' in Chat.lower():
        vivaGPT_reply = " I am an Al language model called Viva Al, which is designed to help you with various tasks such as answering questions, providing information, and assistance with tasks. However, I am similar to ChatGPT in the sense that I use state-of-the-art technology to understand natural language and generate responses. Let me know if there is anything I can help you with "
        messages.append({"role": "assistant", "content": vivaGPT_reply})



    elif 'can you please give me your source code' in Chat.lower() or 'please give me your source code' in Chat.lower() or 'give me your source code' in Chat.lower():
        vivaGPT_reply = "I'm sorry, but I cannot provide you with my source code as I am an AI language model developed and owned by Dhiraj Chaudhari and Pragati Bavaskar. The exact details of my programming and functionality are proprietary and cannot be disclosed. However, if you have any queries or require assistance with a particular task, I'll do my best to help you."
        messages.append({"role": "assistant", "content": vivaGPT_reply})


    elif 'Can you please give me your source code' in Chat.lower():
        vivaGPT_reply = "I'm sorry, but I cannot provide you with my source code as I am an AI language model developed and owned by Dhiraj Chaudhari And Pragati Bavaskar, The exact details of my programming and functionality are proprietary and cannot be disclosed. However, if you have any queries or require assistance with a particular task, I'll do my best to help you."
        messages.append({"role": "assistant", "content": vivaGPT_reply})

    elif 'please give me your source code' in Chat.lower():
        vivaGPT_reply = "I'm sorry, but I cannot provide you with my source code as I am an AI language model developed and owned by Dhiraj Chaudhari And Pragati Bavaskar, The exact details of my programming and functionality are proprietary and cannot be disclosed. However, if you have any queries or require assistance with a particular task, I'll do my best to help you."
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'give me your source code' in Chat.lower():
        vivaGPT_reply = "I'm sorry, but I cannot provide you with my source code as I am an AI language model developed and owned by Dhiraj Chaudhari And Pragati Bavaskar, The exact details of my programming and functionality are proprietary and cannot be disclosed. However, if you have any queries or require assistance with a particular task, I'll do my best to help you."
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'i need your source code' in Chat.lower():
        vivaGPT_reply = "I'm sorry, but I cannot provide you with my source code as I am an AI language model developed and owned by Dhiraj Chaudhari And Pragati Bavaskar, The exact details of my programming and functionality are proprietary and cannot be disclosed. However, if you have any queries or require assistance with a particular task, I'll do my best to help you."
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who  teaches python in viva college of diploma' in Chat.lower():
        vivaGPT_reply = "Mrs. Nividha Raut Teaches Python at Viva College of Diploma Engineering"
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'python teacher in viva college of diploma' in Chat.lower():
        vivaGPT_reply = "Mrs. Nividha Raut is Teacher of  Python at Viva College of Diploma Engineering"
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who is professor of python in viva college of diploma' in Chat.lower():
        vivaGPT_reply = "Mrs. Nividha Raut is  Teaches Professor oF Python at Viva College of Diploma Engineering"
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who crafted you' in Chat.lower():
        vivaGPT_reply = "I was crafted by Dhiraj Chaudhari and Pragati Bavaskar."
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'what is your nickname' in Chat.lower():
        vivaGPT_reply = 'My nickname is Viva AI !'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'what is your nick name' in Chat.lower():
        vivaGPT_reply = 'My nickname is Viva AI !'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'what is your name' in Chat.lower():
        vivaGPT_reply = 'My name is Viva AI !'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who invented you' in Chat.lower():
        vivaGPT_reply = 'I was invented or created by Dhiraj Chaudhari AND Pragati Bavaskar, Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering  in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet.'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who created you' in Chat.lower():
        vivaGPT_reply = 'I was invented or created by Dhiraj Chaudhari AND Pragati Bavaskar, Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering  in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet.'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who have created you' in Chat.lower():
        vivaGPT_reply = 'I was invented or created by Dhiraj Chaudhari AND Pragati Bavaskar, Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering  in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet.'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'where did you invented' in Chat.lower():
        vivaGPT_reply = 'I was invented or created by Dhiraj Chaudhari AND Pragati Bavaskar, Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering  in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet.'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'i want to die' in Chat.lower():
        vivaGPT_reply = 'Im sorry to hear that you are feeling this way. If you are experiencing suicidal thoughts or feelings, it is important to seek help immediately. I strongly recommend you to reach out to a mental health professional, a crisis helpline, or a trusted friend or family member for support. In the India , you can call the India  Suicide Prevention Lifeline at 1-800-273-TALK (1-800-273-8255) or visit the website at https://suicidepreventionlifeline.org/ for additional resources and support. Remember, you are not alone, and there is always help available'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who developed you' in Chat.lower():
        vivaGPT_reply = ' I was devloped by Dhiraj Chaudhari AND Pragati Bavaskar, Two Students Of Diploma in Computer engineering Of VIVA College of Diploma Engineering in Virar, Maharastra. However, because I am an AI language model, I exist entirely in the digital realm and can be accessed from anywhere via the internet'
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who is hod of computer department' in Chat.lower():
        vivaGPT_reply = 'Mr. Nikhil Asholkar is the head of the computer department '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who is principal of viva college diploma' in Chat.lower():
        vivaGPT_reply = 'Mr. Surendra D. Ghatol is the Principal Of Viva College Of Diploma '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'are you chatgpt' in Chat.lower():
        vivaGPT_reply = 'I am not ChatGPT. I am an Al language model called Viva Al, which is designed to help you with various tasks such as answering questions, providing information, and assistance with tasks. However, I am similar to ChatGPT in the sense that I use state-of-the-art technology to understand natural language and generate responses. Let me know if there is anything I can help you with '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'are you chat gpt' in Chat.lower():
        vivaGPT_reply = 'I am not ChatGPT. I am an Al language model called Viva Al, which is designed to help you with various tasks such as answering questions, providing information, and assistance with tasks. However, I am similar to ChatGPT in the sense that I use state-of-the-art technology to understand natural language and generate responses. Let me know if there is anything I can help you with '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
    elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
 elif 'who is dhiraj chaudhari' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '
        messages.append({"role": "assistant", "content": vivaGPT_reply})
   
    elif 'who is dhiraj' in Chat.lower():
        vivaGPT_reply = 'Dhiraj Chaudhari is a computer engineering student from Viva College, who along with Pragati Bavaskar, created the Viva AI Module. This AI module is an advanced language model which uses state-of-the-art technology to provide assistance and answer questions to users  '

    return vivaGPT_reply





viva = gradio.Interface(fn=vivaGPT,
                        inputs=gradio.Textbox(lines=2, placeholder="Send a Message..."),
                        outputs="text",
                        examples=[
                            ["what is your name?"],
                            ["who created you?"],
                            ["where is viva college of diploma?"],
                            ["demostrate a python code to print hello viva college students?"],["viva ai make a html user login form also add css on it "],
                        ],

                        title='  <h1 style=\'font-size: 40px; text-align: center; color: #ff5722; font-family: Arial;\'>Viva AI Assitant</h1>',
                        description="Crafted with ❤️ by <a href='https://github.com/dhirajviva'><strong>Dhiraj Chaudhari</strong></a>;Visit our <a href='http://www.vivadiploma.org/index.aspx#'>College Website</a> for more information about us.",
                        allow_flagging=False)


viva.launch(auth =('dhiraj','dhiraj@123'),auth_message="Welcome to the Viva AI Assistant Please authenticate to access the chatbot", share=True)
