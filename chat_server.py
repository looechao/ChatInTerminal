from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key="apikey", base_url="https://api.deepseek.com")

@app.route('/chat', methods=['POST'])
def chat():
    # 从请求中获取数据
    data = request.json
    user_message = data.get('message')

    # 使用 OpenAI API 生成聊天响应
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "a helpful assistant, 回答在五百字以内"},
            {"role": "user", "content": user_message},
        ],
        stream=False
    )

    # 返回生成的消息
    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在这里设置服务器端口