from django.urls import path
from . import views

# For Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

# When the code is set for Authentication:
# >>Go to the url of "token/"
# >>Here you will find a form
# >>Enter the data to create a token
# >>When the token is created, copy the access token
# >>Open postman
# >>Go to the url that require the authentication, in our case Authentication is required for the "advocate_list()", go to the url of "advocates/"
# >>Send the "GET" request 
# >>See there is a section below "Authentication", go to it, Now in the type select "Bearer to" and paste the copied "access token" and send the GET request. Now you will be able to access the list of Advocates.

urlpatterns = [
    path('advocates/',views.advocate_list, name='advocates'),
    
    # For Authentication
    path('token/', TokenObtainPairView.as_view(), name = "token_obtain_pair"),

    # path('advocates/<str:name>/',views.advocate_detail),
    path('advocates/<str:name>/',views.AdvocateDetail.as_view()),

    path('companies/',views.company_list, name='companies'),
]
