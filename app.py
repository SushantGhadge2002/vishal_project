import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import requests

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="Heart Disease Dashboard",
    page_icon="❤️",
    layout="wide"
)

# ---------------------------------------
# Load Dataset
# ---------------------------------------
df = pd.read_csv("heart_disease_cleaned.csv")

# ---------------------------------------
# Sidebar
# ---------------------------------------
st.sidebar.title("❤️ Heart Disease Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Dashboard", "About"]
)

# =======================================
# HOME PAGE
# =======================================
if menu == "Home":

    st.title("❤️ Heart Disease Prediction Dashboard")

    st.markdown("---")

    st.write("""
Welcome to the Heart Disease Prediction Dashboard.

This dashboard allows users to explore the Heart Disease Dataset interactively.
It includes interactive filters, charts, live data tables, and an external REST API.
""")

    st.info("Select Dashboard from the sidebar to explore the dataset.")

    # ---------------------------------------
    # External REST API
    # ---------------------------------------
    st.subheader("🌐 Live API Data")

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:

        api_data = response.json()

        st.success("API Connected Successfully")

        st.write("### Sample API Response")

        st.write("**Post ID:**", api_data["id"])
        st.write("**User ID:**", api_data["userId"])
        st.write("**Title:**", api_data["title"])

    else:

        st.error("Unable to fetch API data.")

# =======================================
# DASHBOARD PAGE
# =======================================
elif menu == "Dashboard":

    st.title("📊 Interactive Dashboard")

    st.subheader("🔍 Filter Patients")

    # ---------------------------------------
    # Age Slider
    # ---------------------------------------
    age_range = st.slider(
        "Age Range",
        int(df["age"].min()),
        int(df["age"].max()),
        (
            int(df["age"].min()),
            int(df["age"].max())
        )
    )

    # ---------------------------------------
    # Cholesterol Slider
    # ---------------------------------------
    chol_range = st.slider(
        "Cholesterol Range (mg/dL)",
        int(df["chol"].min()),
        int(df["chol"].max()),
        (
            int(df["chol"].min()),
            int(df["chol"].max())
        )
    )

    # ---------------------------------------
    # Blood Pressure Slider
    # ---------------------------------------
    bp_range = st.slider(
        "Resting Blood Pressure (mm Hg)",
        int(df["trestbps"].min()),
        int(df["trestbps"].max()),
        (
            int(df["trestbps"].min()),
            int(df["trestbps"].max())
        )
    )

    # ---------------------------------------
    # Exercise Chest Pain
    # ---------------------------------------
    exang_mapping = {
        "All": None,
        "Yes": 1,
        "No": 0
    }

    exang_choice = st.selectbox(
        "Chest Pain During Exercise",
        list(exang_mapping.keys())
    )

    # ---------------------------------------
    # Apply Filters
    # ---------------------------------------
    filtered_df = df[
        (df["age"] >= age_range[0]) &
        (df["age"] <= age_range[1]) &
        (df["chol"] >= chol_range[0]) &
        (df["chol"] <= chol_range[1]) &
        (df["trestbps"] >= bp_range[0]) &
        (df["trestbps"] <= bp_range[1])
    ]

   
    # Exercise Chest Pain Filter
    if exang_mapping[exang_choice] is not None:
        filtered_df = filtered_df[
            filtered_df["exang"] == exang_mapping[exang_choice]
        ]

    # ---------------------------------------
    # Dashboard Summary
    # ---------------------------------------
    st.subheader("📌 Dashboard Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Patients", len(filtered_df))

    with c2:
        st.metric(
            "Heart Disease",
            int(filtered_df["target_binary"].sum())
        )

    with c3:
        st.metric(
            "No Disease",
            int((filtered_df["target_binary"] == 0).sum())
        )

    with c4:
        if len(filtered_df) > 0:
            st.metric(
                "Average Age",
                round(filtered_df["age"].mean(), 1)
            )
        else:
            st.metric("Average Age", "0")

    # ---------------------------------------
    # Data Table
    # ---------------------------------------
    st.subheader("📋 Filtered Dataset")

    st.dataframe(filtered_df)

    # ---------------------------------------
    # Check Empty Dataset
    # ---------------------------------------
    if filtered_df.empty:
        st.warning("No records found for the selected filters.")
        st.stop()

    # ---------------------------------------
    # Bar Chart
    # ---------------------------------------
    st.subheader("📊 Heart Disease Distribution")

    bar_data = (
        filtered_df["target_binary"]
        .value_counts()
        .rename({
            0: "No Disease",
            1: "Heart Disease"
        })
    )

    st.bar_chart(bar_data)

    # ---------------------------------------
    # Histogram
    # ---------------------------------------
    st.subheader("📈 Age Distribution")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(filtered_df["age"], bins=10)

    ax.set_xlabel("Age")

    ax.set_ylabel("Patients")

    ax.set_title("Age Distribution")

    st.pyplot(fig)

    # ---------------------------------------
    # Pie Chart
    # ---------------------------------------
    st.subheader("🥧 Heart Disease Percentage")

    pie_data = (
        filtered_df["target_binary"]
        .value_counts()
        .reset_index()
    )

    pie_data.columns = [
        "Disease Status",
        "Count"
    ]

    pie_data["Disease Status"] = pie_data["Disease Status"].replace(
        {
            0: "No Disease",
            1: "Heart Disease"
        }
    )

    fig_pie = px.pie(
        pie_data,
        names="Disease Status",
        values="Count",
        title="Heart Disease Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )
    
          # ---------------------------------------
    # Chart 4 : Cholesterol vs Heart Disease
    # ---------------------------------------

    st.subheader("📊 Cholesterol Distribution by Heart Disease Status")

    chol_data = filtered_df.copy()

    chol_data["Disease Status"] = chol_data["target_binary"].replace(
        {
            0: "No Disease",
            1: "Heart Disease"
        }
    )

    fig_box = px.box(
        chol_data,
        x="Disease Status",
        y="chol",
        color="Disease Status",
        title="Cholesterol Level Comparison"
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )
# =======================================
# ABOUT PAGE
# =======================================
else:

    st.title("ℹ️ About Project")

    st.write("""
### ❤️ Project Name

Heart Disease Prediction Dashboard

### 📂 Dataset

UCI Cleveland Heart Disease Dataset

### 🚀 Features

- Interactive Age Filter
- Cholesterol Filter
- Blood Pressure Filter
- Chest Pain Type Filter
- Exercise Chest Pain Filter
- Live Data Table
- Dashboard Summary
- Bar Chart
- Histogram
- Pie Chart
- External REST API Integration

### 🛠 Tools Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly
- Requests
- Scikit-learn

Developed as a Capstone Project.
""")