import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. إعدادات الصفحة الاحترافية (Dark Mode فخم جداً وباسم الراوي ماركت)
st.set_page_config(page_title="ELRAWY MARKET - لوحة التحكم الرقمية", page_icon="🟢", layout="wide")

# 2. حقن ستايل الـ Dark Cyber-WhatsApp الحديث والمبهر جداً
dark_modern_style = """
<style>
    .stApp {
        background-color: #0B141A !important;
        color: #E9EDEF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .main-header {
        background: linear-gradient(135deg, #128C7E 0%, #075E54 100%);
        padding: 25px;
        border-bottom: 2px solid #00A884;
        margin-bottom: 35px;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 168, 132, 0.2);
    }
    [data-testid="metric-container"] {
        background-color: #111B21 !important;
        border: 1px solid #222E35 !important;
        border-top: 4px solid #00A884 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricLabel"] { color: #8696A0 !important; font-size: 0.95rem !important; }
    [data-testid="stMetricValue"] { color: #00A884 !important; font-size: 1.8rem !important; font-weight: bold !important; }
    
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00A884 0%, #25D366 100%) !important;
        color: #111B21 !important;
        border-radius: 30px !important;
        border: none !important;
        font-weight: 800 !important;
        padding: 12px 35px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 168, 132, 0.4);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #25D366 0%, #00A884 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(37, 211, 102, 0.6);
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #111B21 !important; padding: 8px !important; border-radius: 12px !important; border: 1px solid #222E35; }
    .stTabs [data-baseweb="tab"] { color: #8696A0 !important; font-weight: 600 !important; padding: 14px 40px !important; }
    .stTabs [aria-selected="true"] { background-color: #00A884 !important; color: #111B21 !important; border-radius: 8px !important; font-weight: bold !important; }
    
    input, select, div[data-baseweb="select"], .stNumberInput input, .stTextInput input {
        background-color: #222E35 !important; color: #E9EDEF !important; border-radius: 12px !important; border: 1px solid #323D45 !important; padding: 10px !important;
    }
    div[data-testid="stDataFrame"] { background-color: #111B21 !important; border: 1px solid #222E35 !important; border-radius: 15px !important; padding: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.4); }
    hr { border-color: #222E35 !important; }
</style>
"""
st.markdown(dark_modern_style, unsafe_allow_html=True)

# 3.
