# gr_streamlit_clock.py
import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="GR Clock", layout="centered")

st.markdown("<h1 style='text-align: center;'>🕒 GR Clock</h1>", unsafe_allow_html=True)

# ASCII-style dial (text-based)
dial = """
        🕛        
    🕚       🕐    
  🕙    GR     🕑  
    🕘       🕒    
        🕞        
"""

st.markdown(f"<pre style='text-align: center;'>{dial}</pre>", unsafe_allow_html=True)

# Clock display area
clock_placeholder = st.empty()

while True:
    now = datetime.now().strftime('%H:%M:%S')
    clock_placeholder.markdown(
        f"<h2 style='text-align: center; color: white; background-color: black; padding: 10px;'>{now}</h2>",
        unsafe_allow_html=True
    )
    time.sleep(1)
