# Liquipedia – Esports Data Analysis Dashboard

A Streamlit-based esports analytics dashboard that performs comprehensive data analysis on competitive gaming datasets. The project provides insights into team performance, win rates, round efficiency, player statistics, and tournament predictions using historical esports data from Counter-Strike tournaments.

The application also includes web scraping modules that automatically collect esports data from Liquipedia using BeautifulSoup and Requests.

---

## Features

### Interactive Analytics Dashboard

* Streamlit-based web interface
* Dynamic filtering and dataset selection
* Interactive Plotly visualizations

### Team Performance Analysis

* Team performance metrics
* Win rate calculations
* Round difference (RD) analysis
* Playoff appearance tracking

### Round Efficiency Analysis

* Average rounds won per stage
* Average rounds lost per stage
* Round efficiency percentage rankings

### Tournament Prediction

* Tournament winner prediction
* Team qualification analysis
* Historical performance-based insights

### Player Performance Analysis

* Radar chart visualizations
* Kills, deaths, and assists analysis
* Match-by-match player statistics
* Comparative player performance metrics

### Multi-Year Data Analysis

Analyze esports data across multiple tournament years:

* 2021
* 2022
* 2023
* 2024
* Combined dataset (All Years)

### Automated Data Collection

* Liquipedia web scraping system
* Match statistics collection
* Team performance data extraction
* Player statistics gathering
* Tournament information scraping

---

## Project Structure

```text
├── app.py                                   # Main Streamlit application
├── headers.py                               # Data processing and visualization functions
├── requirements.txt                         # Project dependencies
├── README.md                                # Project documentation
│
├── Years/
│   ├── 2021.csv
│   ├── 2022.csv
│   ├── 2023.csv
│   ├── 2024.csv
│   └── AllYears.csv
│
├── Player Stats/
│   └── *.csv
│
├── Web Scrapping/
│   ├── scrapping-player_stats.ipynb
│   └── scrapping-matches_data.ipynb
│
├── bin/
│   └── img/
│       ├── Counter-Strike.png
│       └── Dota.png
```

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* BeautifulSoup
* Requests

---

## Data Source

All datasets used in this project are collected from:

* Liquipedia Counter-Strike

The web scraping modules extract:

* Match statistics
* Team performance data
* Player statistics
* Tournament information

Data is collected using:

* BeautifulSoup
* Requests

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/liquipedia-esports-analysis.git
cd liquipedia-esports-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## How It Works

### Step 1: Data Collection

Esports data is scraped from Liquipedia using BeautifulSoup and Requests.

### Step 2: Data Processing

The scraped data is cleaned, structured, and stored as CSV files.

### Step 3: Dashboard Analysis

The Streamlit application loads the datasets dynamically and allows users to select:

* Esports title
* Tournament year
* Analysis module

### Step 4: Visualization

The system generates:

* Interactive charts
* Team performance metrics
* Tournament predictions
* Radar charts for player analysis

All visualizations are powered by Plotly and displayed directly within the Streamlit dashboard.

---

## Analysis Modules

### Team Metrics

Displays:

* Average win rate
* Average round difference (RD)
* Playoff appearances

### Team Win Rate Analysis

Calculates and visualizes:

* Team win percentages
* Stage-by-stage performance
* Historical comparisons

### Rounds Per Stage

Provides:

* Average rounds won
* Average rounds lost
* Stage-specific performance metrics

### Round Efficiency Rankings

Ranks teams according to:

* Round efficiency percentage
* Overall tournament effectiveness

### Tournament Prediction

Predicts:

* Potential qualifying teams
* Likely tournament winners

### Player Analysis

Provides:

* Radar chart visualization
* Average kills
* Average deaths
* Average assists
* Match-wise performance breakdown

---

## Supported Esports

### Counter-Strike

Current analytics and datasets are focused on professional Counter-Strike tournaments and teams.

Future support can be extended to additional esports titles such as:

* Dota 2
* Valorant
* League of Legends

---

## Future Improvements

* Real-time data updates
* Machine learning-based tournament prediction
* Additional esports title support
* Advanced player comparison tools
* Team ranking system
* Automated data refresh pipeline

---

## License

This project is intended for educational and research purposes.

---

## Acknowledgements

Data provided by Liquipedia and the esports community.

Special thanks to the developers of:

* Streamlit
* Plotly
* Pandas
* BeautifulSoup
* Requests

for making data analytics and visualization accessible to developers.
