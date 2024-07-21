from openai import OpenAI

client = OpenAI(api_key="your_api_key", base_url="https://api.deepseek.com")

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": message},
    ],
    stream=False
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")


