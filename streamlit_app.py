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

# 2. 본인의 혈액형 (하나의 입력창)
st.subheader("2️⃣ 나의 혈액형 쓰기")
blood_type_input = st.text_input("혈액형 (예: A+, B-, AB+, O- 등)", placeholder="예: A+, B-, AB+, O-")

# 3. 실험 결과와 혈액형 일치 확인 버튼
st.subheader("3️⃣ 실험 결과와 혈액형 일치 여부 확인")

# 응집 결과 기반 예측 함수
def predict_blood_type_code(ra, rb, rd):
    abo = ""
    rh = "+" if rd == "응집함" else "-"

    if ra == "응집함" and rb == "응집함":
        abo = "AB"
    elif ra == "응집함" and rb == "응집하지 않음":
        abo = "A"
    elif ra == "응집하지 않음" and rb == "응집함":
        abo = "B"
    elif ra == "응집하지 않음" and rb == "응집하지 않음":
        abo = "O"

    return abo + rh

if st.button("✅ 혈액형 일치 여부 확인"):
    predicted_type = predict_blood_type_code(reaction_a, reaction_b, reaction_d)
    if blood_type_input.strip().upper().replace("형", "") == predicted_type:
        st.success("✅ 입력한 혈액형과 실험 결과가 일치합니다!")
    else:
        st.warning("⚠️ 입력한 혈액형과 실험 결과가 일치하지 않습니다. 다시 확인해보세요!")

    # 4. 응집원, 응집소 선택형
    st.subheader("4️⃣ 나의 응집원과 응집소 예측")
    selected_antigens = st.multiselect("내가 가진 응집원 (항원)", ["A", "B", "Rh", "없음"])
    selected_antibodies = st.multiselect("내가 가진 응집소 (항체)", ["α", "β", "δ"])

    # 정답 기준 정의
    def get_expected_antigens(abo, rh):
        antigens = []
        if "A" in abo: antigens.append("A")
        if "B" in abo: antigens.append("B")
        if rh == "+": antigens.append("Rh")
        if len(antigens) == 0:
            antigens.append("없음")
        return antigens

    def get_expected_antibodies(abo, rh):
        antibodies = []
        if abo == "A": antibodies.extend(["β"])
        elif abo == "B": antibodies.extend(["α"])
        elif abo == "O": antibodies.extend(["α", "β"])
        elif abo == "AB": antibodies.extend([])
        if rh == "-": antibodies.append("δ")
        return antibodies

    expected_abo = predicted_type[:-1] if predicted_type[-1] in ["+", "-"] else predicted_type
    expected_rh = predicted_type[-1] if predicted_type[-1] in ["+", "-"] else ""

    expected_antigens = get_expected_antigens(expected_abo, expected_rh)
    expected_antibodies = get_expected_antibodies(expected_abo, expected_rh)

    if st.button("✅ 응집원과 응집소 정답 확인"):
        st.markdown(f"**예상되는 응집원(항원)**: {', '.join(expected_antigens)}")
        st.markdown(f"**예상되는 응집소(항체)**: {', '.join(expected_antibodies)}")

        if set(selected_antigens) == set(expected_antigens):
            st.success("✅ 응집원이 정확합니다!")
        else:
            st.error("❌ 응집원이 다릅니다.")

        if set(selected_antibodies) == set(expected_antibodies):
            st.success("✅ 응집소가 정확합니다!")
        else:
            st.error("❌ 응집소가 다릅니다.")
