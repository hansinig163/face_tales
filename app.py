import streamlit as st
import json

# Load remedies
with open("remedies.json", "r") as f:
    remedies = json.load(f)

st.set_page_config(page_title="Face Tales 💖", page_icon="🌿")
st.markdown("<h1 style='text-align: center; color: pink;'>🌸 Face Tales – Pretty Remedies 🌸</h1>", unsafe_allow_html=True)
st.markdown("💕 Discover your ✨skin's bff✨ – with cute home remedies you’ll love 💕")

# Category selection
issues = sorted(set([r['issue'] for r in remedies]))
selected_issue = st.selectbox("💭 Pick your skin concern:", ["All"] + issues)

# Filter remedies:
with st.expander(remedy['title']):
        st.write(f"💢 *Issue:* {remedy['issue']}")
        st.write(f"📝 *Steps:*\n{remedy['steps']}")

st.markdown("<footer style='text-align: center; margin-top: 40px; color: grey;'>Made with 💖 by Honey</footer>", unsafe_allow_html=True)
=======
import streamlit as st
import json
import os

# Load remedies JSON
with open("real_remedies_50plus.json", "r", encoding="utf-8") as f:
    remedies = json.load(f)

# 🌸 Pretty Page Setup
st.set_page_config(page_title="Face Tales – Pretty Remedies", page_icon="🌷", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
        color: #4B4453;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stTextInput > div > div > input {
        border: 2px solid #ffb6c1;
        border-radius: 10px;
        background-color: #fff0f5;
    }
    </style>
""", unsafe_allow_html=True)

# 🌼 App Header
st.markdown("<h1 style='text-align: center;'>🌸 Face Tales – Pretty Remedies 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Discover your 🌟 skin’s bff 🌟 – with cute home remedies you’ll love 💕</p>", unsafe_allow_html=True)
st.markdown("---")

# 💡 Session State for page switching
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# 🌷 Remedy Input Page
if not st.session_state.show_result:
    user_concern = st.text_input("Type your concern (e.g. acne, dry skin, blackheads) 💌").strip().lower()

    if user_concern:
        if user_concern in remedies:
            st.session_state.selected_concern = user_concern
            st.session_state.show_result = True
            st.experimental_rerun()
        else:
            st.warning("Sorry babe 🥺! No remedy found. Try something like 'acne', 'dandruff', etc.")

# 💖 Result Page
else:
    concern = st.session_state.selected_concern
    remedy = remedies[concern]

    st.subheader(remedy["title"])

    # 📸 Show image if available
    image_path = f"images/{concern}.jpg"
    if os.path.exists(image_path):
        st.image(image_path, caption="Your remedy in action 🌿", use_column_width=True)
    else:
        st.image("images/default.jpg", caption="Your remedy in action 🌿", use_column_width=True)

    # 🧺 Ingredients
    st.markdown("### 🧺 Ingredients You’ll Need:")
    for item in remedy["ingredients"]:
        st.markdown(f"- {item}")

    # 🪞 How To Use
    st.markdown("### 🪞 How To Use:")
    st.markdown(remedy["how_to"])

    st.success("✨ Tip: Always do a patch test before using anything new 💗")

    # 🔙 Back button
    if st.button("🔙 Try another concern"):
        st.session_state.show_result = False
        st.experimental_rerun()

# ✨ Footer
st.markdown("---")
st.caption("Made with 💖 by Face Tales | Your home remedy BFF 🌿")
