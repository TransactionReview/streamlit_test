import streamlit as st

st.sidebar.title('this is sidebar')
st.sidebar.title('this is SIDEBAR')

Checkbox_TEST_1 = st.sidebar.checkbox(key=1, value=False, label='체크박스에 표시될 문구 ######1', label_visibility="visible")
Checkbox_TEST_2 = st.sidebar.checkbox(key=2, value=False, label='체크박스에 표시될 문구 #2', label_visibility="visible")
Checkbox_TEST_3 = st.sidebar.checkbox(key=3, value=True, label='체크박스에 표시될 문구 #3', label_visibility="hidden")
Checkbox_TEST_4 = st.sidebar.checkbox(key=4, value=True, label='체크박스에 표시될 문구 #4', label_visibility="collapsed")
Checkbox_TEST_5 = st.sidebar.checkbox(key=5, value=True, label='체크박스에 표시될 문구 #5', label_visibility="collapsed")
# st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")


tab1, tab2 = st.tabs(['Tab A','Tab B'])
with tab1 :
    st.write('Hello')
    
with tab2 :
    st.write('Streamlit')
    st.link_button(label="App Gallery", url="https://streamlit.io/gallery", help="App Gallery 설명", type="primary", disabled=False, use_container_width=False)
    st.link_button(label="st.link_button", url="https://docs.streamlit.io/library/api-reference/widgets/st.link_button", help="streamlit 설명", type="secondary", disabled=False, use_container_width=False)
    # st.link_button(label, url, *, help=None, type="secondary", disabled=False, use_container_width=False)


col1, col2, col3 = st.columns([4,2,4])
with col1 :  
    st.title('hello Streamlit')
    st.header('hello Header \n 개행문자')
    st.subheader('this is subheader')
    st.write("writing TEST")

with col3 :
    content = "종자 산업은 웰빙·건강에 대한 관심 증가와 농업 부문의 경쟁력 향상 및 새로운 가치 창출을 위해 기능성 증진, 맞춤형 기능 식품 등 대체 식품용 신품종 개발과 고부가가치화 등 농산물 부가가치 향상과 직결돼 있다는 평가가 나온다. \
           정부는 국내 종자 시장 규모를 2027년까지 1조2000억원 규모로 키우고, 종자 수출액도 1억2000만달러까지 확대할 계획이다."
    st.text(content)
    st.markdown(content)

    if Checkbox_TEST_1 :
        st.write("GREAT!!!")
    

