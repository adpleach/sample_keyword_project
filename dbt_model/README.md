### Introduction
This dbt project contains the data and models required to run the keyword extraction process:
- dbt_project.yml specifies the project configuration
- packages.yml specifies the packages required for the project and their dependecies
- data\keywords.csv contains the list of keywords to be matched and associated regex
- data\posts.csv contains data extracted from r/dataengineering using get_data.py
- models\example\schema.yml contains descriptions of the models, their primary key and associated tests
- models\example\base_keywords.sql contains the keywords of interest, their categories and associated regular expressions
- models\example\base_post_sentences.sql contains reddit post data and text data flattened by sentence
- models\example\stg_keyword_extraction.sql calculates metrics and dimensions pertaining to the keywords in text data
- models\example\keyword_extraction.sql contains metrics and dimensions pertaining to the keywords identified

### Installation
- pip install dbt-core \ dbt-postgres \ dbt-redshift \ dbt-snowflake \ dbt-bigquery
- change directory to dbt_model
- dbt init
- dbt deps

### Running the models
- dbt run 
- dbt test (as required)

### Dependencies
- dbt-labs/dbt_utils >= 0.7.0

*******
Information below is provided by dbt when a new project is started
*******

Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](http://slack.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
