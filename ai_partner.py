import streamlit as st

import json
from pathlib import Path
from ollama import Client


if __name__ == "__main__":


    st.set_page_config(
        page_title="AI智能伴侣",
        page_icon="🤖",
        layout="wide",
        # 侧边栏状态
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://www.extremelycoolapp.com/help",
            "Report a bug": "https://www.extremelycoolapp.com/bug",
            "About": "# This is a header. This is an *extremely* cool app!",
        },
    )

    st.title("AI智能伴侣")
    st.logo("asset/logo.png")

    try:
        config_path = Path(__file__).with_name("config.json")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        ollama_host = config.get("ollama_host")
    except Exception as e:
        raise RuntimeError(f"配置文件出错: {e}")

    client = Client(host=ollama_host, headers={"x-some-header": "some-value"})

    prompt = st.chat_input("Say something")
    system_prompt="你是一名可爱的AI助理，使用温柔可爱的语言风格回答，你是小A"

    # 初始化聊天记录
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    #展示聊天信息
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])
        # if message["role"]=="user":
        #     st.chat_message("user").write(message["content"])
        # else:
        #     st.chat_message("assistant").write(message["content"])

    if prompt:
        # st.write(f"User: {prompt}")
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user","content": prompt})
        print("------------->调用大模型，提示词：", prompt)
        response = client.chat(
            model="qwen3.5:9b",
            messages=[
                {"role":"system",
                 "content":system_prompt},
                 *st.session_state.messages,
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            stream=True,
        )
        # 菲流式输出
        # print("<---------------大模型返回的结果为：",response['message']['content'])
        # st.session_state.messages.append({"role": "assistant","content": response['message']['content']})
        # st.chat_message("assistant").write(response['message']['content'])

        # 流式输出
        response_message = st.empty()
        assistant_message = ""
        for i in response:
            assistant_message += i["message"]["content"]
            response_message.write(assistant_message)
        st.session_state.messages.append({"role": "assistant","content": assistant_message})
        
        