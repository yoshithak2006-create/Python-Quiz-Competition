import streamlit as st
import pandas as pd
from questions import questions
from certificate import create_certificate

st.set_page_config(
    page_title="Python Quiz Competition",
    page_icon="🏆",
    layout="centered"
)

st.title("🏆 PYTHON QUIZ COMPETITION 2026")
st.subheader("Developed by K. Yoshitha")

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    name = st.text_input("👤 Enter Student Name")
    roll = st.text_input("🆔 Enter Roll Number")

    st.markdown("""
### 📋 Instructions

✅ Total Questions : 50

✅ Time : 90 Seconds

✅ No Negative Marks

✅ Click Submit After Completing Quiz
""")

    if st.button("🚀 Start Quiz"):

        if name == "" or roll == "":
            st.warning("Please Enter Name and Roll Number")

        else:
            st.session_state.started = True
            st.session_state.name = name
            st.session_state.roll = roll
            st.rerun()

else:

    st.success(f"Welcome {st.session_state.name}")

    answers = []

    for i, q in enumerate(questions):

        st.subheader(q["question"])

        ans = st.radio(
            "Select Answer",
            q["options"],
            key=i
        )

        answers.append(ans)

    if st.button("✅ Submit Quiz"):

        score = 0

        for i, q in enumerate(questions):

            if answers[i].startswith(q["answer"]):
                score += 1

        st.success(f"🎉 Your Score : {score}/{len(questions)}")

        with open("results.csv","a") as f:
            f.write(f"{st.session_state.name},{st.session_state.roll},{score}\n"
            )
            pdf = create_certificate(
            st.session_state.name,
            score
        )

        with open(pdf, "rb") as file:
            st.download_button(
                label="📄 Download Certificate",
                data=file,
                file_name=pdf,
                mime="application/pdf"
            )

        st.write("## 🏆 Leaderboard")

        try:
            df = pd.read_csv(
                "results.csv",
                names=["Name", "Roll", "Score"]
            )

            df["Score"] = pd.to_numeric(df["Score"])

            df = df.sort_values(
                by="Score",
                ascending=False
            )

            st.dataframe(df, use_container_width=True)

        except Exception:
            st.info("No Results Yet")