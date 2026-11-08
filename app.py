import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Acadivanta",
    page_icon="🎓",
    layout="wide"
)

multiclass_model = joblib.load("multiclass_model.pkl")
binary_model = joblib.load("binary_model.pkl")
regression_model = joblib.load("regression_model.pkl")


df = pd.read_csv("data.csv", sep=";")
df.columns = df.columns.str.strip()


categorical_cols = [
    "Marital status",
    "Application mode",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation"
]

feature_cols = [
    "Marital status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Previous qualification (grade)",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Admission grade",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
    "Unemployment rate",
    "Inflation rate",
    "GDP"
]

st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
    color: #2563EB;
}
.subtitle {
    color: #64748B;
    font-size: 16px;
}
div[data-testid="stMetric"] {
    background-color: rgba(128, 128, 128, 0.08);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(128, 128, 128, 0.2);
}
</style>
""", unsafe_allow_html=True)


st.sidebar.title("🎓 Acadivanta")
st.sidebar.caption(
    "Student Analytics & Intelligence"
)
st.sidebar.divider()
st.sidebar.markdown("### Project Overview")
st.sidebar.write(
    "An ML-based system for analysing student academic "
    "outcomes and identifying students who may need support."
)
st.sidebar.divider()
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Student Prediction",
        "About Project"
    ]
)
st.sidebar.divider()
st.sidebar.caption(
    "Built with Python, Scikit-learn & Streamlit"
)
st.sidebar.divider()
st.sidebar.markdown("### 👨‍💻 Developed by")
st.sidebar.write("**Shashank Parmar**")
st.sidebar.markdown(
    "[🔗 LinkedIn Profile](https://www.linkedin.com/in/shashankmeaw/)"
)

st.markdown(
    '<p class="main-title">🎓 Acadivanta</p>',
    unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitle">Student Analytics & Intelligence | Predict. Understand. Improve.</p>',
    unsafe_allow_html=True
)
st.divider()


if page == "Dashboard":
    st.header("📊 Project Dashboard")
    st.write(
        "Welcome to Acadivanta. Explore student academic "
        "outcomes using machine learning."
    )
    st.info(
        "Navigate through the sidebar to explore predictions "
        "and project information."
    )

    st.subheader("📁 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ML Models", "3")
    with col2:
        st.metric("Dataset Records", f"{len(df):,}")
    with col3:
        st.metric("Input Features", len(feature_cols))
    st.divider()

    st.subheader("📈 Model Performance")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Multiclass Accuracy",
            "74.92%"
        )
    with col2:
        st.metric(
            "Dropout Model Accuracy",
            "86.55%"
        )
    with col3:
        st.metric(
            "Regression R² Score",
            "53.37%"
        )
    st.caption(
        "Metrics are based on the previously evaluated test datasets."
    )
    st.divider()
    st.subheader("🎯 Project Objectives")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Academic Outcome Prediction**

        - Graduate prediction
        - Dropout prediction
        - Enrolled prediction
        """)
    with col2:
        st.markdown("""
        **Academic Performance Analysis**

        - Dropout probability estimation
        - Second-semester grade estimation
        - Early identification of students who may need support
        """)
    st.progress(0.8655)
    st.caption(
        "Dropout model test accuracy: 86.55% "
        "(not an individual student's risk score)."
    )
elif page == "Student Prediction":
    st.header("🔍 Student Prediction")
    st.write(
        "Enter student information to generate machine learning predictions."
    )
    st.info(
        "The form uses admission and first-semester information."
    )
    with st.form("student_form"):
        input_data = {}
        col1, col2 = st.columns(2)
        for i, col in enumerate(feature_cols):
            current_col = col1 if i % 2 == 0 else col2
            with current_col:
                if col in categorical_cols:
                    options = sorted(
                        df[col].unique().tolist()
                    )
                    input_data[col] = st.selectbox(
                        col,
                        options
                    )
                else:
                    input_data[col] = st.number_input(
                        col,
                        min_value=float(df[col].min()),
                        max_value=float(df[col].max()),
                        value=float(df[col].median())
                    )
        submit = st.form_submit_button(
            "🚀 Generate Predictions",
            use_container_width=True
        )

    if submit:
        input_df = pd.DataFrame(
            [input_data],
            columns=feature_cols
        )
        st.success(
            "Student information submitted successfully!"
        )

        outcome = multiclass_model.predict(input_df)[0]

        dropout_probability = binary_model.predict_proba(
            input_df
        )[0][
            list(binary_model.classes_).index(1)
        ]

        predicted_grade = regression_model.predict(
            input_df
        )[0]

        st.divider()
        st.header("📊 Prediction Results")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Predicted Academic Outcome",
                outcome
            )
        with col2:
            st.metric(
                "Estimated Dropout Probability",
                f"{dropout_probability * 100:.2f}%"
            )
            st.progress(float(dropout_probability))
        with col3:
            st.metric(
                "Predicted 2nd Semester Grade",
                f"{predicted_grade:.2f}"
            )
        st.warning(
            "The grade model was trained using records with "
            "positive second-semester grades. Its estimate is "
            "conditional on that training subset."
        )
        st.info(
            "These predictions are estimates based on historical data. "
            "The three models operate independently. Results should "
            "support student guidance, not determine a student's future."
        )

elif page == "About Project":
    st.header("ℹ️ About Acadivanta")
    st.write(
        "Acadivanta is a machine learning project designed "
        "to analyse student academic performance and support "
        "early identification of students who may need assistance."
    )
    st.divider()
    st.subheader("🚀 Project Features")
    st.markdown("""
    **1. Multiclass Classification**

    Predicts three academic outcomes:
    - Graduate
    - Dropout
    - Enrolled

    **2. Binary Classification**

    Estimates the probability of a student belonging to the Dropout class.

    **3. Regression**

    Estimates the student's second-semester grade using admission
    and first-semester information.
    """)
    st.divider()
    st.subheader("🛠️ Technologies Used")
    st.markdown("""
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Scikit-learn
    - Streamlit
    - Joblib
    """)
    st.divider()
    st.subheader("📂 Dataset Information")
    st.write(
        "Dataset: UCI Predict Students' Dropout and Academic Success"
    )
    st.write(f"Total Records: {len(df)}")
    st.write(f"Input Features: {len(feature_cols)}")
    st.divider()
    st.subheader("⚠️ Disclaimer")
    st.write(
        "This project is an educational machine learning system. "
        "Its predictions are estimates based on historical data "
        "and should not be treated as definitive decisions about students."
    )