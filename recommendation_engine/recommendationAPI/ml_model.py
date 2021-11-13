from django.conf.urls import url
from django.http import HttpResponse

from lightfm import LightFM
from scipy.sparse import csr_matrix
import pandas as pd
import pickle


def prep_data():
        interactions = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//Interactions.csv')
        users = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//Users.csv')
        courses = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//recommendation_engine//recommendationAPI//courses.csv')
        
        course_transformed = pd.get_dummies(courses, columns = ['SKILL_ID', 'SUBJECT_ID', 'PROVIDER_ID'])
        course_transformed = course_transformed.sort_values('COURSE_ID')
        course_matrix = csr_matrix(course_transformed.drop('COURSE_ID', axis=1).values)
        
        interactions_pivot = pd.pivot_table(interactions, index='USER_ID', columns='COURSE_ID', values='RATING')
        interactions_pivot = interactions_pivot.fillna(0)
        interactions_matrix = csr_matrix(interactions_pivot.values)
        
        return course_matrix, interactions_matrix
    
def build_model(interactions_matrix, course_matrix):
        model = LightFM(loss='warp', random_state=2016, learning_rate=0.90, no_components=150, user_alpha=0.000005)
        model = model.fit(interactions_matrix, item_features=course_matrix, epochs=100, verbose=True)
        
        return model


def recommender_system():
        course_data, interaction_data = prep_data()
        model = build_model(interaction_data, course_data)
        filename = 'recommender_model.sav'
        with open(filename, 'wb') as files:
            pickle.dump(model, files)
        
