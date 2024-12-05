# AFM_Personal_Project
Advanced Financial Modeling Personal Project (M&A Screener)


Link to Run Program (EASIEST WAY TO RUN), copy into any browser
(https://afmpersonalproject-iziwxrzmsewnhwdgajj6yp.streamlit.app/)

**Mergers & Acquisitions Candidate Screening Tool**

Overview

The Mergers & Acquisitions Candidate Screening Tool is a web application built using Streamlit. It helps users filter and analyze companies based on specific financial metrics and criteria, providing a streamlined way to screen M&A candidates. The app integrates data visualization and report generation features to support data-driven decision-making. This app is tailored towards investment banks or private equity firms.

**Features**

    1. Screening Parameters
    Filter by EBITDA:
    Minimum and maximum values can be specified.
    Apply numeric filters for key financial ratios:
    Return on Assets (ROA %)
    Return on Equity (ROE %)
    Net Profit Margin (NPM %)
    Debt to Equity Ratio
    Debt/EBITDA
    Industry-based filtering:
    Select specific industries from a dropdown menu.
    All filters are optional and customizable.
    2. Dynamic Results
    Displays a filtered dataset based on user-defined criteria.
    Removes unnecessary columns (e.g., SIC, GICS sector) for cleaner presentation.
    Renames columns for better readability.
    3. Interactive Visualizations
    Generate bar charts for selected metrics (e.g., ROA, ROE, EBITDA) by company.
    Visualize data dynamically based on filtered results.
    4. Reporting Module
    Summarize results with descriptive statistics.
    Includes Yahoo Finance links for filtered companies' tickers.
    Allows users to download filtered results as a CSV file for further analysis.
    Getting Started
    Prerequisites
    Install Python (3.8 or higher).

**Install required Python packages:**


    pip install streamlit pandas plotly

**Ensure your dataset is available in the same directory as the app:**

    Filename: merged_filtered_wrds_with_sic_descriptions.csv
    The dataset must contain the following columns:
    TICKER, roa, roe, npm, de_ratio, debt_ebitda, ebitda, description, gsector, sic

**Running the Application**

    Save the script as app.py.
    
    Run the application:
    
    streamlit run app.py
    Open the app in your browser (Streamlit will provide a URL).

**Dataset Details**

    Required Columns:
    TICKER: Company ticker symbol.
    roa, roe, npm: Financial performance metrics as ratios (will be converted to percentages).
    de_ratio, debt_ebitda, ebitda: Additional financial metrics.
    description: Industry description for filtering.
    gsector, sic: Optional columns that will be removed from the output.
    Ensure the dataset is clean and properly formatted before running the app.

**How to Use**

    Set Screening Parameters:
    
    Input values for EBITDA and numeric ratios in the sidebar.
    Optionally, filter by industry using the dropdown menu.
    
    View Filtered Results:
    
    The main page will display results matching your criteria.
    Reset index ensures row numbers do not appear in the results table.
    
    Visualize Data:
    
    Use the dropdown to select a metric for visualization.
    Generate a bar chart for easy comparison across companies.
    
    Generate Reports:
    
    View a summary of filtered results.
    Access Yahoo Finance links for additional information.
    Download results as a CSV file for external use.

    EXAMPLE CRITERIA:
    For a company with high profitability and low debt
    EBITDA:
        Minimum: 50 (e.g., $50M)
        Maximum: Leave blank (no maximum)
    Return on Assets (ROA %):
        Minimum: 10%
        Maximum: Leave blank
    Return on Equity (ROE %):
        Minimum: 15%
        Maximum: Leave blank
    Net Profit Margin (NPM %):
        Minimum: 20%
        Maximum: Leave blank
    Debt to Equity Ratio:
        Maximum: 0.5
    Industry:
        Select: "Semiconductors and related devices"

**Technical Details**

    Data Caching
    The app uses Streamlit’s @st.cache_data to cache the loaded dataset, ensuring efficient performance.
    
    Customizable Filters
    Filters for numeric ratios are created dynamically based on column names and human-readable labels.
    
    Visualization
    Plotly Express is used for creating bar charts, ensuring interactive and visually appealing graphics.
    
    Report Generation
    Summary statistics are calculated using pandas' describe function.
    Download functionality allows easy access to filtered datasets.

**Known Issues**

    Ensure the dataset matches the expected format. Missing or misnamed columns may cause errors.
    When filtering industries, ensure the description column contains valid data.

**Future Enhancements**

    Add support for additional data sources or APIs for real-time data updates.
    Introduce multi-metric visualization and comparison charts.
    Enhance reporting features with PDF export options.



**Acknowledgments**
    
      Streamlit for enabling the creation of interactive applications.
      Pandas, Matplotlib, and Seaborn for data manipulation and visualization tools.
