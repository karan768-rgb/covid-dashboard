# COVID-19 Dashboard (India)

A fully interactive data visualization dashboard built using **Dash (Plotly)** to analyze COVID-19 case data across India.
This project provides real-time insights into case distribution, recovery trends, and state-wise impact.

---

## Live Demo

https://covid-dashboard-qvew.onrender.com

---

## Features

* Interactive dashboard built with Dash & Plotly
* Real-time filtering using dropdown (All / Hospitalized / Recovered / Deceased)
* Key metrics overview:

  * Total Cases
  * Active Cases
  * Recovered Cases
  * Death Cases
  * Recovery Rate
  * Mortality Rate
* State-wise case distribution visualization
* Top 5 affected states analysis
* Clean dark UI using Bootstrap theme

---

## Tech Stack

* Python
* Dash (Plotly)
* Pandas
* NumPy
* Plotly Graph Objects
* Dash Bootstrap Components

---

## Project Structure

```
covid-dashboard/
│
├── main.py                 # Main application file
├── requirements.txt        # Dependencies
├── IndividualDetails.csv   # Dataset
└── README.md
```
## Data Source

The dataset used (`IndividualDetails.csv`) contains:

* Current status (Hospitalized, Recovered, Deceased)
* State information
* Case-level records
---

## Key Insights

* Majority of cases are active at early stages
* Significant variation across states
* Recovery and mortality rates provide quick health indicators

---

## Future Improvements

* Time-series analysis (cases over time)
* State-wise map visualization
* API-based live data integration
* Search & filtering by district
* Export reports (PDF/CSV)
* Mobile responsive UI improvements

---

👨‍💻 Author

Karan Kaushik

📧 karankaushik83336@gmail.com
🔗 https://github.com/karan768-rgb

⭐ If you like this project

Consider giving it a star on GitHub.

## License

This project is open-source and available for learning and development purposes.
