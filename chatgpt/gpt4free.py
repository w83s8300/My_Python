import openai

openai.api_key = ""
openai.api_base = "http://localhost:1337"
messages = []  # 存储消息的列表

def main():
    content=""
    contentstr=""
    user_input = input("You: ")
    messages.append({"role": "system", "content": "你正在与一位翻譯的专家交谈。"},)  # 将消息添加到列表
    if user_input:
        messages.append({"role": "user", "content": "幫我翻譯[0.00s -> 3.00s]  Uh, what is this? More? I have to sneeze.[10.00s -> 12.00s]  Did you just call me an A.I.?[13.00s -> 17.00s]  Wow, this A.I. is so realistic. I feel like I'm really talking to Gura.[18.00s -> 20.00s]  How do I prove I'm not an A.I.?[21.00s -> 23.00s]  Ask me a question only Gura would know.[25.00s -> 29.00s]  Two times two is four. Or fish if you put them together the right way.[30.00s -> 35.00s]  Fake Gura wouldn't know that. Exactly, which is why I'm real Gura.[36.00s -> 37.00s]  I'm not an A.I.[44.00s -> 47.00s]  Real Gura wouldn't know what? Real Gura wouldn't know what?[50.00s -> 52.00s]  That two times two is four?[53.00s -> 55.00s]  Exactly what an A.I. would say. No.[56.00s -> 59.00s]  Real Gura can't do two times two is four.[61.00s -> 64.00s]  Okay, ask me another question then.[65.00s -> 66.00s]  Ah, wait.[69.00s -> 71.00s]  Five times five is twenty five.[72.00s -> 76.00s]  Five times five is twenty five. Five, ten, fifteen, twenty, twenty five. Boom.[77.00s -> 78.00s]  Is Kira cute? Yes.[79.00s -> 83.00s]  How tall are you in bananas? Uh, I don't know. I don't know that.[85.00s -> 88.00s]  Shoe size? None of your business.[90.00s -> 93.00s]  She's real. See! I am real. I am real![95.00s -> 96.00s]  Why am I arguing?[98.00s -> 100.00s]  Nine plus ten, twenty one.[102.00s -> 104.00s]  Don't quiz me while I'm working. I changed my mind. I changed my mind.[111.00s -> 113.00s]  How do I know you're real?[116.00s -> 118.00s]  Whoa, whoa, whoa, whoa, wait a minute.[120.00s -> 122.00s]  How do I know you're actually who you are?[124.00s -> 127.00s]  We passed the cap challenge. Are you sure?[136.00s -> 137.00s]  I'm Gar Gura.[137.00s -> 138.00s]  Wombus.[138.00s -> 139.00s]  Bumbo.[139.00s -> 140.00s]  And me how-[150.00s -> 151.00s]  Achoo!"})  # 将消息添加到列表
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )

        if isinstance(chat_completion, dict):
            # not stream
            print(chat_completion.choices[0].message.content)
        else:
            # stream
            for token in chat_completion:
                content = token["choices"][0]["delta"].get("content")
                if content != None:
                    print(content, end="", flush=True)
                    contentstr+=content
        messages.append({"role": "assistant", "content": contentstr})
        print('==========================')
        print(messages)
        # print(contentstr)
while True:
    main()