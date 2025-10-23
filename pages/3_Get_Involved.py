import streamlit as st
st.set_page_config(page_title="Get Involved • Almost Okay", page_icon="🤝")

st.title("🤝 Get Involved")
st.write("""
Help us grow this calm, transparent movement.
""")

st.markdown("### 🪴 Submit a Therapist")
st.write("Know a great therapist? Add them here:")
st.link_button("Submit a therapist", "https://forms.gle/YOUR_FORM_LINK")

st.markdown("### 🌟 Volunteer")
st.write("Want to help with data curation, outreach, or design?")
st.link_button("Volunteer interest form", "https://forms.gle/YOUR_VOLUNTEER_FORM")

st.markdown("### 💌 Share the word")
st.code("almost-okay.streamlit.app", language="text")
