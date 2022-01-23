### Introduction
This poetry project contains two scripts and associated package management files:
- get_data.py is used to collect data from reddit to be transformed by the dbt models
- data_visualizaton.py is used on the file (keyword_matches.csv) that results from the dbt transformation. It produces a word cloud file displaying the counts of keyword mentions
- keyword_matches.csv is provided as an example of the data that might result from running the dbt models in the folder dbt_model

### Installation
- pip install poetry
- change directory to python_scripts
- poetry install

### Running a script
- poetry run python script_name.py

### Packages
- pandas (01/2022)
- psaw (01/2022)
- matplotlib (01/2022)
- wordcloud (01/2022) 