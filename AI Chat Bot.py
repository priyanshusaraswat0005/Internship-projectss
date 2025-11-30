import google.generativeai as genai 
import streamlit as st

key = "******************"

print(key)

genai.configure(api_key=key)
while True:
    user = input("What do you want To Search :   \n  Type 'exit' to close: ")

    if user.lower() == "exit":
        print("bye bye")
        break

    response = Model.generate_content(user)
    print("bot:", response.text)