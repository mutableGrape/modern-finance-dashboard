import streamlit as st

if "finance_data" not in st.session_state:
    st.session_state.finance_data = []

page_data = [
    {
        "page_name": "Dashboard",
        "page_icon": ":material/dashboard:",
        "filepath": "pages/dashboard.py",
    },
    {
        "page_name": "Analysis",
        "page_icon": ":material/query_stats:",
        "filepath": "pages/analysis.py",
    },
    {
        "page_name": "Settings",
        "page_icon": ":material/settings:",
        "filepath": "pages/settings.py",
    },
]

pages = [
    st.Page(page["filepath"], title=page["page_name"], icon=page["page_icon"]) for page in page_data
]

st_nav = st.navigation(pages)
st_nav.run()