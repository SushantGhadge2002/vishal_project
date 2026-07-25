# ❤️ Heart Disease Prediction Dashboard

## Project Overview

This project is an interactive Streamlit dashboard built using the UCI Cleveland Heart Disease Dataset.

The dashboard allows users to explore the dataset through interactive filters, visualizations, and a live external API. It helps users understand heart disease trends in a simple and user-friendly way.

---

## Dataset

**Dataset:** UCI Cleveland Heart Disease Dataset

The dataset contains patient medical information such as age, blood pressure, cholesterol level, heart rate, and other clinical features used to analyze heart disease.

---

## Features

This dashboard includes the following interactive features:

- Interactive Age Filter (Slider)
- Live Data Table
- Bar Chart
- Histogram
- Pie Chart
- External REST API Integration

All charts and the data table update automatically based on the selected age range.

---

## Dashboard Visualizations

The dashboard contains three interactive visualizations:

1. **Bar Chart** – Shows the number of patients with and without heart disease.
2. **Histogram** – Displays the distribution of patient ages.
3. **Pie Chart** – Shows the percentage of patients with and without heart disease.

These charts change dynamically according to the selected filter.

---

## External API

**API Used:**

https://jsonplaceholder.typicode.com/posts/1

**HTTP Method:**

GET

**Displayed Fields:**

- Post ID
- User ID
- Title

The dashboard sends a GET request to the JSONPlaceholder REST API using the Python `requests` library. The API returns sample JSON data, and selected fields are displayed on the Home page.

---

## Technologies Used

The project was developed using the following technologies:

- Python

- Streamlit  
  Used to create the interactive dashboard.

- Pandas  
  Used for loading and processing the CSV dataset.

- Matplotlib  
  Used to create the Age Distribution histogram.

- Plotly  
  Used for interactive Pie Chart and Cholesterol Box Plot.

- Requests  
  Used to connect with the external REST API.

- Scikit-learn  
  Included for machine learning related functionality.
---

## How to Run the Project

1. Install the required libraries using:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

streamlit run app.py
```

3. The dashboard will open automatically in your web browser.

---

## Streamlit Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live Dashboard URL:**

(Add your Streamlit Community Cloud URL here after deployment.)

---

## Project Summary

This project demonstrates how Machine Learning datasets can be transformed into an interactive dashboard using Streamlit. It combines data visualization, filtering, live API integration, and an easy-to-use interface, making it suitable for both technical and non-technical users.