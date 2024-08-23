from openai import OpenAI

client = OpenAI(api_key="api", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "a helpful assistant, 回答在五百字以内"},
        {"role": "user", "content": "文学创作"},
    ],
    stream=False
)

print(response.choices[0].message.content)