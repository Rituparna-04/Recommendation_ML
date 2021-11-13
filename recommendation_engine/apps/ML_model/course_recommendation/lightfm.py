import pickle
import pandas as pd
import numpy as np
from lightfm import LightFM
from scipy.sparse import csr_matrix

class RecommendationSystem:
    def __init__(self):
        path_to_artifacts = "../Recommendation_model/"
        filename1 = path_to_artifacts + "model_dump"
        with open(filename1 , 'rb') as f1:
            self.model = pickle.load(f1)
        
        filename2 = path_to_artifacts + "coursematrix_dump"
        with open(filename2 , 'rb') as f2:
            self.courses = pickle.load(f2)
               
        filename3 = path_to_artifacts + "interactions_dump"
        with open(filename3 , 'rb') as f3:
            self.interactions = pickle.load(f3)
    
    
    def show_recommendations(self, user_id, threshold = 0, nrec_items = 5):
        
        n_items = self.interactions.shape[1]
        scores = pd.Series(self.model.predict(user_id, np.arange(n_items), item_features=self.courses))
        scores.index = self.interactions.columns
        scores = list(pd.Series(scores.sort_values(ascending=False).index))
        known_items = list(pd.Series(self.interactions.loc[user_id,:][self.interactions.loc[user_id,:] > threshold].index).sort_values(ascending=False))
    
        scores = [x for x in scores if x not in known_items]
        score_list = scores[0:nrec_items]
        return score_list
    
    def predict_recommendations(self, users):
        #u = kwargs
        user_id = users["user_id"]
        try:
            #courses, interactions = self.prep_data()
            scores = self.show_recommendations(user_id)
            
        except Exception as e:
            return {"status": "Error", "message": str(e)}
        
        return {"recommendation": scores, "status": "OK"} 
       