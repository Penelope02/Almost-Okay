import streamlit as st
import pandas as pd
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Almost Okay", layout="wide")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        /* Background + fonts */
        [data-testid="stAppViewContainer"] {
            background-color: #FFF9F3; /* soft cream to match logo */
            font-family: 'Inter', sans-serif;
            color: #2E2E2E;
        }
        [data-testid="stSidebar"] {
            background-color: #F5EBDD;
        }
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif;
            color: #2E2E2E;
        }
        div.stButton > button {
            background-color: #C8D6C4;
            color: #2E2E2E;
            border-radius: 12px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #E4C4B8;
            color: white;
        }
        .stDataFrame {
            border-radius: 12px;
            background-color: white;
        }
        a {
            color: #2E2E2E;
            text-decoration: underline dotted;
        }
        .streamlit-expanderHeader {
            font-weight: 600;
            color: #2E2E2E;
        }
    </style>
""", unsafe_allow_html=True)


# --- LOGO & HEADER ---
st.markdown(
    """
    <div style="text-align:center; padding-top:20px; padding-bottom:10px;">
        <img src="logo.png" width="250" alt="Almost Okay Logo"><br>
        <p style="font-size:18px; color:#4a4a4a; font-family:'Inter', sans-serif; margin-top:15px;">
            A transparent guide to therapy in the Netherlands.<br>
            Because being almost okay is perfectly okay 🌷
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- CALM QUOTE ---
quotes = [
    "Healing isn't linear 🌿",
    "It's okay to rest before you restart.",
    "Small steps still count 💛",
    "Your feelings are valid, always.",
    "You don't have to move mountains. Simply fall in love with the process of growing. – Morgan Harper Nichols",
    "You are not behind. You are exactly where you need to be.",
    "One day, you will tell your story of how you overcame what you went through – and it will become someone else's survival guide. – Brené Brown",
    "Rest is not laziness, it's medicine. – Glennon Doyle",
    "The wound is the place where the light enters you. – Rumi",
    "It's okay to be a masterpiece and a work in progress at the same time. – Sophia Bush",
]
st.caption(random.choice(quotes))


# --- WELCOME CARD ---
st.markdown("""
<div style="background-color:#F3E6D8;padding:15px;border-radius:15px;text-align:center; margin-bottom:20px;">
<b>Welcome to Almost Okay 💛</b><br>
We’re here to make mental health support in NL more transparent, calm, and human.<br>
Compare prices, waiting times, and find care that fits your pace.
</div>
""", unsafe_allow_html=True)


# --- ABOUT SECTION ---
st.markdown("### 🌱 Why This Exists")
st.write(
    """Finding therapy in the Netherlands can be confusing — prices are often unclear, and waiting times can be long.
    
Almost Okay was created to bring a little clarity (and calm) to the process.  
By listing transparent information in one place, we hope to make mental health support feel more accessible and human.

💛 We believe being almost okay is still a step towards being okay."""
)
st.write("")


# --- LOAD DATA ---
@st.cache_data
def load_data():
    return pd.read_csv("therapists.csv")

df = load_data()


# --- SIDEBAR FILTERS ---
st.sidebar.header("🪴 Filter your search")
cities = st.sidebar.multiselect("City", sorted(df["City"].unique()))
types = st.sidebar.multiselect("Type", sorted(df["Type"].unique()))
max_price = st.sidebar.slider("Max price (€)", 40, 200, 120)

filtered = df.copy()
if cities:
    filtered = filtered[filtered["City"].isin(cities)]
if types:
    filtered = filtered[filtered["Type"].isin(types)]
filtered = filtered[filtered["Price (€)"] <= max_price]


# --- TABLE DISPLAY ---
st.markdown("### 💶 Compare Therapists")
st.dataframe(
    filtered.reset_index(drop=True),
    use_container_width=True,
    hide_index=True
)


# --- ADD YOUR PRACTICE ---
st.markdown("---")
st.markdown(
    "🪴 **Know a therapist who should be listed here?** [Submit their details](https://forms.gle/YOUR_FORM_LINK) — it’s free to be added to Almost Okay."
)


# --- FOOTER ---
st.markdown("""
<hr style="border:0.5px solid #EAE4D3;">
<div style="text-align:center;color:#555;">
Made with calm energy in the Netherlands 🌷<br>
© 2025 Almost Okay
</div>
""", unsafe_allow_html=True)













