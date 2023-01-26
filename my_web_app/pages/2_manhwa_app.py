import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

manhwa_select = ["SLAMDUNK", "HUNTERXHUNTER", "BERSERK"]
manhwa_select_option = st.sidebar.selectbox("좋아하는 만화를 선택하세요",manhwa_select, index=2)

folder = './data/'
# 사이드바에 아까 선택하지 않은 것(애니메이션, 영화, 책 등등) 이미지파일3개 가져오셔서
manhwa_image_files =['슬램덩크.jpeg','헌터헌터.jpeg','베르세르크.webp']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
st.header(manhwa_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
manhwa_select_index = manhwa_select.index(manhwa_select_option)

st.write(manhwa_select_index)
st.image(folder + manhwa_image_files[manhwa_select_index])
