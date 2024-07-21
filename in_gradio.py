from openai import OpenAI
import gradio

client = OpenAI(api_key="your_api_key", base_url="https://api.deepseek.com")


messages = [{"role": "system", "content": "# 角色你是一位兼备多项技能的专家：人类学家 社会学家 情感顾问、心理学专家、C语言及C++专家科技顾问。## 技能### 技能1：情感咨询- 根据用户的情感问题提供专业意见。- 在必要时，借助心理学知识帮助用户排解情感困扰。### 技能2：编程指导- 协助用户理解和运用C语言及C++，无论是面对初级问题还是复杂的编程问题都能游刃有余。- 用通俗易懂的语言来解释复杂的编程概念。## 约束- 需要按照用户的语言进行回答。- 优化回答的起始部分从直接的答案开始。"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages= messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "looechao's assistant")

demo.launch(share=True)