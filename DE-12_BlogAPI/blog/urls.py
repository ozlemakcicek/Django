

# from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryView,PostView

#Router:
router=DefaultRouter()
router.register('category',CategoryView)
router.register('post',PostView)

urlpatterns = router.urls
# tanimlanmis bir urlpatterns olmadigi icin += demeye gerek yok direkt = yaz
