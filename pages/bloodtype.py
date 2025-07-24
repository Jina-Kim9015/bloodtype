import streamlit as st
from PIL import Image
import os

# 이미지 폴더 경로
IMAGE_DIR = "images"

# 혈액형 표시: {UI표시용: 파일명}
blood_type_map = {
    "Rh⁺A형": "Rh+A형.png",
    "Rh⁻A형": "Rh-A형.png",
    "Rh⁺B형": "Rh+B형.png",
    "Rh⁻B형": "Rh-B형.png",
    "Rh⁺AB형": "Rh+AB형.png",
    "Rh⁻AB형": "Rh-AB형.png",
    "Rh⁺O형": "Rh+O형.png",
    "Rh⁻O형": "Rh-O형.png"
}

# 사이트 제목
st.set_page_config(page_title="혈액형 판정 들여다보기", layout="wide")
st.title("🧬 혈액형 판정 들여다보기")
st.markdown("아래에서 혈액형을 선택하면 실험 결과를 확인할 수 있습니다.")

# ✅ 항상 표시될 항체(anti) 이미지 (50% 크기로 줄이기)
anti_image_path = os.path.join(IMAGE_DIR, "anti.png")
if os.path.exists(anti_image_path):
    anti_img = Image.open(anti_image_path)
    new_size = (anti_img.width // 2, anti_img.height // 2)  # 50% 크기
    anti_img_resized = anti_img.resize(new_size)
    st.image(anti_img_resized, caption="항A, 항B, 항Rh 혈청")
else:
    st.warning("⚠️ 'anti.png' 이미지가 images 폴더에 없습니다.")

st.markdown("---")

# 버튼 UI 구성 (4열)
cols = st.columns(4)
selected_key = None

for i, label in enumerate(blood_type_map.keys()):
    if cols[i % 4].button(label):
        selected_key = label

# 선택한 혈액형의 이미지 출력
if selected_key:
    file_name = blood_type_map[selected_key]
    file_path = os.path.join(IMAGE_DIR, file_name)

    if os.path.exists(file_path):
        img = Image.open(file_path)
        st.image(img, caption=f"🧪 {selected_key} 실험 결과", use_container_width=True)
    else:
        st.error(f"❌ 이미지 파일이 존재하지 않습니다: {file_path}")
