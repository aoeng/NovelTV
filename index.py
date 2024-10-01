import streamlit as st

novel_page = st.Page("web/novel.py", title="小说管理", icon=":material/apps:")
role_page = st.Page("web/role.py", title="角色管理", icon=":material/settings_accessibility:")
section_page = st.Page("web/section.py", title="段落管理", icon=":material/stacks:")
setting_page = st.Page("web/setting.py", title="配置管理", icon=":material/settings:")
pg = st.navigation([novel_page, role_page, section_page, setting_page])

st.set_page_config(page_title="小说推文", page_icon=":material/home:")

pg.run()
