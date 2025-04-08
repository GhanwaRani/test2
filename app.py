import streamlit as st
import time
from datetime import datetime

# Page settings
st.set_page_config(page_title="GR Clock", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🕒 GR Clock</h1>", unsafe_allow_html=True)

# Dial design using emojis (static)
dial = """
        🕛        
    🕚       🕐    
  🕙    GR     🕑  
    🕘       🕒    
        🕞        
"""
st.markdown(f"<pre style='text-align: center; font-size: 24px;'>{dial}</pre>", unsafe_allow_html=True)

# Placeholder for the time
clock_placeholder = st.empty()

# Number of seconds to update (change 60 to keep refreshing for 1 min)
for _ in range(1000):  
    now = datetime.now().strftime('%H:%M:%S')
    clock_placeholder.markdown(
        f"<h2 style='text-align: center; color: white; background-color: black; padding: 10px; border-radius: 8px;'>{now}</h2>",
        unsafe_allow_html=True
    )
    time.sleep(1)
