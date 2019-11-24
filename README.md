# Top-250-IMDB-Movies-Scraper
This python scraper scrapes the details of top 250 movies from IMDB official website

## Pre-requisites
[Python 3](https://www.python.org/downloads/) is recommended to run the script.
The following python libraries must be installed (if not already done) prior running the script:
* [Selenium Requests](https://pypi.org/project/selenium-requests/)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

### Running the script
1. Download the zip file of this repository extract the zip file.
2. Open terminal (in Linux) or command prompt (in Windows) and go to the directory containing the script   `cd path/to/extracted/directory`
3. Enter `python3 imdb_movie_scrapper.py` (in terminal) or `py imdb_movie_scrapper.py` (in Command Prompt).
4. Wait for the program to finish. A file named **movies.json** will be generated by the program.

### Contents of the JSON file
It contains an JSON object which contains a **movie** array.
Each object of this array contains:
* **title** : Title of the movie.
* **director** : An array of names of the movie director(s).
* **writer** : An array of names of the movie writer(s).
* **star** : An array of names of the movie star(s).
* **poster** : Image URL of the movie poster.
* **rating** : IMDB rating of the movie.
* **date** : An object containing movie release dates in various countries.

#### Sample movie object in the JSON file
```json
{
  "title": "Seven Samurai (1954) ",
  "director": [
    "Akira Kurosawa"
  ],
  "writer": [
    "Akira Kurosawa",
    "Shinobu Hashimoto",
    "1 more credit"
  ],
  "star": [
    "Toshirô Mifune",
    "Takashi Shimura",
    "Keiko Tsushima",
    "See full cast & crew"
  ],
  "poster": "https://m.media-amazon.com/images/M/MV5BODdlYjU1Y2MtMWUxMy00YjJjLTgyMWItNzgzZmZkNTYxNWFkXkEyXkFqcGdeQXVyMTAwMjU1MzA2._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
  "rating": "8.6",
  "date": {
    "Japan": "26 April 1954",
    "Italy": "25 August 1954",
    "France": "30 November 1955",
    "Belgium": "23 March 1956",
    "Greece": "25 June 1956",
    "USA": "3 July 1956",
    "Uruguay": "3 December 1956",
    "Argentina": "1 January 1957",
    "Finland": "6 February 1959",
    "West Germany": "13 July 1962",
    "Sweden": "20 September 1965",
    "Spain": "20 April 1967",
    "Portugal": "20 November 1967",
    "Denmark": "29 June 1968",
    "Australia": "5 November 1993",
    "Netherlands": "18 March 2004",
    "Czech Republic": "15 January 2009",
    "Madagascar": "10 June 2015",
    "UK": "5 March 2017",
    "Hong Kong": "17 April 2017",
    "Tunisia": "27 October 2019"
  }
}
```
