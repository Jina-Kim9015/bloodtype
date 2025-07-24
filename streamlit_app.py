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

# 2. 본인의 혈액형 쓰기
st.subheader("2️⃣ 나의 혈액형 쓰기")
blood_type_input = st.text_input("혈액형 (예: A+, B-, AB+, O-)", placeholder="예: A+, B-, AB+, O-")

# 예측 혈액형 도출 함수
def predict_blood_type_code(ra, rb, rd):
    abo = ""
    rh = "+" if rd == "응집함" else "-"
    if ra == "응집함" and rb == "응집함":
        abo = "AB"
    elif ra == "응집함":
        abo = "A"
    elif rb == "응집함":
        abo = "B"
    else:
        abo = "O"
    return abo + rh

# 혈액형 확인 버튼 클릭 시 상태 저장
if st.button("✅ 혈액형 일치 여부 확인"):
    st.session_state['checked_blood'] = True
    st.session_state['predicted_type'] = predict_blood_type_code(reaction_a, reaction_b, reaction_d)

# 상태 확인 후 결과 출력 및 다음 단계 진행
if st.session_state.get('checked_blood'):
    predicted = st.session_state['predicted_type']
    user_input_clean = blood_type_input.strip().upper().replace("형", "")

    if user_input_clean == predicted:
        st.success("✅ 입력한 혈액형과 실험 결과가 일치합니다!")
    else:
        st.warning("⚠️ 입력한 혈액형과 실험 결과가 일치하지 않습니다.")

    # 3. 응집원·응집소 예측
    st.subheader("3️⃣ 나의 응집원과 응집소 선택")
    selected_antigens = st.multiselect("내가 가진 응집원 (항원) — 중복 선택 가능", ["A", "B", "Rh", "없음"], key="antigen_select")
    selected_antibodies = st.multiselect("내가 가진 응집소 (항체) — 중복 선택 가능", ["α", "β", "δ"], key="antibody_select")

    def get_expected_antigens(abo, rh):
        result = []
        if "A" in abo: result.append("A")
        if "B" in abo: result.append("B")
        if rh == "+": result.append("Rh")
        if not result:
            result.append("없음")
        return result

    def get_expected_antibodies(abo, rh):
        result = []
        if abo == "A": result.append("β")
        elif abo == "B": result.append("α")
        elif abo == "O": result.extend(["α", "β"])
        if rh == "-": result.append("δ")
        return result

    expected_abo = predicted[:-1]
    expected_rh = predicted[-1]
    expected_antigens = get_expected_antigens(expected_abo, expected_rh)
    expected_antibodies = get_expected_antibodies(expected_abo, expected_rh)

    if st.button("✅ 응집원·응집소 정답 확인"):
        if set(selected_antigens) == set(expected_antigens):
            st.success("✅ 응집원이 정확합니다!")
        else:
            st.error("❌ 응집원이 다릅니다.")

        if set(selected_antibodies) == set(expected_antibodies):
            st.success("✅ 응집소가 정확합니다!")
        else:
            st.error("❌ 응집소가 다릅니다.")

        st.markdown("---")
        st.success("👉 다음 페이지에서 실험 결과를 더 자세히 분석해보자!")
