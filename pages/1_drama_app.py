import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os


drama_select = ["비밀의숲", "DAREDEVIL", "스토브리그"]
drama_select_option = st.sidebar.selectbox("좋아하는 시리즈를 선택하세요",drama_select, index=2)
folder = './data/'
drama_image_files = ['비밀의숲.jpeg','데어데블.png','스토브리그.jpeg']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
html = """
<style>
h2 {
    color : blue;
}
<style>
"""

st.markdown(html, unsafe_allow_html=True)
st.header(drama_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
drama_select_index = drama_select.index(drama_select_option)

st.write(drama_select_index)
st.image(folder + drama_image_files[drama_select_index])