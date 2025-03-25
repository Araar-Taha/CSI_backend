from django.urls import path

from .views import CreateTacheView,RetrieveTacheView,DeleteTacheView,UpdateTacheView


urlpatterns = [
    path('create/', CreateTacheView.as_view(), name='create-tache'),
    path('<int:pk>/', RetrieveTacheView.as_view(), name='retrieve-tache'),
    path('update/', UpdateTacheView.as_view(), name='update-tache'),
    path('delete/', DeleteTacheView.as_view(), name='delete-tache'),
]