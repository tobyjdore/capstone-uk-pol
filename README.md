# capstone-uk-pol
## GA DSI7 Capstone Project - NLP analysis of UK political speeches

The aim of this project was to build a predictive model that would guess an MP's party based on the text of a speech, without any obvous indicators like party names or party leader names.

I also looked at the vocabularies of speakers from different parties, and carried out topic analysis on the speeches.

My dataset was scraped from the <a href='http://www.ukpol.co.uk'>UKPOL Political Speech Archive</a>.

Here is the <a href='https://tobyjdore.github.io/ukpol/project'>project report</a>, and I also kept a <a href='https://mydsblog.home.blog'>wordpress blog</a> of the process.

### Repository Contents:

#### Capstone-summary
- Summary of project, results, working code.

#### Data (folder)
- CSV files of project data from initial scrape through stages of cleaning

#### web-app (folder)
- flask code, web templates, and pickled model for the <a href='http://tobyjdore.pythonanywhere.com'>deployed classification model</a>.
