import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

movies_df = pd.read_csv("imdb_top_250_movies.csv")
shows_df = pd.read_csv("imdb_top_250_shows.csv")

option = st.sidebar.selectbox(
    "What would you like to see?", ("Top 250 Movies", "Top 250 Shows")
)

if option == "Top 250 Movies":
    # Sidebar input to determine the number of movies to display
    num_movies = st.sidebar.slider("Enter the number of movies to display:", 1, 250, 10)

    # Display header
    header_string = "Top " + str(num_movies) + " Movies"
    st.header(header_string)

    # Initialize counter
    i = 0

    # While loop to display the specified number of movies
    while i < num_movies:
        row = movies_df.iloc[i]
        st.subheader(str(i + 1) + ". " + row["Name"])
        st.image(row["Image"], caption=row["Name"], width=200)
        st.write(f"**Description:** {row['Description']}")
        st.write(f"**Rating:** {row['Rating']}")
        st.write(f"**Rating Count:** {row['Rating Count']}")
        st.write(f"**Content Rating:** {row['Content Rating']}")
        st.write(f"**Genre:** {row['Genre']}")
        st.write(f"**Duration:** {row['Duration']}")
        st.write(f"[More info]({row['URL']})")
        st.write("---")
        i += 1

elif option == "Top 250 Shows":
    # Sidebar input to determine the number of shows to display
    num_shows = st.sidebar.number_input(
        "Enter the number of shows to display:", 1, 250, 10
    )

    # Display header
    header_string = "Top " + str(num_shows) + " Shows"
    st.header(header_string)

    # Initialize counter
    i = 0

    # While loop to display the specified number of shows
    while i < num_shows:
        row = shows_df.iloc[i]
        st.subheader(row["Name"])
        st.image(row["Image"], caption=row["Name"], use_column_width=True)
        st.write(f"**Description:** {row['Description']}")
        st.write(f"**Rating:** {row['Rating']}")
        st.write(f"**Rating Count:** {row['Rating Count']}")
        st.write(f"**Content Rating:** {row['Content Rating']}")
        st.write(f"**Genre:** {row['Genre']}")
        st.write(f"**Duration:** {row['Duration']}")
        st.write(f"[More info]({row['URL']})")
        st.write("---")
        i += 1
