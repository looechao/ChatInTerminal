from openai import OpenAI

client = OpenAI(api_key="your_api_key", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "a helpful assistant"},
        {"role": "user", "content": "write an essay about dragon"},
    ],
    stream=False
)

print(response.choices[0].message.content)