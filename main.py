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
    "INTJ": {
        "celebrities": ["이정재 🎬", "엘론 머스크 🚀", "아리아나 그란데 🎤"],
        "description": "🧠 전략가 INTJ는 계획을 잘 세우고 미래를 내다보는 능력이 뛰어나요.\n💪 장점: 분석적 사고, 목표 지향적, 독립성\n😅 단점: 고집이 셀 수 있어요, 감정 표현에 서툴 수 있어요"
    },
    "INTP": {
        "celebrities": ["정해인 🎥", "앨버트 아인슈타인 🧪", "트로이 시반 🎶"],
        "description": "🔍 아이디어 뱅크 INTP는 궁금한 게 많고 깊이 있게 생각하는 걸 좋아해요!\n💪 장점: 창의적, 논리적, 호기심 많음\n😅 단점: 현실보단 이론에 빠지기 쉬움, 감정 표현 부족"
    },
    "ENTJ": {
        "celebrities": ["오프라 윈프리 🎤", "고든 램지 🍳", "정우성 🎬"],
        "description": "👑 리더십 강한 ENTJ는 뭐든 계획하고 실행하는 데 능해요.\n💪 장점: 추진력, 전략적 사고, 리더십\n😅 단점: 완벽주의, 융통성 부족할 수 있어요"
    },
    "ENTP": {
        "celebrities": ["유재석 😂", "로버트 다우니 주니어 🦾", "에디슨 💡"],
        "description": "🎉 아이디어 부자 ENTP는 새로운 걸 도전하는 걸 좋아하고, 말솜씨도 좋아요!\n💪 장점: 창의적, 활발한 토론가, 순발력\n😅 단점: 산만함, 계획 마무리 어려움"
    },
    "INFJ": {
        "celebrities": ["BTS RM 🎶", "태연 🎤", "엘리자베스 올슨 🧙‍♀️"],
        "description": "🌌 조용한 이상주의자 INFJ는 세상을 더 나은 곳으로 만들고 싶어 해요.\n💪 장점: 깊은 공감, 통찰력, 헌신적\n😅 단점: 혼자 고민 많이 함, 쉽게 지칠 수 있어요"
    },
    "INFP": {
        "celebrities": ["뷔 🎭", "존 레논 🎸", "앨리샤 키스 🎹"],
        "description": "🎨 감성 가득한 INFP는 마음이 따뜻하고 상상력이 풍부해요!\n💪 장점: 이상주의, 창의성, 공감 능력\n😅 단점: 현실 도피, 결정 어려움"
    },
    "ENFJ": {
        "celebrities": ["바라크 오바마 🇺🇸", "엠마 왓슨 📚", "정은지 🎤"],
        "description": "🌟 따뜻한 지도자 ENFJ는 사람들을 돕고 응원하는 걸 좋아해요.\n💪 장점: 사교성, 열정, 책임감\n😅 단점: 타인을 너무 배려해서 자기감정 억제"
    },
    "ENFP": {
        "celebrities": ["지코 🐯", "아이유 🎤", "윌 스미스 🎬"],
        "description": "🌈 에너지 넘치는 ENFP는 언제나 새로운 걸 찾고, 분위기 메이커예요!\n💪 장점: 창의력, 열정, 친화력\n😅 단점: 산만함, 감정 기복"
    },
    "ISTJ": {
        "celebrities": ["박보검 🎬", "조지 워싱턴 🇺🇸", "나오미 오사카 🎾"],
        "description": "📚 성실한 ISTJ는 규칙을 잘 지키고 믿음직스러워요.\n💪 장점: 책임감, 꼼꼼함, 신뢰성\n😅 단점: 융통성 부족, 변화 어려움"
    },
    "ISFJ": {
        "celebrities": ["아이린 🎤", "비욘세 🎶", "앤 해서웨이 🎭"],
        "description": "🧸 배려심 많은 ISFJ는 조용히 주변을 챙겨주는 천사예요.\n💪 장점: 책임감, 친절함, 헌신적\n😅 단점: 자기표현 부족, 타인 기대에 예민"
    },
    "ESTJ": {
        "celebrities": ["마거릿 대처 🧑‍⚖️", "송강호 🎬", "미셸 오바마 🧕"],
        "description": "🏛️ 조직적이고 단호한 ESTJ는 실행력 있는 현실주의자예요.\n💪 장점: 체계적, 결정력, 지도력\n😅 단점: 완고함, 감정 표현 약함"
    },
    "ESFJ": {
        "celebrities": ["수지 🎤", "테일러 스위프트 🎶", "휴 그랜트 🎬"],
        "description": "🎀 친절한 사교왕 ESFJ는 사람들과 어울리는 걸 정말 좋아해요!\n💪 장점: 배려심, 책임감, 사교성\n😅 단점: 타인의 시선에 민감, 스트레스에 취약"
    },
    "ISTP": {
        "celebrities": ["이민호 🎬", "크리스틴 스튜어트 🏍️", "브루스 윌리스 🔧"],
        "description": "🔧 조용한 모험가 ISTP는 탐험과 실험을 좋아해요!\n💪 장점: 관찰력, 손재주, 논리적\n😅 단점: 감정 공유 어려움, 충동적 행동"
    },
    "ISFP": {
        "celebrities": ["정국 🎤", "리아나 🎶", "마이클 잭슨 🕺"],
        "description": "🎨 예술적 감성의 ISFP는 자유롭고 조용한 성향이에요.\n💪 장점: 미적 감각, 따뜻함, 유연함\n😅 단점: 우유부단함, 자기표현 부족"
    },
    "ESTP": {
        "celebrities": ["카이 🎤", "에르난 크레스포 ⚽", "마돈나 🎤"],
        "description": "⚡ 활력 넘치는 ESTP는 재미있는 걸 좋아하고 즉흥적이에요!\n💪 장점: 사교성, 적응력, 추진력\n😅 단점: 참을성 부족, 충동적"
    },
    "ESFP": {
        "celebrities": ["하니 🎤", "엘튼 존 🎹", "카메론 디아즈 🎬"],
        "description": "🎊 밝고 낙천적인 ESFP는 어디서든 분위기 메이커예요!\n💪 장점: 친근함, 유쾌함, 감성적\n😅 단점: 계획 부족, 감정 기복"
    }
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
