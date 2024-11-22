import streamlit as st
import langchain_helper
from langchain_helper import cuisine_function

st.title("Reasturent name generator")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexical","American"))


if cuisine:
    response=cuisine_function(cuisine)
    st.header(response['reasturent_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write("***Menu Items***")
    for item in menu_items:
        st.write("-",item)