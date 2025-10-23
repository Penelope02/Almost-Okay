import streamlit as st
import pandas as pd

st.set_page_config(page_title="Therapy Prices NL", layout="wide")
# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        /* Background + font setup */
        [data-testid="stAppViewContainer"] {
            background-color: #FAFAF8;
            font-family: 'Inter', sans-serif;
            color: #2E2E2E;
        }
        [data-testid="stSidebar"] {
            background-color: #EAE4D3;
        }
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif;
            color: #2E2E2E;
        }
        /* Buttons */
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
        /* Dataframe container */
        .stDataFrame {
            border-radius: 12px;
            background-color: white;
        }
        /* Links */
        a {
            color: #2E2E2E;
            text-decoration: underline dotted;
        }
        /* Expander style */
        .streamlit-expanderHeader {
            font-weight: 600;
            color: #2E2E2E;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🧠 Therapy Prices NL")
st.subheader("Find therapy that fits — transparent, simple, and stress-free.")
st.write(
    "Compare therapists in the Netherlands by **price**, **availability**, and **specialisation** — all in one place."
)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    return pd.read_csv("therapists.csv")

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter search")
cities = st.sidebar.multiselect("City", sorted(df["City"].unique()))
types = st.sidebar.multiselect("Type", sorted(df["Type"].unique()))
max_price = st.sidebar.slider("Max price (€)", 40, 200, 120)

filtered = df.copy()
if cities:
    filtered = filtered[filtered["City"].isin(cities)]
if types:
    filtered = filtered[filtered["Type"].isin(types)]
filtered = filtered[filtered["Price (€)"] <= max_price]

# --- DISPLAY ---
st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

st.markdown("---")
st.markdown(
    "🪴 **Know a therapist who should be here?** [Submit their details](https://forms.gle/YOUR_FORM_LINK) — it’s free to be listed."
)

# --- ABOUT SECTION ---
with st.expander("Why this exists 🌱"):
    st.write(
        """Finding therapy in the Netherlands can be confusing. Prices aren’t always clear, waiting times can be long, and many people give up before they even start.
        
This project was created to make that process easier — by putting everything in one transparent place.
        
💚 Built independently to help you find the right support faster."""
    )

st.caption(
    "Information is public or user-submitted. Always confirm details directly before booking. © 2025 Therapy Prices NL"
)

