<<<<<<< HEAD
#!/usr/bin/python3

from flask import Blueprint
app_views = Blueprint("/api/v1", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
=======
#!/usr/bin/python
3from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

""" import views """
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
>>>>>>> 20914765f6d45aeab9cedbb8293ff75ba310db96
