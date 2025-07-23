import streamlit as st

st.set_page_config(page_title="내 혈액형 판정 결과 기록하기", layout="centered")
st.title("🧪 내 혈액형 판정 결과 기록하기")

st.markdown("실험을 통해 확인한 결과를 아래에 기록해보세요.")

# 1. 항체별 응집 결과 입력
st.subheader("1️⃣ 항체별 실험 반응 결과")

col1, col2, col3 = st.columns(3)

with col1:
    reaction_a = st.radio("항 A혈청", ["응집함", "응집하지 않음"], horizontal=True)
with col2:
    reaction_b = st.radio("항 B혈청", ["응집함", "응집하지 않음"], horizontal=True)
with col3:
    reaction_d = st.radio("항 D(Rh)혈청", ["응집함", "응집하지 않음"], horizontal=True)

# 2. 본인의 혈액형 (Rh식, ABO식)
st.subheader("2️⃣ 나의 혈액형 쓰기")
abo = st.text_input("ABO식 혈액형", placeholder="예: A형, B형, AB형, O형")
rh = st.text_input("Rh식 혈액형", placeholder="예: Rh⁺, Rh⁻")

# 3. 응집원, 응집소
st.subheader("3️⃣ 나의 응집원과 응집소")
antigens = st.text_input("내가 가진 응집원 (항원)", placeholder="예: A, B, Rh")
antibodies = st.text_input("내가 가진 응집소 (항체)", placeholder="예: Anti-B, Anti-A")

# 제출 결과 요약
if st.button("✅ 제출 내용 확인"):
    st.success("당신의 입력 내용을 확인해보세요:")
    st.markdown(f"""
    ### 🔍 실험 결과 요약

    **항 A혈청 반응**: {reaction_a}  
    **항 B혈청 반응**: {reaction_b}  
    **항 D(Rh)혈청 반응**: {reaction_d}  

    **ABO식 혈액형**: {abo}  
    **Rh식 혈액형**: {rh}  

    **응집원(항원)**: {antigens}  
    **응집소(항체)**: {antibodies}  
    """)

    st.info("❗ 다음 페이지에서 응집 결과를 더 자세히 살펴볼까요 ?")
