import os
import streamlit as st

st.set_page_config(page_title="I'm sorry Siss...", page_icon="💔", layout="wide")

# ---- Edit these ----
SORRY_IMAGE = "Sorry1.png"   # original image
HAPPY_IMAGE = "Happy1.png"   # image shown after she presses Yes
HER_NAME = "Siss..."               # optional, e.g. "Riya"
MAX_NO_PRESSES = 19         # image stops growing after this many Nos
# --------------------

NO_MESSAGES = [
    "I know I messed up... and I hate that it hurt you... 🥺",
    "Please don't stay mad forever... I'll shrink every day... 🥹",
    "You're my favorite person to annoy... and apologize to... 💛",
    "I'll do the dishes... all of them... for a week... 🍽️",
    "I'm sorry for what I said... and how I said it...",
    "Can I at least get a half-forgive? 🥺👉👈",
    "I wrote this apology with my whole heart... 💌",
    "I'll let you pick the movie... even the sad one... 🎬",
    "I'm not going anywhere... I'm too sorry to leave... 🌙",
    "Please say yes... my puppy eyes are getting tired... 🐶",
    "You deserve better than how I acted... I'll show you... 🌼",
    "I'll save you the last bite of everything... 🍰",
    "Even grumpy-you is my favorite... please forgive me... 😢",
    "Siblings forgive each other... right? Right..? 🥺",
    "I'm holding a tiny white flag... can you see it..? 🏳️",
    "I'll never stop saying sorry... until you say okay... 💔",
    "Just one tiny smile... that's all I'm asking... 🌷",
    "I promise to think before I speak... next time... and always... 🫶",
    "Okay... I'll just sit here with my sorry and my chocolates... 🍫🥺",
]

if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False


def say_no():
    st.session_state.no_count = min(st.session_state.no_count + 1, MAX_NO_PRESSES)


def say_yes():
    st.session_state.accepted = True


def show_image(path):
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning(f"Put your image at `{path}` next to app.py")


n = st.session_state.no_count
image_scale = 1 + n * 0.025

st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #fff1f5 0%, #ffe1ea 55%, #fff4df 100%);
        color: #563747;
    }}
    .stMainBlockContainer {{
        max-width: none;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }}
    .st-key-apology_frame {{
        box-sizing: border-box;
        width: 80vw;
        height: 80vh;
        margin: 0 auto;
        padding: 1rem;
        overflow: hidden;
        border: 1px solid #efb3c2;
        border-radius: 18px;
        background: #fffaf8;
        box-shadow: 0 16px 48px rgba(170, 72, 105, 0.14);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .st-key-apology_frame [data-testid="stHorizontalBlock"] {{
        flex: 1;
        min-height: 0;
        align-items: center;
    }}
    .st-key-image_stage {{
        width: min(100%, 66vh);
        aspect-ratio: 1;
        margin: 0 auto;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 14px;
        background: #050505;
        border: 4px solid #fff;
        box-shadow: 0 0 0 1px #f2c5d0;
    }}
    .st-key-image_stage [data-testid="stImage"] {{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .st-key-image_stage img {{
        width: auto !important;
        height: 100% !important;
        max-width: 100% !important;
        max-height: 100% !important;
        object-fit: contain;
        transform: scale({image_scale:.3f});
        transition: transform 450ms ease;
    }}
    .st-key-apology_frame [data-testid="stVerticalBlock"] {{ gap: 0.5rem; }}
    .st-key-apology_frame h1 {{ color: #d94370; margin: 0 0 0.25rem; line-height: 1.1; }}
    .st-key-apology_frame h3 {{ color: #71465b; margin: 0.25rem 0; line-height: 1.15; }}
    .st-key-message_bubble {{
        box-sizing: border-box;
        height: 120px;
        margin: 0.4rem 0 0.5rem;
        padding: 0.9rem 1rem;
        display: flex;
        align-items: center;
        border: 1px solid #f0bdca;
        border-left: 4px solid #ee6b8d;
        border-radius: 12px;
        background: #fff0f4;
        color: #563747;
    }}
    .st-key-message_bubble p {{ margin: 0; font-size: 150%; line-height: 1.2; }}
    .st-key-apology_frame [data-testid="stBaseButton-primary"] {{
        background: #e95f84;
        border-color: #e95f84;
        color: #fff;
    }}
    .st-key-apology_frame [data-testid="stBaseButton-primary"]:hover {{
        background: #d94d73;
        border-color: #d94d73;
    }}
    .st-key-apology_frame [data-testid="stBaseButton-secondary"] {{
        border-color: #efbdc8;
        color: #81465e;
        background: #fff5f1;
    }}
    @media (max-width: 760px) {{
        .st-key-apology_frame {{
            width: 94vw;
            height: auto;
            min-height: 80vh;
            margin: 40px auto 0;
            padding: 0.75rem;
        }}
        .st-key-image_stage {{ width: min(100%, 36vh); }}
        .st-key-apology_frame [data-testid="stHorizontalBlock"] {{ gap: 0.3rem !important; }}
        .st-key-apology_frame [data-testid="stVerticalBlock"] {{ gap: 0.25rem; }}
        .st-key-apology_frame h1 {{ font-size: 1.5rem; }}
        .st-key-message_bubble {{
            box-sizing: border-box;
            width: 100%;
            height: 70px;
            min-height: 70px;
            flex-shrink: 0;
            margin: 0.2rem 0;
            padding: 1rem;
        }}
        .st-key-message_bubble p {{ font-size: 112.5%; line-height: 1.2; }}
        .st-key-apology_frame [data-testid="stHorizontalBlock"] {{ flex: initial; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container(key="apology_frame"):
    left, right = st.columns([1.1, 0.9], gap="large", vertical_alignment="center")

    with left:
        with st.container(key="image_stage"):
            show_image(HAPPY_IMAGE if st.session_state.accepted else SORRY_IMAGE)

    with right:
        if st.session_state.accepted:
            st.markdown("# Thank you Siss...🥹")
            st.markdown("### I promise to make it up to you.")
            st.balloons()
        else:
            name = f", {HER_NAME}" if HER_NAME else ""
            st.markdown(f"# I'm sorry{name} 💔")
            st.markdown(
                "I messed up... and I feel terrible about it... "
                "I really value you and I never wanted to hurt you..."
            )
            st.markdown("### Do you accept my apology?")

            message = (
                NO_MESSAGES[min(n - 1, len(NO_MESSAGES) - 1)]
                if n > 0
                else "Your apology is waiting for one little yes..."
            )
            with st.container(key="message_bubble"):
                st.markdown(message)

            st.button("Yes 💖", on_click=say_yes, use_container_width=True, type="primary")
            st.button("No 💔", on_click=say_no, use_container_width=True)
