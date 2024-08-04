# Movie Recommendation System
This is a Streamlit-based movie recommendation system. The app allows users to select a movie from a dropdown list and receive recommendations for similar movies
*The required datasets can be found below

https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/input?select=movies_metadata.csv
https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/input?select=credits.csv
https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/input?select=links_small.csv

#Obtain an API key from https://www.themoviedb.org. This is used to fetch the posters for the recommended movies.
## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- Streamlit
- pandas
- requests
- pickle

**Features**
- Select a movie from a dropdown list to get recommendations.
- Display movie posters alongside the recommended titles.
- Use of cosine similarity to find similar movies based on movie metadata.
- User-friendly interface with Streamlit.
  

**To run this project locally, follow these steps:**

- Add the csv files and the Movie_Recommender.ipynb to one folder called Movie Recommender System.

- Run the ipynb file. You will see two pkl files named similarity.pkl and movies.pkl in the folder.

- Create an app.py file and read both pkl files.

- Install streamlit in the terminal using pip install streamlit.

-rRn the app.py using the command streamlit run app.py.


**Usage**
- Open the Streamlit app in your browser.
- Select a movie from the dropdown list.
- Click the "Show Recommendations" button.
- View the recommended movies and their posters.
  
## Data

The project uses movie metadata from various CSV files. The data preprocessing steps include:

- Loading and merging datasets (movies metadata, credits, keywords, links).
- Cleaning the data by dropping unnecessary columns and handling missing values.
- Creating a combined 'tags' column from the 'overview', 'genres', 'cast', and 'keywords' columns.
- Using TF-IDF Vectorizer to convert the 'tags' text into numerical representations.
- Calculating cosine similarity between movie vectors.
- Saving the processed data and similarity matrix into pickle files.

To generate the `movies.pkl` and `similarity.pkl` files, follow these steps:

1. Load the necessary CSV files into pandas DataFrames.
2. Preprocess the data as described in the script.
3. Save the processed DataFrame and similarity matrix into pickle files.

## How It Works

### Code Explanation

**Data Preprocessing**:

- Load movie metadata, credits, keywords, and links datasets.
- Clean the data by dropping unnecessary columns and rows with inconsistent data.
- Merge datasets on the 'id' column.
- Create a 'tags' column by combining relevant metadata.

**Feature Extraction**:

- Use TF-IDF Vectorizer to convert the 'tags' text into numerical representations.
- Calculate cosine similarity between movie vectors.

**Recommendation Function**:

- Define a function `fetch_recommendations` that takes a movie title as input.
- Find the index of the selected movie in the DataFrame.
- Compute similarity scores and get the top 5 most similar movies.
- Fetch the poster URLs for the recommended movies.

**Streamlit App**:

- Load the processed DataFrame and similarity matrix from pickle files.
- Create a Streamlit app with a dropdown for movie selection and a button to show recommendations.
- Display the recommended movies and their posters.




