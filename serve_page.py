from spyre import server
import twitteranalyzer
from sklearn.externals import joblib
import pandas as pd
import pickle

class SimpleApp(server.App):
    title = "Personality based music recommender system"
    inputs = [{ "type":"text",
                "key":"words",
                "label":"write words here",
                #"value":"hello world", 
                "action_id":"simple_html_output"}]

    outputs = [{"type":"html",
                "id":"simple_html_output"}]

    def getHTML(self, params):
        words = params["words"]
        #twitteranalyzer.personalityinsights(words)
        personality_data = pd.read_csv("pi_5.csv")
        test_data = personality_data[["Trust","Orderliness","Extraversion","Anger","Adventurousness","Artistic interests","Emotionality","Intellect","Liberalism","Love"]]
        pca = joblib.load('pca_usedfortxfm.pkl')
        clusterer = joblib.load('clusterer.pkl')
        pca_samples = pca.transform(test_data)
        sample_preds = clusterer.predict(pca_samples)
        clus = sample_preds[0]
        reslts = joblib.load('reslts.pkl')
        similar_res = reslts.loc[reslts['Cluster'] == clus].drop(["Cluster"],axis=1)
        wrds = str(similar_res.userid.to_string(index=False)).split('\n')
        return "%s" % wrds         
        
        
        
        
app = SimpleApp()
app.launch(port=9090)
