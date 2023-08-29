import g4f
import requests
import json

messages = []  # 存储消息的列表
while True:
    content=""
    user_input = input("You: ")
    
    messages.append({"role": "system", "content": "你正在与一位翻譯的专家交谈。"},)  # 将消息添加到列表
    if user_input:
        messages.append({"role": "user", "content": user_input})  # 将消息添加到列表
        # Set with provider
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            provider=g4f.Provider.DeepAi,
            messages=messages,
            stream=True,
        )
        for message in response:
            print(message)
            content+=message
       
        messages.append({"role": "assistant", "content": content})
        print(messages)
        print('==========================')
        print(content)
