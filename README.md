# PhonePe UPI Transaction Insights (National Level)
This project analyzes India's UPI transaction trends using data from the official ([PhonePe Pulse](https://www.phonepe.com/pulse/)) GitHub repository. The analysis focuses on **national-level transaction types** over time and presents visual insights through an interactive Streamlit dashboard.

## Project Structure
 phonepe-upi-insights/
├── app.py # Streamlit dashboard  link - ([Streamlit link](https://phonepeproject-jru4nwepappvx8j2efuu5xx.streamlit.app/))
├── report.pdf # Final report 
├── requirements.txt # Python dependencies
├── final_aggregated_data.csv # Cleaned transaction data
├── quarterly_trend.csv # Quarterly growth data
├── top_transaction_types.csv # Ranked transaction types
├── phonepe_data.db # SQLite database

## Tech Stack
- **Python** (Pandas, Plotly, SQLite)
- **Google Colab** (Data extraction & preprocessing)
- **Streamlit** (Dashboard UI)
- **Plotly** (Interactive charts)

## Features
-  Filter by year and quarter
-  Pie chart of transaction types
-  Bar chart of top transaction types (all time)
-  Line chart for quarterly trends
-  Downloadable CSVs and SQLite DB
-  Simple, clean UI with sidebar controls

##  Sample KPIs Displayed

-  Total UPI Amount (in Trillions)
-  Total Number of Transactions (in Billions)
-  Most popular transaction type

##  Run the Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Data Source
All data is sourced from the open-source repository:
([Data link]https://github.com/PhonePe/pulse)

## Future Scope
- Add state-wise and district-wise maps
- Include insurance & user metrics
- Add ML-based fraud detection or segmentation
