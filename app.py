import streamlit as st
import pandas as pd

st.set_page_config(page_title="Therapy Prices NL", layout="wide")

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
