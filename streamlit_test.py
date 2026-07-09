import streamlit as st

st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    layout="wide",
    #侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("布偶猫介绍")
st.header("dawdawdaw")
st.subheader("daaefefae")

st.write("""布偶猫是一种中大型长毛猫，最迷人的特征是湛蓝的眼睛、柔软蓬松的毛发和优雅的重点色花纹。
         它们性格温顺亲人，通常喜欢陪伴主人，抱起来时常显得放松，因此被称为“布偶”。
         布偶猫不太好斗，适合室内饲养，也比较适合有孩子或其他宠物的家庭。
         它们外表像小仙女，气质安静甜美，但毛发较长，需要定期梳理，防止打结和掉毛。
         总体来说，布偶猫是一种颜值高、性格好、陪伴感强的家庭宠物。""")

st.image("./asset/cat.jpg")
st.audio("asset/news.mp3")
st.video("asset/news.mp4")
st.logo("asset/logo.png")
nums=[i for i in range(10)]
st.table(nums)
name=st.text_input("最喜欢的人","None",type="password")
st.write(f"最喜欢的人是{name}")