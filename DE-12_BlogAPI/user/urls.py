from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserView

#*********************************
#Login
from rest_framework.authtoken.views import obtain_auth_token
#Logout
from rest_framework.decorators import api_view
@api_view(['POST'])

def logout(request):
    request.user.auth.token.delete() # Token Sil.
    return Response({"message": 'User Logout: Token Deleted'})

# Login/Logout
urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', logout),
]



# ROUTER:
router = DefaultRouter()
router.register('', UserView)

urlpatterns += router.urls