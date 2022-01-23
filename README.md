### Repo Information
This repo contains files and folders related to the article "Parsing keywords from unstructured text data with dbt and regex". The repo contains the following folders:
- dbt_model: dbt project containing data and models used for keyword matching
- python_scripts: Poetry project containing python scripts used to extract data from reddit and create wordcloud from keyword matches

A typical work flow is the following:
1. Run get_data.py to extract posts from r/dataengineering
2. Run dbt models in database on posts data with chosen keywords (example files: keywords.csv, posts.csv)
3. Run data_visualizations.py on resulting table (example file: keyword_matches.csv) to visualize results

### Resources:
- Read the [article]()
- Learn more about [dbt](https://docs.getdbt.com/docs/introduction)
- Learn more about [poetry](https://python-poetry.org/docs/)