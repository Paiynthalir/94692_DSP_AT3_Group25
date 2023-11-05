# Import packages
import streamlit as st
import pandas as pd
import sys
import os
from pathlib import Path

# Set Python path
current_dir = os.path.dirname(__file__)
parent_dir = str(Path(current_dir).resolve().parents[0])
sys.path.append(parent_dir)

# Import custom functions
from test_display import display_tab_df_content

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="CSV Explorer",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Set objects in Streamlit session state
st.session_state["file_path"] = None
st.session_state["df"] = None
st.session_state["dataset"] = None

# Display Title
st.title("CSV Explorer")

# Add Window to upload CSV file
with st.expander("ℹ️ - Streamlit application for performing data exploration on a CSV", expanded=True):
    st.session_state.file_path = st.file_uploader("Choose a CSV file")

# If a CSV file is uploaded, display the different tabs
if st.session_state.file_path is not None:
    display_tab_df_content(file_path=st.session_state.file_path)

