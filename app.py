import streamlit as st
import pandas as pd
import joblib
from api_helper import generate_ai_recommendation
from pdf_report import generate_report


st.set_page_config(
    page_title="AI Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)


model = joblib.load("model.pkl")


_DEFAULTS = {"age": 17, "studytime": 2, "failures": 0, "absences": 5, "g1": 10, "g2": 10}
for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle at 10% 10%, #1b1035 0%, #0d0a1f 45%, #05050f 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1100px; }


    .hero-container {
        background: linear-gradient(120deg, #6a11cb 0%, #2575fc 45%, #00d4ff 100%);
        border-radius: 26px; padding: 48px 40px; margin-bottom: 34px; text-align: center;
        box-shadow: 0 20px 60px rgba(37, 117, 252, 0.35); position: relative; overflow: hidden;
    }
    .hero-container::before { content:""; position:absolute; top:-60px; right:-60px; width:220px; height:220px; background:rgba(255,255,255,0.12); border-radius:50%; }
    .hero-container::after { content:""; position:absolute; bottom:-80px; left:-40px; width:260px; height:260px; background:rgba(255,255,255,0.08); border-radius:50%; }
    .hero-title { font-family:'Poppins',sans-serif; font-weight:800; font-size:2.6rem; color:#fff; margin-bottom:10px; letter-spacing:-0.5px; text-shadow:0 4px 20px rgba(0,0,0,0.25); }
    .hero-subtitle { font-size:1.05rem; color:rgba(255,255,255,0.92); max-width:640px; margin:0 auto; }

  

    .st-key-student_card,
    .st-key-academic_card,
    .st-key-performance_card,
    .st-key-assessment_card {
     background: rgba(255,255,255,0.05);
     border: 1px solid rgba(255,255,255,0.12);
     border-radius: 22px;
     padding: 26px 28px 20px 28px;
     margin-bottom: 26px;
     box-shadow: 0 8px 32px rgba(0,0,0,0.35);
     backdrop-filter: blur(14px);
     -webkit-backdrop-filter: blur(14px);
}      

  
    .field-label { color:#fff; font-weight:600; font-size:0.95rem; margin-bottom:2px; margin-top:24px; }
    .field-sub { color:rgba(255,255,255,0.45); font-size:0.78rem; margin-bottom:10px; }

    /* Text input */
    label, .stTextInput label { color: rgba(255,255,255,0.85) !important; font-weight:500 !important; }
    .stTextInput input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 10px 14px !important;
    }
    .stTextInput input:focus { border:1px solid #00d4ff !important; box-shadow:0 0 0 3px rgba(0,212,255,0.15) !important; }

 
    div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.07) !important;
        border: 1.5px solid rgba(255,255,255,0.18) !important;
        border-radius: 14px !important;
        color: #fff !important;
        min-height: 48px !important;
    }
    div[data-baseweb="select"] * { color: #fff !important; }
    div[data-baseweb="select"]:hover > div { border-color: #00d4ff !important; }
    div[data-baseweb="popover"] ul, ul[data-baseweb="menu"] {
        background: #170e33 !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
    }
    li[role="option"] { color: rgba(255,255,255,0.85) !important; }
    li[role="option"]:hover, li[aria-selected="true"] {
        background: linear-gradient(135deg, rgba(106,17,203,0.5), rgba(0,212,255,0.4)) !important;
        color: #fff !important;
    }


    div.stButton > button {
        border-radius: 14px !important;
        font-family: 'Inter', sans-serif !important;
        cursor: pointer;
        transition: all .2s ease;
        outline: none !important;
        box-shadow: none;
    }
    div.stButton > button:focus { outline:none !important; box-shadow:none !important; }

  
    [class*="st-key-chip_"] button {
        background: rgba(255,255,255,0.06) !important;
        border: 1.5px solid rgba(255,255,255,0.15) !important;
        color: rgba(255,255,255,0.8) !important;
        font-weight: 600 !important;
        padding: 10px 0 !important;
        border-radius: 999px !important;
    }
    [class*="st-key-chip_"] button:hover { border-color:#00d4ff !important; color:#fff !important; }

  
    [class*="st-key-card_"] button {
        background: rgba(255,255,255,0.05) !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        color: rgba(255,255,255,0.85) !important;
        min-height: 78px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.2);
    }
    [class*="st-key-card_"] button:hover { transform: translateY(-3px); border-color: rgba(0,212,255,0.5) !important; }

  
    [class*="st-key-seg_"] button {
        background: rgba(255,255,255,0.05) !important;
        border: 1.5px solid rgba(255,255,255,0.12) !important;
        color: rgba(255,255,255,0.7) !important;
        font-weight: 700 !important;
        padding: 12px 0 !important;
        border-radius: 12px !important;
    }
    [class*="st-key-seg_"] button:hover { border-color: rgba(0,212,255,0.5) !important; }

  
    [class*="st-key-stp_"] button {
        background: rgba(255,255,255,0.08) !important;
        border: 1.5px solid rgba(255,255,255,0.15) !important;
        border-radius: 14px !important;
        color: #fff !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        height: 54px !important;
    }
    [class*="st-key-stp_"] button:hover { border-color:#00d4ff !important; background: rgba(0,212,255,0.15) !important; }
    .stepper-value {
        text-align:center; font-family:'Poppins',sans-serif; font-size:1.9rem; font-weight:800; color:#fff;
        background: rgba(255,255,255,0.04); border-radius:14px; padding:8px 0; border:1px solid rgba(255,255,255,0.1);
    }
    .stepper-max { font-size:0.9rem; color:rgba(255,255,255,0.4); font-weight:500; }

 
    .st-key-predict_action { display:flex; justify-content:center; margin-top:22px; margin-bottom:6px; }
    .st-key-predict_action button {
        background: linear-gradient(120deg, #6a11cb, #2575fc, #00d4ff) !important;
        background-size: 200% 200% !important;
        color: #fff !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        padding: 16px 60px !important;
        border-radius: 999px !important;
        border: none !important;
        box-shadow: 0 12px 35px rgba(37, 117, 252, 0.45) !important;
        letter-spacing: 0.3px;
    }
    .st-key-predict_action button:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 16px 45px rgba(0, 212, 255, 0.55) !important; }


    .result-hero {
        background: linear-gradient(135deg, rgba(106,17,203,0.35), rgba(0,212,255,0.25));
        border: 1px solid rgba(255,255,255,0.18); border-radius: 22px; padding: 30px;
        text-align: center; margin-bottom: 22px; backdrop-filter: blur(14px);
    }
    .result-score { font-family:'Poppins',sans-serif; font-size:3rem; font-weight:800; color:#fff; margin:6px 0; text-shadow:0 4px 20px rgba(0,0,0,0.3); }
    .result-label { color:rgba(255,255,255,0.75); font-size:0.95rem; letter-spacing:1px; text-transform:uppercase; }
    .badge-excellent, .badge-good, .badge-average, .badge-poor {
        display:inline-block; padding:8px 24px; border-radius:999px; font-weight:700; font-family:'Poppins',sans-serif; font-size:1rem; margin-top:10px;
    }
    .badge-excellent { background: rgba(0,230,118,0.18); color:#00e676; border:1px solid #00e67655; }
    .badge-good       { background: rgba(41,182,246,0.18); color:#29b6f6; border:1px solid #29b6f655; }
    .badge-average    { background: rgba(255,193,7,0.18); color:#ffc107; border:1px solid #ffc10755; }
    .badge-poor       { background: rgba(255,82,82,0.18); color:#ff5252; border:1px solid #ff525255; }

    .ai-chat-card {
        background: rgba(255,255,255,0.05); border:1px solid rgba(0,212,255,0.25); border-radius:22px;
        padding:24px 26px; margin-top:10px; margin-bottom:26px; backdrop-filter:blur(14px);
        box-shadow: 0 8px 30px rgba(0,212,255,0.12);
    }
    .ai-chat-header { display:flex; align-items:center; gap:10px; margin-bottom:14px; }
    .ai-avatar { width:40px; height:40px; border-radius:50%; background:linear-gradient(135deg,#6a11cb,#00d4ff); display:flex; align-items:center; justify-content:center; font-size:1.2rem; box-shadow:0 4px 14px rgba(0,212,255,0.4); }
    .ai-chat-name { color:#fff; font-family:'Poppins',sans-serif; font-weight:600; font-size:1.05rem; }
    .ai-chat-status { color:#00e676; font-size:0.75rem; }
    .ai-chat-bubble { background: rgba(255,255,255,0.06); border-radius:16px; padding:16px 18px; color:rgba(255,255,255,0.9); line-height:1.6; font-size:0.95rem; }

 
    div[data-testid="stDownloadButton"] { display:flex; justify-content:center; margin-top:6px; }
    div[data-testid="stDownloadButton"] > button {
        background: rgba(255,255,255,0.08); border:1px solid #00e67680; color:#00e676; font-weight:700;
        border-radius:999px; padding:14px 42px; font-family:'Poppins',sans-serif; transition: all .25s ease;
    }
    div[data-testid="stDownloadButton"] > button:hover { background: rgba(0,230,118,0.15); transform: translateY(-2px); }

    .stProgress > div > div > div { background: linear-gradient(90deg, #6a11cb, #00d4ff) !important; }
    hr { border-color: rgba(255,255,255,0.1) !important; }
</style>
""", unsafe_allow_html=True)



def field_header(title, subtitle):
    st.markdown(f'<div class="field-label">{title}</div><div class="field-sub">{subtitle}</div>', unsafe_allow_html=True)


def chip_group(group, options, state_key, labels=None):
    labels = labels or [str(o) for o in options]
    cols = st.columns(len(options))
    for col, opt, lab in zip(cols, options, labels):
        with col:
            with st.container(key=f"chip_{group}_{opt}"):
                if st.button(lab, key=f"chipbtn_{group}_{opt}", use_container_width=True):
                    st.session_state[state_key] = opt
    current = st.session_state[state_key]
    st.markdown(f"""<style>
    .st-key-chip_{group}_{current} button {{
        background: linear-gradient(135deg, #6a11cb, #00d4ff) !important;
        color: #fff !important;
        border-color: transparent !important;
        box-shadow: 0 6px 18px rgba(0,212,255,0.4) !important;
    }}</style>""", unsafe_allow_html=True)


def card_group(group, cards, state_key):
    cols = st.columns(len(cards))
    for col, (val, lab) in zip(cols, cards):
        with col:
            with st.container(key=f"card_{group}_{val}"):
                if st.button(lab, key=f"cardbtn_{group}_{val}", use_container_width=True):
                    st.session_state[state_key] = val
    current = st.session_state[state_key]
    st.markdown(f"""<style>
    .st-key-card_{group}_{current} button {{
        background: linear-gradient(135deg, rgba(106,17,203,0.9), rgba(0,212,255,0.9)) !important;
        color: #fff !important;
        border-color: transparent !important;
        box-shadow: 0 10px 28px rgba(0,212,255,0.45) !important;
    }}</style>""", unsafe_allow_html=True)


def segmented_control(group, state_key, bands):
    cols = st.columns(len(bands))
    for col, (val, lab, lo, hi) in zip(cols, bands):
        with col:
            with st.container(key=f"seg_{group}_{val}"):
                if st.button(lab, key=f"segbtn_{group}_{val}", use_container_width=True):
                    st.session_state[state_key] = val
    current = st.session_state[state_key]
    rules = []
    for val, lab, lo, hi in bands:
        if lo <= current <= hi:
            rules.append(
                f".st-key-seg_{group}_{val} button {{"
                f"background: linear-gradient(135deg,#6a11cb,#00d4ff) !important;"
                f"color:#fff !important; border-color:transparent !important;}}"
            )
    st.markdown(f"<style>{''.join(rules)}</style>", unsafe_allow_html=True)


def stepper(group, state_key, minv, maxv):
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        with st.container(key=f"stp_{group}_minus"):
            if st.button("−", key=f"stpbtn_{group}_minus", use_container_width=True):
                st.session_state[state_key] = max(minv, st.session_state[state_key] - 1)
    with c2:
        st.markdown(
            f'<div class="stepper-value">{st.session_state[state_key]}'
            f'<span class="stepper-max">/{maxv}</span></div>',
            unsafe_allow_html=True
        )
    with c3:
        with st.container(key=f"stp_{group}_plus"):
            if st.button("+", key=f"stpbtn_{group}_plus", use_container_width=True):
                st.session_state[state_key] = min(maxv, st.session_state[state_key] + 1)


st.markdown("""
<div class="hero-container">
    <div class="hero-title">AI-Driven Student Performance Prediction</div>
    <div class="hero-subtitle">
        Predict a student's final academic performance using Machine Learning,
        with AI-generated recommendations and an instant downloadable report.
    </div>
</div>
""", unsafe_allow_html=True)

with st.container(key="student_card"):
    st.markdown(
        '<div class="card-heading">👤 Student Information</div>',
        unsafe_allow_html=True
    )

    field_header("📝 Student Name", "")
    student_name = st.text_input(
    "Student Name",
    placeholder="Enter student's name",
    label_visibility="collapsed"
)

    field_header("🎂 Age", "Select the student's current age")
    age_options = list(range(15, 26))
    selected_age = st.selectbox(
        "Age",
        options=age_options,
        index=age_options.index(st.session_state["age"]),
        label_visibility="collapsed"
    )
    st.session_state["age"] = selected_age

age = st.session_state["age"]


with st.container(key="academic_card"):
    st.markdown(
        '<div class="card-heading">📘 Academic Information</div>',
        unsafe_allow_html=True
    )


    field_header("⏰ Study Hours", "Average hours spent studying per day")
    card_group("study", [
    (1, "🕐 Less than 2 hrs"),
    (2, "🕑 2–4 hrs"),
    (3, "🕒 4–6 hrs"),
    (4, "🕓 More than 6 hrs"),
], "studytime")


    field_header("⚠️ Previous Failed Subjects", "Number of previously failed subjects")

    chip_group(
    "fail",
    [0, 1, 2, 3, 4],
    "failures",
    labels=[
        "0 Subjects",
        "1 Subject",
        "2 Subjects",
        "3 Subjects",
        "4+ Subjects"
    ]
)
    
    field_header("📅 Attendance", "Select their approximate attendance percentage")
    card_group("attendance", [
        (2, "🟢  95–100%"),
        (12, "🔵  85–94%"),
        (25, "🟡  75–84%"),
        (45, "🔴  Below 75%"),
    ], "absences")

studytime = st.session_state["studytime"]
failures = st.session_state["failures"]
absences = st.session_state["absences"]


with st.container(key="assessment_card"):
    st.markdown(
        '<div class="card-heading">📊 Academic Assessment</div>'
        '<div class="card-subtext">Academic scores used for prediction</div>',
        unsafe_allow_html=True
    )

    field_header("📘 Internal Assessment", "Internal examination marks (0–20)")
    g1 = st.selectbox(
        "Internal Assessment",
        list(range(21)),
        index=st.session_state["g1"],
        label_visibility="collapsed"
    )

    field_header("📝 External Assessment", "External examination marks (0–20)")
    g2 = st.selectbox(
        "External Assessment",
        list(range(21)),
        index=st.session_state["g2"],
        label_visibility="collapsed"
    )

    st.session_state["g1"] = g1
    st.session_state["g2"] = g2

with st.container(key="predict_action"):
    predict = st.button("🔍 Predict Performance")


if predict:

    input_df = pd.DataFrame({
        "age": [age],
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [g1],
        "G2": [g2]
    })

    prediction = model.predict(input_df)[0]

    if prediction >= 16:
        performance = "Excellent"
        badge_class = "badge-excellent"
        badge_icon = "🏆"
    elif prediction >= 12:
        performance = "Good"
        badge_class = "badge-good"
        badge_icon = "🥈"
    elif prediction >= 8:
        performance = "Average"
        badge_class = "badge-average"
        badge_icon = "🥉"
    else:
        performance = "Poor"
        badge_class = "badge-poor"
        badge_icon = "🔴"

    student_display = f"👤 {student_name}" if student_name.strip() else "👤 Student"

    st.markdown(f"""
    <div class="result-hero">
        <div class="result-label">{student_display} · Prediction Result</div>
        <div class="result-score">{prediction:.2f} / 20</div>
        <div class="result-label">Predicted Final Grade (G3)</div>
        <div class="{badge_class}">{badge_icon} Performance Level: {performance}</div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(min(int(prediction * 5), 100))

    with st.spinner("🤖 AI is analyzing the student's performance..."):

        ai_response = generate_ai_recommendation(
            student_name,
            age,
            studytime,
            failures,
            absences,
            g1,
            g2,
            prediction
        )

    st.markdown(f"""
    <div class="ai-chat-card">
        <div class="ai-chat-header">
            <div class="ai-avatar">🤖</div>
            <div>
                <div class="ai-chat-name">AI Academic Advisor</div>
                <div class="ai-chat-status">● Online · Personalized Insight</div>
            </div>
        </div>
        <div class="ai-chat-bubble">{ai_response}</div>
    </div>
    """, unsafe_allow_html=True)

    filename = "Student_Performance_Report.pdf"

    generate_report(
        filename,
        student_name,
        age,
        studytime,
        failures,
        absences,
        g1,
        g2,
        prediction,
        performance,
        ai_response
    )

    with open(filename, "rb") as pdf_file:
        st.download_button(
            label="📄 Download AI Report",
            data=pdf_file,
            file_name=filename,
            mime="application/pdf"
        )