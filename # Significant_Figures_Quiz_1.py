# Significant_Figures_Quiz_1
import streamlit as st

st.title("Significant Figures Quiz")

st.subheader("Rules")
st.markdown(
"""
**Rule 1:** All nonzero digits are significant.  
**Rule 2:** If the position of a zero is between two nonzero digits, then the zero is significant.  
**Rule 3:** If the position of a zero is at the beginning of a number, then it is not significant.  
**Rule 4:** If the position of a zero is at the end of a number and after a decimal point, then it is significant.  
**Rule 5:** If the position of a zero is at the end of a number with no decimal point, then it is not significant.
"""
)

st.subheader("Questions")
st.markdown("Find the number of significant figures in each measurement:")

questions = [
    ("1. 700", 1),
    ("2. 8080", 3),
    ("3. 0.004", 1),
    ("4. 9007", 4),
    ("5. 0.1060", 4),
    ("6. 878.42", 5),
    ("7. 0.10300", 5),
    ("8. 0.00810", 3),
    ("9. 3,000,000", 1),
    ("10. 0.00506", 3),
]

user_answers = []
for label, _ in questions:
    ans = st.number_input(f"{label}", min_value=0, step=1, format="%d")
    user_answers.append(ans)

if st.button("Submit"):
    score = 0
    st.subheader("Results")
    for (label, correct), user in zip(questions, user_answers):
        is_correct = (user == correct)
        if is_correct:
            score += 1
        st.write(f"{label}: Your answer = {user}, Correct answer = {correct} — {'✅ Correct' if is_correct else '❌ Incorrect'}")

    st.markdown(f"### Your score: {score} / {len(questions)}")
