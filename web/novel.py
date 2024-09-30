
import streamlit as st


def create_novel():
    st.title('创建新小说')
    name = st.text_input('名称')



st.title("角色管理")

if st.button('创建新小说'):
    create_novel()


