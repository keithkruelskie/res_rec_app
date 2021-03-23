# Project 5: Washington, DC Public Schools

### Problem Statement
Can we predict a school's STAR rating based on features relating to each school?
**bolded info**

### Executive Summary
This project aims to evaluate metrics used to evaluate schools in the DC Public School system.


### File Directory / Table of Contents
Data was collected using _____

##### Python notebook files:
 - 01 Data Collection
 - 02 Data Cleaning
 - 03 EDA
 - 04 Modeling

##### Files contained in the 'data' folder:
   - 'school_df_v6.csv' - 
 
### Data Dictionaries
<br>

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**code**|*float*|school_df_v6|School code|
|**name**|*object*|school_df_v6|School name| 
|**grade_band**|*object*|school_df_v6|School grades| 
|**enrollment_SY1718**|*float*|school_df_v6|Student enrollment 2017-2018| 
|**enrollment_SY1819**|*float*|school_df_v6|Student enrollment 2018-2019| 
|**star_score_SY1718**|*float*|school_df_v6|School star score 2017-2018| 
|**star_score_SY1819**|*float*|school_df_v6|School star score 2018-2019|
|**star_rating_SY1718**|*float*|school_df_v6|School star rating 2017-2018|
|**star_rating_SY1819**|*float*|school_df_v6|School star rating 2018-2019|
|**capacity_SY1718**|*float*|school_df_v6|School capacity 2017-2018|
|**capacity_SY1819**|*float*|school_df_v6|School capacity 2018-2019|
|**latitude**|*float*|school_df_v6|School latitude|
|**longitude**|*float*|school_df_v6|School longitude|
|**cluster**|*float*|school_df_v6|School cluster|
|**ward**|*float*|school_df_v6|School ward|

### Data Cleaning


### EDA


### Modeling
##### Base Model
##### Linear Regression
##### Ridge Model
##### Lasso Model
##### Decision Tree Regressor
##### KNN Regressor
##### Random Forest Regressor
##### Elastic Net
##### Polynomial Features
##### Bagging Regressor
##### Adaboost
##### Gradient Boosting Regressor
##### Support Vector

### Interactive App

The app is an extension of the EDA and a way to quickly visualize multiple graphs side by 
side, at the user's discretion along with an interactive choropleth overlay on the D.C.
region.

The app was developed in Flask, and runs on a local server activated by the app.py file.
The app.py file draws its data from the school_df_v6.csv and cluster_map.csv file to 
populate the graphs and choropleth. Once a user has navigated to the app, a number of drop
downs control what each graph shows, and another dropdown controls the overlay on the D.C.
metro area. Clicking Update Dashboard refreshes the page with the new graphs and maps.

Future app integrations might include additional tooltips and data on the schools that 
populate on the map, and perhaps an interactive layer to allow for selection of
neighborhood clusters to look at data about the cluster in detail.

### Conclusions and Recomendations
In conclusion, While student academic performance is the leading indicator of a school’s star rating, we believe school attendance to be the largest actionable issue that the school district can address.
By addressing truancy, we expect to see an increase in student academics, and therefore STAR rating.
And, in fact, the DC department of education has taken a major interest in the issue of chronic absenteeism beginning in 2018. They have implemented a number of policies to maximize student attendance, including the mayor’s attendance initiative titled “Every Day Counts.” 


### Sources
