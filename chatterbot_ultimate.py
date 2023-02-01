import os
import openai
import time
import wolframalpha
import getpass
from steamship import Steamship
Wolfram_Key = getpass.getpass("Enter your Wolfram Alpha API Key: ")
openai.api_key = getpass.getpass("Enter your OpenAI API Key: ")
steamship_api_key = getpass.getpass("Enter your Steamship API key: ")
os.system("clear")
client=wolframalpha.Client(Wolfram_Key)
pkg = Steamship.use("chatbot-engine", api_key = steamship_api_key)
class ChatterBot:
  def respond_to(myprompt):
    output=[]
    result=openai.Completion.create(model="text-davinci-003",prompt=myprompt,max_tokens=1024,temperature=0.3)
    for i in result.choices[0].text:
      output.append(i)
    for i in range(2,len(output)):
      if i!=len(output):
        print(output[i],end="")
      else:
        print(output[i])
  def program(myprompt):
    output=[]
    result=openai.Completion.create(model="code-davinci-002",prompt="# "+myprompt+" in python",max_tokens=1024,temperature=0.3)
    for i in result.choices[0].text:
      output.append(i)
    for i in range(2,len(output)):
      if i!=len(output):
        print(output[i],end="")
      else:
        print(output[i])
  def chatbot(personality):
    username = input("What is your username? ")
    os.system("clear")
    if personality != "smart" and personality != "rickroller" and personality != "programmer":
      userinput = input(username+": ")
      resp = pkg.invoke("generate",input = userinput,personality = personality)
      print("\nChatterBot: "+resp+"\n")
      while userinput != "exit":
        userinput = input(username+": ")
        resp = pkg.invoke("generate",input = userinput,personality = personality)
        print("\nChatterBot: "+resp+"\n")
      else:
        os.system("clear")
        ChatterBot.main()
    if personality == "knowledgeable":
      userinput = input(username+": ")
      if userinput != "exit":
        print()
        print("ChatterBot: ",end="")
        ChatterBot.respond_to("Simulate a friendly chatbot and don't change the prompts. Here is the first prompt: "+userinput)
        print()
      else:
        os.system("clear")
        ChatterBot.main()
      while True:
        print()
        userinput = input(username+": ")
        if userinput != "exit":
          print()
          print("ChatterBot: ",end="")
          ChatterBot.respond_to(userinput)
          print()
        else:
          os.system("clear")
          ChatterBot.main()
    if personality == "smart":
      while True:
        query = input(username+": ")
        if query != "exit":
          print()
          res = client.query(query)
          answer = next(res.results).text
          print("ChatterBot: "+answer)
          print()
        else:
          os.system("clear")
          ChatterBot.main()
    if personality == "rickroller":
      lyric = 0
      while True:
        userinput = input(username+": ")
        if userinput != "exit":
          print()
          while True:
            if lyric == 0:
              print("ChatterBot: Never gonna give you up")
              print()
              lyric += 1
            userinput = input(username+": ")
            if userinput != "exit":
              print()
              if lyric == 1:
                print("ChatterBot: Never gonna let you down")
                print()
                lyric += 1
              userinput = input(username+": ")
              if userinput!= "exit":
                print()
                if lyric == 2:
                  print("ChatterBot: Never gonna run around and desert you")
                  print()
                  lyric += 1
                userinput = input(username+": ")
                if userinput != "exit":
                  print()
                  if lyric == 3:
                    print("ChatterBot: Never gonna make you cry")
                    print()
                    lyric += 1
                  userinput = input(username+": ")
                  if userinput!= "exit":
                    print()
                    if lyric == 4:
                      print("ChatterBot: Never gonna say goodbye")
                      print()
                      lyric += 1
                    userinput = input(username+": ")
                    if userinput!= "exit":
                      print()
                      if lyric == 5:
                        print("ChatterBot: Never gonna tell a lie and hurt you")
                        print()
                    else:
                      os.system("clear")
                      ChatterBot.main()
                  else:
                    os.system("clear")
                    ChatterBot.main()
                else:
                  os.system("clear")
                  ChatterBot.main()
              else:
                os.system("clear")
                ChatterBot.main()
              userinput = input(username+": ")
              print()
              lyric = 0
            else:
              os.system("clear")
              ChatterBot.main()
    if personality == "programmer":
      while True:
        userinput = input(username+": ")
        if userinput!= "exit":
          print()
          print("ChatterBot: ")
          print()
          ChatterBot.program(userinput)
          print()
          print()
        else:
          os.system("clear")
          ChatterBot.main()
  def main():
    print("Welcome to ChatterBot")
    time.sleep(1.2)
    print("Made by the legendary: ")
    time.sleep(1.2)
    print("zameerlovesmath")
    time.sleep(1.2)
    os.system("clear")
    personality = input("What personality should your chatbot have? ")
    os.system("clear")
    ChatterBot.chatbot(personality)
ChatterBot.main()