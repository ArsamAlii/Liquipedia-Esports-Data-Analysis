import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def load_data():
    """Loads and processes data for all years (2021 to 2024)."""
    data = {}
    for year in range(2021, 2025):
        file_path = f"{year}.csv"
        df = pd.read_csv(file_path)
        df.drop('Unnamed: 1', axis=1, inplace=True)  
        df.rename(columns={'Unnamed: 0': 'Stage'}, inplace=True)  

        
        df1 = df.iloc[:16].reset_index(drop=True).fillna('')
        df2 = df.iloc[16:32].reset_index(drop=True).fillna('')
        df3 = df.iloc[32:].reset_index(drop=True).fillna('')
        df_stages = pd.concat([df1, df2, df3], keys=['Opening Stage', 'Elimination Stage', 'Playoff Stage']).drop('Stage', axis=1)

        data[year] = df, df_stages

    st.write("Data for 2021 to 2024 Loaded Successfully.")
    return data


def calculate_avg_metrics(df):
    """Calculates and displays average metrics for each team."""
    team_stats = df.groupby('Team', group_keys=False).apply(_calculate_team_metrics).reset_index()
    st.write("Average Metrics for Each Team:")
    st.write(team_stats)


def _calculate_team_metrics(group):
    """Helper function to calculate metrics for a single team group."""
    total_wins = group['Matches'].apply(lambda x: int(x.split('-')[0])).sum()
    total_losses = group['Matches'].apply(lambda x: int(x.split('-')[1])).sum()
    total_matches = total_wins + total_losses
    avg_win_rate = total_wins / total_matches
    avg_rd = group['RD'].mean()
    stages = group['Stage'].tolist()
    playoff_appearances = stages.count('Playoff Stage')
    return pd.Series({
        'Avg Win Rate': avg_win_rate,
        'Avg RD': avg_rd,
        'Playoff Appearances': playoff_appearances
    })


def predict_outcome(df = "AllYears.csv", playoff_threshold=2, win_rate_threshold=0.4):
    """Predicts and displays likely qualifiers and winners based on metrics."""
    team_stats = df.groupby('Team', group_keys=False).apply(_calculate_team_metrics).reset_index()
    likely_qualifiers = team_stats[
        (team_stats['Playoff Appearances'] >= playoff_threshold) &
        (team_stats['Avg Win Rate'] >= win_rate_threshold)
    ]
    
    likely_winners = likely_qualifiers.sort_values(by=['Avg RD', 'Avg Win Rate'], ascending=False).head(1)
    
    st.write("Teams Likely to Qualify:")
    st.write(likely_qualifiers['Team'])
    st.write("Team Likely to Win:")
    st.write(likely_winners['Team'])


def call_cal_win_rate(df):
    """Adds Win Rate and Win Rate % columns to the DataFrame and displays them."""
    if 'Win Rate' not in df.columns:
        df['Win Rate'] = df.apply(calculate_win_rate, axis=1)

    df['Win Rate %'] = (df['Win Rate'] * 100).apply(lambda x: f"{x:.0f}%")
    st.write("Win Rate % for Each Team:")
    st.write(df[['Team', 'Win Rate %']])


def calculate_win_rate(row):
    """Calculates the win rate from the Matches column."""
    wins = int(row['Matches'].split('-')[0])
    losses = int(row['Matches'].split('-')[1])
    total_matches = wins + losses
    return wins / total_matches


def cal_total_matches(df):
    """Calculates and displays columns for average rounds won/lost per match."""
    df['Total Matches'] = df.apply(total_matches, axis=1)
    df['Rounds Won'] = df['Rounds'].str.split('-').str[0].astype(int)
    df['Rounds Lost'] = df['Rounds'].str.split('-').str[1].astype(int)
    df['Avg Rounds Won'] = (df['Rounds Won'] / df['Total Matches']).astype(int)
    df['Avg Rounds Lost'] = (df['Rounds Lost'] / df['Total Matches']).astype(int)
    st.write("Average Rounds Won and Lost per Match:")
    st.write(df[['Team', 'Avg Rounds Won', 'Avg Rounds Lost']])


def total_matches(row):
    """Calculates total matches played from the Matches column."""
    wins = int(row['Matches'].split('-')[0])
    losses = int(row['Matches'].split('-')[1])
    return wins + losses


def ranking(df):
    """Calculates and displays round efficiency ranking."""
    df['Rounds Won'] = df['Rounds'].str.split('-').str[0].astype(int)
    df['Rounds Lost'] = df['Rounds'].str.split('-').str[1].astype(int)
    df['Total Rounds Played'] = df['Rounds Won'] + df['Rounds Lost']
    df['Round Efficiency'] = df['Rounds Won'] / df['Total Rounds Played']
    st.write("Round Efficiency for Each Team:")
    st.write(df[['Team', 'Round Efficiency']])


def top3(df):
    """Displays the top 3 teams by Win Rate."""
    if 'Win Rate' not in df.columns:
        df['Win Rate'] = df.apply(calculate_win_rate, axis=1)

    top_3_teams = df.sort_values(by='Win Rate', ascending=False).head(3).reset_index()
    st.write("Top 3 Teams by Win Rate:")
    st.write(top_3_teams[['Team', 'Win Rate']])


st.set_page_config(layout="wide")


col1, col2 = st.columns([1, 3])


with col1:
    st.header("Esports")
    
    
    esports_option = st.selectbox(
        "Select an Esport game:",
        ["Select", "Counter-Strike", "Dota 2", "League of Legends"]
    )

    if esports_option == "Counter-Strike":
        st.write("You selected Counter-Strike!")

        
        cs_option = st.selectbox(
            "Select Counter-Strike data analysis type:",
            ["Select Data", "Calculate Average Metrics", "Predict Outcome", 
             "Calculate Win Rate", "Calculate Total Matches and Rounds", 
             "Calculate Round Efficiency", "Top 3 Teams by Win Rate", "Comparison"]
        )

        
        data = load_data()

        
        year_option = st.selectbox("Select Year:", [2021, 2022, 2023, 2024])


st.markdown("<hr>", unsafe_allow_html=True)


with col2:
    
    if esports_option == "Counter-Strike":
        st.header("Counter-Strike Data Analysis")
        
        df, df_stages = data[year_option]

        if cs_option == "Calculate Average Metrics":
            calculate_avg_metrics(df)

        elif cs_option == "Predict Outcome":
            predict_outcome(df)

        elif cs_option == "Calculate Win Rate":
            call_cal_win_rate(df)

        elif cs_option == "Calculate Total Matches and Rounds":
            cal_total_matches(df)

        elif cs_option == "Calculate Round Efficiency":
            ranking(df)

        elif cs_option == "Top 3 Teams by Win Rate":
            top3(df)

        elif cs_option == "Comparison":
            
            fig, ax = plt.subplots(figsize=(10, 6))

            all_teams = set(df['Team'])
            for year in range(2021, 2025):
                df_year, _ = data[year]
                avg_win_rates = df_year.groupby('Team')['Win Rate'].mean()
                ax.plot(avg_win_rates.index, avg_win_rates.values, label=f"Year {year}")

            ax.set_title("Comparison of Average Win Rates (2021-2024)")
            ax.set_xlabel("Teams")
            ax.set_ylabel("Average Win Rate")
            ax.legend()
            st.pyplot(fig)
