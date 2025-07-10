import streamlit as st

st.set_page_config(page_title="MBTI 연예인 매칭", page_icon="🎤")
st.title("🎤 MBTI 유형별 연예인 친구 찾기!")
st.write("당신과 같은 성격을 가진 **국내외 스타들✨**은 누구일까요?\nMBTI를 선택해서 확인해보세요! 🧠💫")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("👇 MBTI를 골라주세요!", mbti_list)

data = {
    "ENFP": {
        "celebrities": ["지코 🐯", "아이유 🎤", "로빈 윌리엄스 🤹‍♂️", "윌 스미스 🎬"],
        "description": "ENFP는 세상을 🌈 밝게 만드는 에너자이저예요! 사람들과 어울리기 좋아하고, 아이디어가 넘쳐나요💡. 항상 새로운 걸 시도하고 싶은 마음이 가득하죠!"
    },
    "INFJ": {
        "celebrities": ["BTS RM 🎶", "태연 🎤", "마틴 루터 킹 ✊", "엘리자베스 올슨 🧙‍♀️"],
        "description": "INFJ는 마음이 따뜻한 꿈꾸는 철학자예요 🧚‍♀️. 조용하지만 깊은 생각을 많이 하고, 남을 도와주는 걸 정말 좋아해요 💕."
    },
    "ISTP": {
        "celebrities": ["이민호 🎬", "크리스틴 스튜어트 🏍️", "찰리 푸스 🎹", "브루스 윌리스 🔧"],
        "description": "ISTP는 말보다는 행동! ⚙️ 모험심이 강하고, 손으로 무언가 만드는 걸 좋아해요. 생각보다 유쾌하고 엉뚱한 매력도 있어요 😎."
    },
    "ISFP": {
        "celebrities": ["정국 🎤", "리아나 🎶", "마이클 잭슨 🕺", "브리트니 스피어스 💃"],
        "description": "ISFP는 감성이 풍부한 예술가 🎨. 조용하지만 자신의 스타일이 확실하고, 예쁜 것, 감동적인 걸 좋아해요 💖."
    },
    "ENTJ": {
        "celebrities": ["오프라 윈프리 🎤", "고든 램지 🍳", "정우성 🎬", "앤 해서웨이 👠"],
        "description": "ENTJ는 멋진 리더 타입이에요 🧠👑. 계획을 잘 세우고, 목표를 향해 멋지게 나아가는 추진력이 있어요!"
    },
    "INFP": {
        "celebrities": ["뷔 🎭", "존 레논 🎸", "이효리 🧘", "앨리샤 키스 🎹"],
        "description": "INFP는 상상력과 감성이 풍부한 힐러 타입이에요 🌱✨. 혼자만의 시간을 좋아하지만, 마음은 누구보다 따뜻해요."
    }
    # 여기에 다른 유형도 계속 추가 가능
}

if mbti in data:
    st.subheader("🎬 당신과 같은 MBTI 연예인들!")
    for celeb in data[mbti]["celebrities"]:
        st.markdown(f"- {celeb}")

    st.markdown("---")
    st.subheader("💖 성격 특징 설명")
    st.write(f"{data[mbti]['description']}")

    st.balloons()
else:
    st.info("이 MBTI 유형은 곧 업데이트될 예정이에요! 🔧 기다려주세요 😄")
