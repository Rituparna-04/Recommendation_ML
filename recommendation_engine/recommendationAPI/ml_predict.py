
from lightfm import LightFM
from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np
import pickle

'''
class personalize(object):
    def __init__(self, courses, interactions):
        self.courses = courses
        self.interactions = interactions
'''        
def prep_data():
        interactions = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//Interactions.csv')
        users = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//Users.csv')
        courses = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//courses.csv')

        course_transformed = pd.get_dummies(courses, columns = ['SKILL_ID', 'SUBJECT_ID', 'PROVIDER_ID'])
        course_transformed = course_transformed.sort_values('COURSE_ID')
        courses = csr_matrix(course_transformed.drop('COURSE_ID', axis=1).values)
        
        interactions = pd.pivot_table(interactions, index='USER_ID', columns='COURSE_ID', values='RATING')
        interactions = interactions.fillna(0)
                
        return courses, interactions
 
           
def show_recommendations(interactions, course_matrix, user_id, threshold = 0, nrec_items = 5, show = True):
        filename = "recommender_model.sav"
        with open(filename , 'rb') as f:
            model = pickle.load(f)
               
        n_items = interactions.shape[1]
        scores = pd.Series(model.predict(user_id, np.arange(n_items), item_features=course_matrix))
        scores.index = interactions.columns
        scores = list(pd.Series(scores.sort_values(ascending=False).index))
        known_items = list(pd.Series(interactions.loc[user_id,:][interactions.loc[user_id,:] > threshold].index).sort_values(ascending=False))
    
        scores = [x for x in scores if x not in known_items]
        score_list = scores[0:nrec_items]
        if show == True:
            print ("User: " + str(user_id))
            print("~~~~~")
            print("Recommended Items:")
            print('------------------')
            counter = 1
            for i in score_list:
                print(str(counter) + '- ' + str(i))
                counter+=1
        
def predict_recommendations(user_id):
        course_data, interaction_data = prep_data()
        show_recommendations(interaction_data, course_data, user_id)
'''        
if __name__ == '__main__':
    customer_id = input("Provide Customer_id : ")
    if(customer_id.isdigit()):
        customer_id = int(customer_id)
        interactions = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//Project//Interactions.csv')
        courses = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//Project//courses.csv')
        recommendations = personalize(courses, interactions)
        recommendations.predict_recommendations(customer_id)
    else:
        print("\n!!!!! Customer_id should be integer !!!!!")
'''            
    