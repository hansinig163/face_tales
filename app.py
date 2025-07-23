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

# Filter remedies
filtered = remedies if selected_issue == "All" else [r for r in remedies if r["issue"] == selected_issue]

# Display remedies
for remedy in filtered:
    with st.expander(remedy['title']):
        st.write(f"💢 *Issue:* {remedy['issue']}")
        st.write(f"📝 *Steps:*\n{remedy['steps']}")

st.markdown("<footer style='text-align: center; margin-top: 40px; color: grey;'>Made with 💖 by Honey</footer>", unsafe_allow_html=True)