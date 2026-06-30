



# EcoPulse AI: Live Global Inflation & Energy Price Dynamics Dashboard

This repository houses **EcoPulse AI**, an interactive Data Analytics dashboard built with Streamlit. Instead of using static downloaded files, this project leverages **Automated API Integration** to fetch real-time macroeconomic indicators directly from global databases.

## 🔌 Automated API Live Data Pipeline
The core strength of this project is its dynamic data pipeline:
* **Global Inflation Data:** Fetched programmatically using the official **World Bank API** to fetch the latest Consumer Price Index (CPI) across nations.
* **Energy Price Data:** Extracted directly using live financial API connectors to track the real-time daily/monthly movements of **Brent Crude Oil Prices**.

The system automatically merges these two live streams into a unified timeline (`EcoPulse_Master_Dataset.csv`) for real-time analysis.

---

## 📊 Repository Components
1. `app.py`: The production-ready Streamlit application delivering the interactive user interface and running the live API connectors.
2. `EcoPulse_Core_Engine.ipynb`: Jupyter Notebook documenting the API prototyping, data merging logic, and exploratory data analysis (EDA).
3. `EcoPulse_Master_Dataset.csv`: The combined master dataset generated via live API integration.
4. `Global_Inflation_CPI.csv` & `Brent_Crude_Oil_Prices.csv`: Localized caches of the raw data fetched through the APIs.
5. `EcoPulse_Analysis_Chart.png`: Visualization showcasing the dynamic correlation between oil spikes and inflation pulses.

---

## 🛠️ Key Features of the Dashboard
* **Live API Data Fetching:** Zero manual downloading; data refreshes automatically via Python scripts hitting the World Bank and financial APIs.
* **Dynamic Correlation Analytics:** Interactive overlay charts displaying how spikes in Brent Crude Oil directly impact global inflation trends across historical milestones.
* **Interactive UI:** Built using Streamlit sliders and toggles, allowing users to seamlessly manipulate timeframes and analyze economic volatility.

---

## 💻 Tech Stack & Libraries Used
* **Core Language:** Python
* **Web Framework:** Streamlit
* **API Integration:** Requests / API Client Libraries (World Bank & Financial Data Engines)
* **Data Manipulation & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
* **Version Control:** GitHub Portfolio Pipeline


https://github.com/user-attachments/assets/25e4b0ab-a4a4-4d4e-b91d-0c4a150cc25c


