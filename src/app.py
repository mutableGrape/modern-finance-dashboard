import streamlit as st

pages = [
    {
        "title": "Dashboard",
        "page": "pages/dashboard.py",
        "icon": ":material/dashboard:"
    },
    {
        "title": "Analysis",
        "page": "pages/analysis.py",
        "icon": ":material/query_stats:"
    },
    {
        "title": "Settings",
        "page": "pages/settings.py",
        "icon": ":material/settings:"
    }
]

nav = []
for page in pages:
    nav.append(
        st.Page(
            page["page"],
            title=page["title"],
            icon=page["icon"],
        )
    )

pg = st.navigation(nav)
pg.run()
