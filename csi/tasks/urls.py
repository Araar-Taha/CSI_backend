from django.urls import path

from .views import CreateTacheView,RetrieveTacheView,DeleteTacheView,UpdateTacheView,AffectTacheToWooferView


urlpatterns = [
    path('create/', CreateTacheView.as_view(), name='create-tache'),
    path('<int:pk>/', RetrieveTacheView.as_view(), name='retrieve-tache'),
    path('update/', UpdateTacheView.as_view(), name='update-tache'),
    path('delete/', DeleteTacheView.as_view(), name='delete-tache'),
    path('affect/', AffectTacheToWooferView.as_view(), name='affect-tache'),

]