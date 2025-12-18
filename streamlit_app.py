import streamlit as st
from collections import Counter

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(page_title="CODE: ME", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = "intro"
if "answers" not in st.session_state:
    st.session_state.answers = []

# -----------------------------
# 질문 및 선택지 데이터
# -----------------------------
chapters = [
    {
        "title": "Chapter 1 | 음악과 감정 반응",
        "questions": [
            ("음악을 들을 때 가장 중요한 것은?",
             {"가사와 메시지": "emotion",
              "분위기와 감정": "emotion",
              "리듬과 에너지": "expression",
              "구조와 완성도": "analysis"}),
            ("새로운 음악을 접할 때 나는?",
             {"감정적으로 바로 반응": "emotion",
              "분석하며 듣는다": "analysis",
              "스타일을 본다": "expression",
              "익숙한 것 위주": "structure"})
        ]
    },
    {
        "title": "Chapter 2 | 패션과 자기표현",
        "questions": [
            ("옷을 고를 때 가장 우선하는 기준은?",
             {"편안함": "structure",
              "이미지 관리": "analysis",
              "개성 표현": "expression",
              "상황과 맥락": "analysis"}),
            ("패션은 나에게 어떤 의미인가?",
             {"나를 드러내는 수단": "expression",
              "사회적 언어": "analysis",
              "실용적인 도구": "structure",
              "기분 전환": "emotion"})
        ]
    },
    {
        "title": "Chapter 3 | 뷰티와 자기관리",
        "questions": [
            ("자기관리는 왜 한다고 생각하나?",
             {"나 자신을 존중해서": "emotion",
              "신뢰를 주기 위해": "analysis",
              "표현의 일부": "expression",
              "필요해서": "structure"}),
            ("스타일 변화를 시도할 때 나는?",
             {"과감히 바꾼다": "expression",
              "천천히 조정": "structure",
              "이유 있을 때만": "analysis",
              "거의 안 바꿈": "structure"})
        ]
    },
    {
        "title": "Chapter 4 | 사고방식과 인문적 태도",
        "questions": [
            ("문제 상황에서 먼저 드는 생각은?",
             {"사람의 감정": "emotion",
              "원인과 구조": "analysis",
              "해결 방법": "structure",
              "의미와 가치": "emotion"}),
            ("진로에서 가장 중요한 것은?",
             {"의미와 보람": "emotion",
              "사회적 영향력": "analysis",
              "안정성": "structure",
              "창의적 자유": "expression"})
        ]
    }
]

# -----------------------------
# 시작 화면
# -----------------------------
if st.session_state.step == "intro":
    st.title("CODE: ME — 문화로 읽는 나의 정체성")
    st.write("""
이 앱은 당신의 음악, 패션, 뷰티 선택을  
단순한 취향이 아닌 **문화적 언어**로 해석합니다.

우리는 무엇을 입고, 무엇을 듣고,  
어떤 방식으로 자신을 표현하는지에 따라  
세상과 관계 맺는 방식을 드러냅니다.

이 앱은 정답이나 유형을 제시하지 않습니다.  
대신 선택의 **패턴과 방향성**을 인문학적으로 해석합니다.

천천히, 솔직하게 답해 주세요.
""")
    if st.button("시작하기"):
        st.session_state.step = 0
        st.rerun()

# -----------------------------
# 질문 진행
# -----------------------------
elif isinstance(st.session_state.step, int):
    chapter_index = st.session_state.step
    chapter = chapters[chapter_index]

    st.header(chapter["title"])
    
    # 이번 챕터의 질문
    for i, (q, options) in enumerate(chapter["questions"]):
        answer = st.radio(q, list(options.keys()), key=f"{chapter_index}_{i}")
        index = chapter_index * 2 + i
        if len(st.session_state.answers) > index:
            st.session_state.answers[index] = (options[answer], answer)
        else:
            st.session_state.answers.append((options[answer], answer))

    if st.button("다음"):
        if chapter_index + 1 < len(chapters):
            st.session_state.step += 1
        else:
            st.session_state.step = "result"
        st.rerun()

# -----------------------------
# 결과 분석
# -----------------------------
elif st.session_state.step == "result":
    st.title("분석 결과")

    tags = [tag for tag, _ in st.session_state.answers]
    counter = Counter(tags)
    main_tag = counter.most_common(1)[0][0]

    # 2단락 분석 결과
    results = {
        "emotion": (
            "당신의 선택은 감정에 대한 민감한 인식과 공감 능력을 강하게 드러냅니다. "
            "세상을 분석하기보다 먼저 느끼고, 사람과 상황의 온도를 읽는 방식에 익숙합니다. "
            "이는 인간 중심적 사고와 깊은 의미 탐색으로 이어집니다.",
            "이러한 성향은 인문, 교육, 예체능 계열에서 강점으로 작용할 가능성이 큽니다. "
            "자신과 타인의 감정을 이해하고 문화적 맥락을 해석하는 능력이 뛰어나, "
            "창의적 표현이나 사람 중심적 프로젝트에서도 두각을 나타낼 수 있습니다."
        ),
        "analysis": (
            "당신은 감정보다 구조와 맥락을 먼저 파악하려는 경향을 보입니다. "
            "선택 하나하나에 이유를 부여하며, 사회와 시스템을 분석적으로 이해합니다.",
            "이는 사회, 공학, 의학 계열에서 문제 해결형 사고로 확장될 수 있습니다. "
            "논리적 판단과 체계적 분석 능력이 요구되는 분야에서 큰 장점을 발휘할 수 있습니다."
        ),
        "expression": (
            "당신은 자기표현과 창의성을 중요시하며, 선택 하나하나가 개성과 스타일을 드러냅니다. "
            "문화, 예술, 디자인 관련 분야에서 몰입력이 높고 새로운 시도를 즐기는 성향입니다.",
            "예체능, 인문, 교육 계열에서 두각을 나타낼 가능성이 있습니다. "
            "자신만의 독창적 관점과 감각으로 사람들과 소통하거나 작품을 만들어낼 수 있습니다."
        ),
        "structure": (
            "당신은 안정적이고 체계적인 사고를 선호하며, 선택에서도 신중함이 드러납니다. "
            "규칙과 맥락을 중시하며, 문제를 단계적으로 해결하는 경향이 있습니다.",
            "공학, 자연, 사회 계열에서 체계적 분석과 기획 능력을 발휘할 수 있습니다. "
            "안정적이고 신중한 접근으로 프로젝트와 업무를 계획적으로 수행할 수 있습니다."
        )
    }

    para1, para2 = results.get(main_tag, ("당신의 성향은 독특하며 다방면에서 가능성이 있습니다.", ""))
    st.write(para1)
    st.write(para2)

    st.success("CODE: ME 분석이 완료되었습니다.")
