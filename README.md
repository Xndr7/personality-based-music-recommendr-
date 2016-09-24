#Personality based music recommendation system using IBM Watson Personality Insights API 

##About the Project
[Personality Insights API] (https://console.ng.bluemix.net/catalog/services/personality-insights/ "Personality Insights API") derives insights from 
transactional and social media data to identify psychological traits which determine purchase decisions, intent and behavioral traits; utilized to improve conversion rates.
Using this API,a training set of 69 musicians' personality was created. A test set of 7 Youtubers active on twitter was also created.

##How it works
Using this training and test data, certain(10) personality traits were chosen and a cluster-based model was made. Clustering has been done using Kmeans.
This model was then pickled and stored to prevent the model was being made repeatedly at runtime.
Input is given in the form of a Twitter handle and the system fetches the tweets and sends these tweets to analyse the personality of the user.
The output of the Personality Insights API is then received and the same earlier traits are selected and the cluster of musician that closely identify with the user is displayed.

To run the app, create your own config.py file with the relevant twitter and bluemix credentials. Then just simply run the serve_page.py script and goto the relevant url displayed by the system.
A fully functional demo will be available for use.

#####This project has been done for the IBM venturesity hackathon. Feel free to modify and use it as per your wishes, but don't forget to give credit!:)
