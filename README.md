# Surfs Up Challenge Analysis
#flask, #SQLite, #SQLAlchemy #Python 

# Project Overview

The purpose of this analysis is to provide W.Avy more information about temperature trends for the months of June and December. The following informatiion is to support the investment that W.Avy wants to contribute for the surf and ice cream shop. We'll be using SQLite to store the weather data that W. Avy shared with us and that we'll need for our analysis. With the following information, I wil be able to gather data to get the summarized statistcs for June and December. 

# Results

## Summary Statistics for June 

Using Python, Pandas functions and methods, and SQLAlchemy, I filtered the date column from of the Measurements table in the 'hawaii.sqlite' database to retrieve all the temperatures for the month of June. In the Jupyter Notebook, I then converted those temperatures to a list and create a DataFrame from the list.

June's Temperature Stats:

<img width="150" alt="june_describe" src="https://user-images.githubusercontent.com/102995385/188295839-f847cd01-8c30-449a-9b17-0945ad76ed0e.png">

![june_tight_layout](https://user-images.githubusercontent.com/102995385/188296725-47c72fbe-b717-46bf-b93f-a79a8e689004.png)



## Summary Statistics for December
I repeated the same steps as followed for June's results. Except extracting the December Temps. Below are located December's temperature statistics.

December's Temperature Stats:

<img width="177" alt="december_describe" src="https://user-images.githubusercontent.com/102995385/188295885-cf991126-50ee-483f-96b2-3285a7086e46.png">

![december_tight_layout](https://user-images.githubusercontent.com/102995385/188296550-1a1532a7-d17d-4933-b5f1-a139e7aaefe4.png)

## Key Points
    1. Junes average temperature is 74.9 degrees Farhenhit, averaging more than 
    December which is 71 degrees Farhenhit.
    2. June shows highers numbers in 80 degrees and above, where December shows 
    lower numbers for 80 degrees but higher numbers for 70.
    3. The graph also shows a low amount of times that it gets low as 55 degrees and 
    as for June it gets low to 65.

# Summary
To begin, our analysis is to reassure W.Avy concerns and had asked for an analysis on the  weather inorder for him to fully invest in the Surf n' Shake shop in Oahu, HI. I was able to conduct my analysis based off the information we gathered from the 'hawaii.sqlite' database. Throughout the module I was able to extract the measurments of percepitation of the entire year prior. I successfully executed my code in the 'climate_analysis', A Jupyter Notebook using Python. In the notebook you'll notice every cell explained my thought process as to why I was using that code exact and this also reflects in the 'SurfsUp_Challenge' another notebook. The second Jupyter notebook is for an audince for potential investor who are not quite familiar with executing code. I was able to use Flask to generate an easier way for them to view the data. I also only based the second Jupyter Notebook on the months on January and December, the results above. The results below are showing additional support to the analysis and are based off the measurments of percepiation for the months of January and December. 

### Additional Queries

January and Decembers Percepitation



    - The plot above show 
