# TWISTER: Tornado evolution WIth Season and TERrain
Data analysis pipeline to identify trends in NOAA storm event data serving to increase human safety from tornado events.

## **Background** 

Tornados are a highly damaging and dangerous weather phenomenon that appear with minimal warning beforehand. Alerts for potential tornadoes from the National Weather Service are highly dependent on reading the output from radars all across the country. To ensure these alerts are received by affected parties in a timely manner, high quality and high coverage data is a necessity. Unfortunately the coverage by available WSR-88D radars is limited in some areas where, historically, damaging tornadoes are more common. Identifying these high-risk low-coverage areas and installing new weather radars can increase the likelihood that the National Weather Service can issue alerts accurately and save lives.

## **Goal** 

Identify whether there are underserved regions in radar coverage. Determine if tornado alley has shifted in time and location.

## **Strategy** 

Using linear, non-parametric, and quantile regression to determine where and when tornados will most likely strike in the future. Using NOAA 1990-2025 storm event data we can isolate tornado events and construct a model that will predict future risk based on past events.

## **Repo Layout**

### **Data** 

Raw data can be re-downloaded using the download.py script in the src directory.

(1) NOAA Storm Events -- Detailed CSVs containing information on severe storms available from 1990 to 2025. This contains information about tornado events such as severity scale (i.e. EF0 - EF5 or F0 - F5 before 2007), estimated start coordinates for the storm, date and time, human impact (injuries/deaths), etc.

(2) NEXRAD WSR-88D site list -- From the NWS radar API, contains the locations of all existing WSR-88D weather radars. Will be used, along with estimated effective range of these radars in detecting storms, to determine where there are gaps in radar coverage.

### **Data Processing** 

The notebook titled data-preprocessing.ipynb cleans up the storm event data, removing data where important fields are missing or incomplete. The notebook saves the clean data to new data frames in data/processed both with and without more strict cuts based on the availability of human casualty data. This data is also separated by year in sub-directories. 

### **Exploratory Data Analysis** 

EDA-KDE-humanimpact.ipynb contains exploratory data analysis looking for trends in the various features available in the tornado storm events. When exploring dozens of potential parameter correlations and various ML models, the only non-obvious trend emerging from the data was with the time evolution of number and location of tornado events.

### **Model Construction** 

tornado_alley_time_evolution.ipynb - contains the longitudinal time evolution quantile regression model. This model finds that while the eastern edge of tornado alley is not shifting with time, the western edge is shifting east-wards. This shows that the concentration of tornadoes is shifting east with time and will continue to do so in the future.

seasons_EFscale_year.ipynb - contains linear and non-parametric regression models of the number of tornadoes and how this evolves with time. These models explore how these trends vary overall, with season, and with ef scale. The main findings from this analysis show that the overall number of tornado events is increasing with year. Furthermore, there appears to be a larger increase in the number of tornado events in spring and winter (December through May) as opposed to summer and autumn (June through November).

### **Summary Plots** 

Summary plots can be found in the plots directory.

### Dependencies
Users can re-run this entire repo using anaconda by setting up the environment contained in the environment.yml.



