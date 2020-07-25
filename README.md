# US-accidents-data-analysis
This is my pet project. In this, I built a web-app with a basic layout to predict the severity of an accident. Various machine learning models such as Logistic Regression, Decision Tree Classifier, AdaBoost Classifier, etc. were tested and out of that XGBoost Classifier came out to be the best one.
Hyperparameter tuning of these models were done using Bayesian Optimization technique.
I tested the models using F1_Beta score which is a weighted harmonic mean of precision and recall, reaching its optimal value at 1 and its worst value at 0. In this, the beta parameter determines the weight of recall in the combined score. beta < 1 lends more weight to precision, while beta > 1 favors recall (beta -> 0 considers only precision, beta -> +inf only recall). In this case, I was more interested in knowing "how many relavant items are selected" rather than "how many selected items are relevant". Since this is predicting  severity if an accident, it paramount that all the relevant cases are covered even with a few false positives. As for deployment, we used HTML and Flask frameworks.


## Dataset:-
The dataset used for the project is [this](https://www.kaggle.com/sobhanmoosavi/us-accidents). It contains more than 3 million records.

### Data Overview:-
#### We will first discuss about each attribute and discuss what it stands for:
- ID:- A unique identifier for each accident.
- Source:- The source which reported the accident.
- TMC:- It is Traffic Messagen Channel which providea more detailed description of the event.
- Severity:- The level of impact of the accident. 1 being the lowest and 4 being the highest.
- Start_Time:- Shows start time of the accident in local time zone.
- End_Time:- Shows end time of the accident in local time zone.
- Start_Lat:- Shows latitude in GPS coordinate of the start point.
- Start_Lng:- Shows longitude in GPS coordinate of the start point.
- End_Lat:- Shows latitude in GPS coordinate of the end point.
- End_Lng:- Shows longitude in GPS coordinate of the end point.
- Distance(mi)-: The length of the road extent affected by the accident.
- Description:- The description of the accident.
- Number:- Street Number
- Street:- Street Name
- Side:- Relative side of the address field.
- City:- Name of the City.
- County:- Name of the county.
- State:- Name of the state.
- Zipcode:- Zipcode of the address
- Country:- Name of the country
- Timezone:- Timezone of the location where accident occurred
- Airport_Code:- Denotes an airport-based weather station which is the closest one to location of the accident.
- Weather_Timestamp:- Shows the time-stamp of weather observation record
- Temperature(F) :- Temperature in Fahrenheit
- Wind_Chill(F):- Wind chill in Fahrenheit
- Humidity(%):- Humidity in percentage
- Pressure(in):- Air pressure in inches
- Visibility(mi):- Visibilty in miles.
- Wind_Direction:- Wind direction
- Wind_Speed(mph):- Wind speed in miles per hour.
- Precipitation(in): -Precipitation in inches.
- Weather_Condition: Shows what was the weather that day, i.e., if it was rainy, sunny, etc.
- Amenity:- A Point-Of-Interest (POI) annotation which indicates presence of amenity in a nearby location.
- Bump: Tells whether there was any bump on the road.
- Crossing:- Tells whether there was any corssing on the road.
- Give_Way:- Tells whether there was any give-way sign on the road.
- Junction:- Tells whether ther was any junction present.
- No_Exit:- Tells whether there was any no-exit sign on the road.
- Railway:- Tells whether ther was any railway present nearby.
- Roundabout:- Tells whether ther was any roundabout present nearby.
- Station:- Tells whether there was any sytation present.
- Stop:- Tells whether there was any Stop sign on the road.
- Traffic_Calming:- Tells whether ther was any Traffic-calming means present nearby.
- Traffic_Signal:- Tells whether there was any taffic signal nearby.
- Turning_Loop:- Tells whether there was any turning loop nearby.
- Sunrise_Sunset::- Tells us the period of the day based on sunrise or suset.
- Civil_Twilight:- Tells us the period of the day based on civil twilight.
- Nautical_Twilight:- Tells us the period of the day based on nautical twilight.
- Astronomical_Twilight:- Tells us the period of the day based on astrnomical twilight.
