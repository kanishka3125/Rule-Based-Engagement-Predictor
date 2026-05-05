import streamlit as st
import pandas as pd
import logic   # ✅ IMPORTANT (do NOT change)

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Engagement Predictor", layout="wide")

# ------------------ CUSTOM UI ------------------
st.markdown("""
<style>
header[data-testid="stHeader"] {visibility: hidden;}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    margin-bottom: 12px;   /* reduced from 20px */
}

/* REMOVE empty card look */
.card:empty {
    display: none;
}


.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "result" not in st.session_state:
    st.session_state.result = None
    st.session_state.score = 0

# ------------------ HEADER ------------------
st.markdown("""
<h1 style='text-align:center; color:#00C9A7;'> Instagram Engagement Predictor</h1>
<p style='text-align:center;'>Predict • Analyze • Optimize your content strategy</p>
""", unsafe_allow_html=True)


# ------------------ INPUT ------------------


col1, col2 = st.columns(2)

with col1:
    time = st.selectbox("Time", ["morning", "afternoon", "evening", "night"])
    post_type = st.selectbox("Post Type", ["reel", "image", "carousel"])

with col2:
    hashtags = st.slider("Hashtags", 0, 20)
    duration = st.slider("Duration (sec)", 0, 60)

predict_btn = st.button("Predict Engagement")



# ------------------ PREDICTION ------------------
if predict_btn:
    st.session_state.result = logic.predict_engagement(time, hashtags, post_type, duration)
    st.session_state.score = logic.engagement_score(hashtags, duration)

# ------------------ OUTPUT ------------------
if st.session_state.result is not None:

    result = st.session_state.result
    score = int(st.session_state.score)

    # RESULT
    color = "#22c55e" if "High" in result else "#ef4444"

    st.markdown(f"""
    <div class="card" style="background: linear-gradient(90deg, {color}, #00000033); text-align:center;">
     <b style="font-size:22px;">{result}</b>
    </div>
    """, unsafe_allow_html=True)

    # EXPLANATION
    st.markdown(f"""
    <div class="card">
     {logic.explain_prediction(time, hashtags, post_type, duration)}
    </div>
    """, unsafe_allow_html=True)

    # PERFORMANCE

    st.markdown("### Performance Overview")

    c1, c2, c3 = st.columns(3)
    c1.metric("Hashtags", hashtags)
    c2.metric("Duration", duration)
    c3.metric("Score", score)

    st.markdown(f"<p style='text-align:center;'>Engagement Score: <b>{score}%</b></p>", unsafe_allow_html=True)
    st.progress(score)

    st.markdown("<p style='text-align:center; color:#facc15;'>AI Insights Enabled</p>", unsafe_allow_html=True)



    # SUGGESTIONS
   

    st.markdown("###  Suggestions")
    for s in logic.suggest_improvement(time, hashtags, post_type, duration):
        st.write(f" {s}")

    if "Low" in result:
        st.markdown("### Why NOT High?")
        for r in logic.why_not_high(time, hashtags, post_type, duration):
            st.write(f" {r}")

    

    # OPTIMIZER
    
    if st.button("Optimize My Post"):
        opt = logic.auto_optimize(time, hashtags, post_type, duration)

        st.success(f"""
        ✔ Time: {opt['time']}  
        ✔ Hashtags: {opt['hashtags']}  
        ✔ Type: {opt['post_type']}  
        ✔ Duration: {opt['duration']}
        """)

    

    # FEATURE IMPACT
    
    st.markdown("### Feature Impact")

    df = pd.DataFrame({
        "Feature": ["Hashtags", "Duration", "Reel Boost", "Evening Boost"],
        "Impact": [
            hashtags * 2,
            duration * 0.5,
            20 if post_type == "reel" else 5,
            20 if time == "evening" else 5
        ]
    })

    st.bar_chart(df.set_index("Feature"))

    

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:#aaa;'>Built with using Python & Streamlit</p>", unsafe_allow_html=True)