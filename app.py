import streamlit as st
import pandas as pd
import time

from questions import questions
from certificate import create_certificate


st.set_page_config(
    page_title="Python Quiz Competition",
    page_icon="🏆",
    layout="centered"
)


# Title

st.markdown(
    """
    <h1 style='text-align:center;color:#1E40AF;'>
    🏆 PYTHON QUIZ COMPETITION 2026
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h3 style='text-align:center;color:green;'>
    Developed by K. Yoshitha
    </h3>
    """,
    unsafe_allow_html=True
)



if "started" not in st.session_state:
    st.session_state.started = False



# LOGIN PAGE

if not st.session_state.started:


    name = st.text_input(
        "👤 Enter Student Name"
    )


    roll = st.text_input(
        "🆔 Enter Roll Number"
    )



    st.markdown(
        """
        <div style="
        background-color:#EFF6FF;
        padding:20px;
        border-radius:15px;
        border:2px solid #1E40AF;
        ">

        <h3>📋 Instructions</h3>

        ✅ Total Questions : 50

        <br><br>

        ✅ Time : 90 Seconds

        <br><br>

        ✅ No Negative Marks

        <br><br>

        ✅ Certificate After Completion

        </div>
        """,
        unsafe_allow_html=True
    )



    if st.button("🚀 Start Quiz"):


        if name == "" or roll == "":

            st.warning(
                "Please Enter Name and Roll Number"
            )


        else:

            st.session_state.started = True

            st.session_state.name = name

            st.session_state.roll = roll

            st.session_state.start_time = time.time()

            st.rerun()



# QUIZ PAGE

else:


    st.markdown(
        f"""
        <div style="
        background-color:#DCFCE7;
        padding:15px;
        border-radius:15px;
        border:2px solid #16A34A;
        text-align:center;
        ">

        <h2>
        👋 Welcome {st.session_state.name}
        </h2>

        <p>
        All the best for your quiz! 🏆
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    elapsed = int(
        time.time() - st.session_state.start_time
    )


    remaining = max(
        0,
        90 - elapsed
    )


    st.markdown(
        f"""
        <div style="
        background-color:#FEF3C7;
        padding:15px;
        border-radius:15px;
        border:2px solid #F59E0B;
        text-align:center;
        ">

        <h2>
        ⏱️ Time Left : {remaining} Seconds
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    if remaining == 0:

        st.error(
            "⏰ Time Over! Quiz Submitted"
        )

        st.stop()


    answers = []


    for i, q in enumerate(questions):


        st.info(
            f"📌 Question {i+1} / {len(questions)}"
        )


        st.subheader(
            q["question"]
        )


        ans = st.radio(
            "Select Answer",
            q["options"],
            key=i
        )


        answers.append(ans)
            if st.button("✅ Submit Quiz"):


        score = 0


        for i, q in enumerate(questions):


            if answers[i].startswith(
                q["answer"]
            ):

                score += 1



        st.markdown(
            f"""
            <div style="
            background-color:#DCFCE7;
            padding:20px;
            border-radius:15px;
            border:3px solid #16A34A;
            text-align:center;
            ">

            <h1>🎉 Congratulations!</h1>

            <h2>
            Your Score : {score}/{len(questions)}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )



        with open(
            "results.csv",
            "a"
        ) as f:


            f.write(
                f"{st.session_state.name},{st.session_state.roll},{score}\n"
            )



        pdf = create_certificate(
            st.session_state.name,
            score
        )



        with open(
            pdf,
            "rb"
        ) as file:


            st.download_button(

                label="📄 Download Certificate",

                data=file,

                file_name=pdf,

                mime="application/pdf"

            )



    # Leaderboard

    st.write(
        "## 🏆 Leaderboard"
    )


    try:


        df = pd.read_csv(

            "results.csv",

            names=[
                "Name",
                "Roll",
                "Score"
            ]

        )


        df["Score"] = pd.to_numeric(
            df["Score"]
        )


        df = df.sort_values(
            by="Score",
            ascending=False
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    except Exception:


        st.info(
            "No Results Yet"
        )