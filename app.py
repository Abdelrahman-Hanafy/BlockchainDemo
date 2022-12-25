from io import StringIO
import streamlit as st
from Block import Blockchain 
from BlockFun import *

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Block Chain", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Hi, Welcome to our Blockchain :wave:")
    st.subheader("we are Computer Engineering Students @ Arab Academy for Science and technology")
    st.write(
        "We are doing this website as a project @ Data security course"
    )


with st.form(key="Form1"):

    option = st.selectbox(
    'What Do you want to do?',
    ('Mine new block', 'View the chain', 'Check validity'))

    #type = st.radio("Your program is ",('SIC', 'SIC\XE'))
    #st_add = st.text_input("Start Add ",value = '0000')
    #uploaded_file = st.file_uploader("Choose a file")

    sub = st.form_submit_button()


# Initialization
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

if sub:

    if option == 'Mine new block':
        res,st.session_state.blockchain = mine_block(st.session_state.blockchain)
        dic = {"labels":[i for i in res.keys() ],"values":[i for i in res.values()]}
        st.table(dic)

    elif option == 'View the chain':
        res = display_chain(st.session_state.blockchain)
        for item in res['chain']:
            dic = {"labels":[i for i in item.keys() ],"values":[i for i in item.values()]}
            st.table(dic)
            #st.write(item)

    elif option == 'Check validity':
        res,flg = valid(st.session_state.blockchain)
        if flg:
            st.success(res['message'])
        else:
            st.error(res['message'])