# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:10:18 2021

@author: ritup
"""

from lightfm import LightFM
from scipy.sparse import csr_matrix
import pandas as pd
import pickle

class recommender(object):
    def __init__(self, users, courses, interactions):
        self.users = users
        self.interactions = interactions
        self.courses = courses
                
    def prep_data(self):
        course_transformed = pd.get_dummies(self.courses, columns = ['SKILL_ID', 'SUBJECT_ID', 'PROVIDER_ID'])
        course_transformed = course_transformed.sort_values('COURSE_ID')
        course_matrix = csr_matrix(course_transformed.drop('COURSE_ID', axis=1).values)
        
        interactions_pivot = pd.pivot_table(self.interactions, index='USER_ID', columns='COURSE_ID', values='RATING')
        interactions_pivot = interactions_pivot.fillna(0)
        interactions_matrix = csr_matrix(interactions_pivot.values)
        
        return course_matrix, interactions_matrix
    
    def build_model(self, interactions_matrix, course_matrix):
        model = LightFM(loss='warp', random_state=2016, learning_rate=0.90, no_components=150, user_alpha=0.000005)
        model = model.fit(interactions_matrix, item_features=course_matrix, epochs=100, verbose=True)
        
        return model
    
    def recommender_system(self):
        course_data, interaction_data = self.prep_data()
        model = self.build_model(interaction_data, course_data)
        filename = 'recommender_model'
        with open(filename, 'wb') as files:
            pickle.dump(model, files)
        
if __name__ == '__main__':
    interactions = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//Project//Interactions.csv')
    users = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//Project//Users.csv')
    courses = pd.read_csv('C://Users//ritup//OneDrive//Desktop//Flotilla Techs//Project//courses.csv')
    
    recommends = recommender(users, courses, interactions)
    recommends.recommender_system()