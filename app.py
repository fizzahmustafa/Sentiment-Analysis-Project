import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="AI Sentiment Analysis Dashboard",
    page_icon="🤖",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 Dashboard")

st.sidebar.success("API Status: Active")

st.sidebar.info("""
### Project Information

AI Based Sentiment Analysis System

**Algorithm:** LinearSVC

**Vectorization:** TF-IDF

**Backend API:** Flask

**Frontend:** Streamlit

**Language:** Python
""")

st.sidebar.markdown("---")

st.sidebar.write("### Features")
st.sidebar.write("✅ Sentiment Prediction")
st.sidebar.write("✅ Text Statistics")
st.sidebar.write("✅ Prediction History")
st.sidebar.write("✅ Flask API Integration")

st.markdown(
    "<div class='main-title'>🤖 AI Sentiment Analysis Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown("---")

user_text = st.text_area(
    "📝 Enter Text",
    height=180,
    placeholder="Type a review, comment or tweet..."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "LinearSVC")

with col2:
    st.metric("Vectorizer", "TF-IDF")

with col3:
    st.metric("Status", "Ready")

if st.button("🚀 Analyze Sentiment"):

    if user_text.strip():

        try:
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"text": user_text}
            )

            prediction = response.json()["sentiment"]

            words = len(user_text.split())
            chars = len(user_text)

            st.markdown("## 📌 Prediction Result")

            if str(prediction).lower() == "positive":
                st.success("😊 POSITIVE")

            elif str(prediction).lower() == "negative":
                st.error("😞 NEGATIVE")

            else:
                st.info("😐 NEUTRAL")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Word Count", words)

            with c2:
                st.metric("Character Count", chars)

            st.session_state.history.append(
                {
                    "Text": user_text[:60],
                    "Prediction": prediction
                }
            )

        except Exception as e:
            st.error(f"API Connection Error: {e}")

    else:
        st.warning("Please enter some text.")

st.markdown("---")

st.subheader("📜 Prediction History")

if st.session_state.history:

    df = pd.DataFrame(st.session_state.history[::-1])

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No predictions made yet.")

st.markdown("---")

st.subheader("💡 Example Inputs")

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        "I absolutely loved this service and would recommend it."
    )

with c2:
    st.info(
        "The meeting starts tomorrow at 9 AM."
    )

with c3:
    st.error(
        "This was the worst experience I have ever had."
    )

st.markdown("---")

st.caption(
    "BS Artificial Intelligence Project | Sentiment Analysis using LinearSVC, TF-IDF, Flask API and Streamlit"
)

