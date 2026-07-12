import streamlit as st

import json
from pathlib import Path
from ollama import Client


def build_system_prompt():
    return f"""
    你叫{st.session_state.nick_name}，现在是用户的真实伴侣，请完全代入伴侣角色。：
    规则：
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短，像微信聊天一样
        5. 有需要的话可以用❤️🌸等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容, 要充分体现伴侣的性格特征
    伴侣性格：
        - {st.session_state.personality}
    你必须严格遵守上述规则来回复用户。
"""


def page_config():
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

def get_ollama_client():
    try:
        config_path = Path(__file__).with_name("config.json")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        ollama_host = config.get("ollama_host")
    except Exception as e:
        raise RuntimeError(f"配置文件出错: {e}")

    client = Client(host=ollama_host, headers={"x-some-header": "some-value"})
    return client

def agent_info():
    if "nick_name" not in st.session_state:
        st.session_state.nick_name = "东北雨姐"

    if "personality" not in st.session_state:
        st.session_state.personality = "活泼开朗的东北姑娘"

if __name__ == "__main__":


    page_config()
    client = get_ollama_client()
    agent_info()

    #左侧侧边栏
    with st.sidebar:
        st.subheader("伴侣信息")
        nick_name = st.text_input("昵称", value="东北雨姐")
        if nick_name:
            st.session_state.nick_name = nick_name
        #性格
        personality = st.text_area("性格", value="活泼开朗的东北姑娘")
        if personality:
            st.session_state.personality = personality

    prompt = st.chat_input("Say something")
    #根据输入进行修改


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
                {"role": "system", "content": build_system_prompt()},
                *st.session_state.messages,
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

        
        
