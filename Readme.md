# Netflix Titles EDA with Spark

## Overview
This project uses Apache Spark to perform exploratory data analysis (EDA) on a dataset of Netflix titles.

## Dataset
The dataset `netflix_titles.csv` contains information about movies and TV shows available on Netflix. The columns include:
- `show_id`: Unique ID of the show.
- `type`: Type of content (Movie/TV Show).
- `title`: Title of the show.
- `director`: Director of the show.
- `cast`: Cast of the show.
- `country`: Country of production.
- `date_added`: Date when the show was added to Netflix.
- `release_year`: Release year of the show.
- `rating`: Age rating.
- `duration`: Duration of the show.
- `listed_in`: Genres.
- `description`: Description of the show.

## Features
- Analyze data using Apache Spark.
- Handle missing values.
- Aggregations and visualizations for insights.

## Setup

### Prerequisites
1. Docker installed on your system.
2. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

### Build and Run
1. Build the Docker image:
   ```bash
   docker build -t netflix-eda .
   ```

2. Run the Docker container:
   ```bash
   docker run -it --rm -v $(pwd):/app netflix-eda
   ```

3. The analysis will run automatically, and visualizations will be saved as output files in the `/app` directory.

## Dependencies
- Python 3.9
- Apache Spark
- Matplotlib
- Pandas

## Results
Explore the generated output and visualizations for insights into Netflix titles.

