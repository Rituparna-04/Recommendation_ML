from django.test import TestCase
import inspect

from apps.ML_model.registry import MLRegistry
from apps.ML_model.course_recommendation.lightfm import RecommendationSystem

class MLTests(TestCase):
    def test_rf_algorithm(self):
        id = {"user_id": 44}
        my_alg = RecommendationSystem()
        response = my_alg.predict_recommendations(id["user_id"])
        self.assertEqual('OK', response['status'])
        
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "lightfm"
        algorithm_object = RecommendationSystem()
        algorithm_name = "recommendation system"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Rituparna"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RecommendationSystem)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)