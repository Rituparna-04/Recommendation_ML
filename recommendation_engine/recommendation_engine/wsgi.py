"""
WSGI config for recommendation_engine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import inspect
from apps.ML_model.registry import MLRegistry
from apps.ML_model.course_recommendation.lightfm import RecommendationSystem

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommendation_engine.settings')

application = get_wsgi_application()

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rs = RecommendationSystem()
    # add to ML registry
    registry.add_algorithm(endpoint_name="course_recommendation",
                            algorithm_object=rs,
                            algorithm_name="lightfm",
                            algorithm_status="production",
                            algorithm_version="0.0.5",
                            owner="Rituparna Maiti",
                            algorithm_description="Course recommendation for learning application",
                            algorithm_code=inspect.getsource(RecommendationSystem))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
