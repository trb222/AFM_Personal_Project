import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

# Load the updated dataset with SIC descriptions
data = load_data(r"C:\Users\thoma\Downloads\merged_filtered_wrds_with_sic_descriptions.csv")

# App Title
st.title("Mergers & Acquisitions Candidate Screening Tool")

# Sidebar for user-defined inputs
st.sidebar.header("Screening Parameters")

# Add EBITDA Filter
min_ebitda = st.sidebar.number_input("Minimum EBITDA", value=None, step=1.0, placeholder="0.0")
max_ebitda = st.sidebar.number_input("Maximum EBITDA", value=None, step=1.0, placeholder="(Leave blank for no max)")

# Add filters for each numeric ratio with human-readable labels
numeric_filters = {}
st.sidebar.write("### Ratio Screening Options")

# Mapping for human-readable labels
label_mapping = {
    "roa": "Return on Assets",
    "roe": "Return on Equity",
    "npm": "Net Profit Margin",
    "de_ratio": "Debt to Equity Ratio",
    "debt_ebitda": "Debt/EBITDA",
    "ebitda": "EBITDA"
}

for col, label in label_mapping.items():
    if col != "ebitda":  # EBITDA already has its own separate filter
        min_val = st.sidebar.number_input(
            f"Minimum {label}", 
            value=None, 
            step=0.1, 
            placeholder="(No minimum)"
        )
        max_val = st.sidebar.number_input(
            f"Maximum {label} (leave blank for no maximum)", 
            value=None, 
            step=0.1, 
            placeholder="(No maximum)"
        )
        numeric_filters[col] = (min_val, max_val)

# Industry (Description) Dropdown Filter
industry_options = sorted(data["description"].dropna().unique().tolist())
selected_industry = st.sidebar.selectbox("Select Industry (optional)", options=["All"] + industry_options)

# Filter dataset based on user inputs
filtered_data = data

# Apply EBITDA filter
if min_ebitda is not None:
    filtered_data = filtered_data[filtered_data["ebitda"] >= min_ebitda]
if max_ebitda is not None:
    filtered_data = filtered_data[filtered_data["ebitda"] <= max_ebitda]

# Apply numeric filters
for col, (min_val, max_val) in numeric_filters.items():
    if min_val is not None:
        filtered_data = filtered_data[filtered_data[col] >= min_val]
    if max_val is not None:
        filtered_data = filtered_data[filtered_data[col] <= max_val]

# Apply industry filter
if selected_industry != "All":
    filtered_data = filtered_data[filtered_data["description"] == selected_industry]

# Rename columns for better readability
filtered_data = filtered_data.rename(columns=label_mapping)

# Remove SIC and sector columns if they exist
columns_to_remove = ["gsector", "sic"]
for col in columns_to_remove:
    if col in filtered_data.columns:
        filtered_data = filtered_data.drop(columns=[col])

# Display filtered results without row numbers
st.write("### Filtered Results")
st.dataframe(filtered_data.reset_index(drop=True))  # Reset index to remove row numbers

# Visualizations for all selection criteria
if not filtered_data.empty:
    st.write("### Visualizations")

    # Dropdown to select a metric for visualization
    visualization_metric = st.selectbox(
        "Select a metric to visualize:",
        options=list(label_mapping.values())
    )

    # Generate a bar chart for the selected metric
    fig = px.bar(
        filtered_data,
        x="TICKER",
        y=visualization_metric,  # Use the updated column name
        title=f"{visualization_metric} by Company",
        labels={"TICKER": "Company", visualization_metric: visualization_metric}
    )
    st.plotly_chart(fig)

# Reporting Module with Full Column Names and Industry Names
if st.button("Generate Report"):
    st.write("### Report Summary")

    # Rename columns for better readability
    summary = filtered_data.describe(include="all").transpose()

    st.write("### Summary Statistics")
    st.write(summary)

    # Add Yahoo Finance links for each ticker
    st.write("### Yahoo Finance Links")
    for ticker in filtered_data["TICKER"].dropna().unique():
        yahoo_url = f"https://finance.yahoo.com/quote/{ticker}"
        st.markdown(f"- [{ticker}]({yahoo_url})")

    st.download_button(
        label="Download Results as CSV",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_results.csv",
        mime="text/csv",
    )
