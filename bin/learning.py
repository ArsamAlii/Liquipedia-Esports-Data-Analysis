import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# Set up the page layout
st.set_page_config(layout="wide")

# Creating a 2-column layout
col1, col2 = st.columns([1, 3])

# Left Column: "Esports" Dropdown
with col1:
    st.header("Esports")
    
    # Dropdown Menu for selecting esports
    esports_option = st.selectbox(
        "Select an Esport game:",
        ["Select", "Counter-Strike", "Dota 2", "League of Legends"]
    )

    # If "Counter-Strike" is selected, show the relevant content
    if esports_option == "Counter-Strike":
        st.write("You selected Counter-Strike!")
        
        # Counter-Strike specific dropdown (for example, map or player stats)
        cs_option = st.selectbox(
            "Select Counter-Strike data:",
            ["Select Data", "Map Statistics", "Player Performance", "Match Analysis"]
        )

# Add a horizontal line (divider) between the two columns
st.markdown("<hr>", unsafe_allow_html=True)

# Right Column: Counter-Strike related images and a chart
with col2:
    st.header("Counter-Strike Data Analysis")
    
    # Default Image (Before any data is selected

    # Display content based on the left column's selection
    if esports_option == "Counter-Strike" and cs_option != "Select Data":
        
        # Dummy dataset for "Map Statistics"
        if cs_option == "Map Statistics":
            st.subheader("Map Statistics")
            
            # Sample data for Counter-Strike maps
            map_data = {
                'Map': ['Dust 2', 'Mirage', 'Inferno', 'Overpass', 'Train'],
                'Kills': [25, 30, 35, 28, 40],
                'Deaths': [10, 12, 8, 15, 10],
                'Headshots': [15, 18, 20, 25, 22],
            }

            df = pd.DataFrame(map_data)
            st.write(df)  # Display the dataframe

            # Plotting a bar chart for Map Statistics
            fig, ax = plt.subplots()
            df.set_index('Map')[['Kills', 'Deaths', 'Headshots']].plot(kind='bar', ax=ax)
            ax.set_title("Counter-Strike Map Statistics")
            ax.set_ylabel("Count")
            ax.set_xlabel("Map")
            st.pyplot(fig)

        # Dummy dataset for "Player Performance"
        elif cs_option == "Player Performance":
            st.subheader("Player Performance")
            
            # Sample data for Player Performance
            player_data = {
                'Player': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5'],
                'Kills': [45, 30, 50, 20, 40],
                'Deaths': [10, 15, 12, 18, 10],
                'Headshots': [25, 20, 30, 15, 22],
            }

            df = pd.DataFrame(player_data)
            st.write(df)  # Display the dataframe

            # Plotting a bar chart for Player Performance
            fig, ax = plt.subplots()
            df.set_index('Player')[['Kills', 'Deaths', 'Headshots']].plot(kind='bar', ax=ax)
            ax.set_title("Player Performance")
            ax.set_ylabel("Count")
            ax.set_xlabel("Player")
            st.pyplot(fig)

        # Dummy dataset for "Match Analysis"
        elif cs_option == "Match Analysis":
            st.subheader("Match Analysis")
            
            # Sample data for Match Analysis
            match_data = {
                'Match': ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5'],
                'Kills': [150, 200, 170, 180, 160],
                'Deaths': [80, 90, 75, 85, 80],
                'Headshots': [80, 100, 90, 95, 85],
            }

            df = pd.DataFrame(match_data)
            st.write(df)  # Display the dataframe

            # Plotting a bar chart for Match Analysis
            fig, ax = plt.subplots()
            df.set_index('Match')[['Kills', 'Deaths', 'Headshots']].plot(kind='bar', ax=ax)
            ax.set_title("Match Analysis")
            ax.set_ylabel("Count")
            ax.set_xlabel("Match")
            st.pyplot(fig)

    else:
        # When no data is selected, only show the default image
        img = Image.open("cs_image.jpg")  # Make sure you have this image in the same directory
        st.image(img, caption="Counter-Strike Map", use_column_width=True)
        st.write("Select a specific data category from the left.")
