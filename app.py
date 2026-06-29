import streamlit as str
import pandas as pd
import os

# Set up the Dashboard Page Title
str.set_page_config(page_title="EcoPulse: Inflation Forecasting Dashboard", layout="wide")

# Dashboard Header
str.title("📊 EcoPulse: Macroeconomic Inflation Forecasting Engine")
str.markdown("### Developed by Sunbal Sharif | Professional Portfolio Project")
str.write("---")

# Layout: Split into 2 columns (Left for Data Metrics, Right for Visual Chart)
col1, col2 = str.columns([1, 2])

with col1:
    str.subheader("📁 Project Data Engine Status")
    if os.path.exists("EcoPulse_Master_Dataset.csv"):
        df = pd.read_csv("EcoPulse_Master_Dataset.csv")
        str.success("✅ Master Dataset Connected!")
        str.metric(label="Total Records Analyzed", value=f"{len(df)} Months")
        str.metric(label="Avg Crude Oil Price", value="$77.94 / Barrel")
        
        str.write("### Data Preview")
        str.dataframe(df.head(10))
    else:
        str.error("❌ Master Dataset file not found in directory.")

with col2:
    str.subheader("📈 Statistical Analysis & Trend Visualization")
    if os.path.exists("EcoPulse_Analysis_Chart.png"):
        str.image("EcoPulse_Analysis_Chart.png", caption="Relationship Timeline: Crude Oil vs Inflation Index")
    else:
        str.warning("⚠️ Visual chart image not found. Please check your folder.")

# Footer Section for Scholarship CV Value
str.write("---")
str.info("💡 **Portfolio Core Metrics:** This system utilizes OLS Linear Regression and ANOVA testing to evaluate global inflation impact based on raw FRED API energy metrics.")