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
    if prompt:
        # st.write(f"User: {prompt}")
        st.chat_message("user").write(prompt)
        print("------------->调用大模型，提示词：", prompt)
        response = client.chat(
            model="qwen3.5:9b",
            messages=[
                {"role":"system",
                 "content":system_prompt},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            stream=False,
        )
        # print(response['message']['content'])
        print("<---------------大模型返回的结果为：",response['message']['content'])
        st.chat_message("assistant").write(response['message']['content'])