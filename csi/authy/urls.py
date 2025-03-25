from django.urls import path
from .views import RegisterView,LoginView,LogoutView,AddWooferView,ModifyWooferView,DeleteUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('addwoofer/',AddWooferView.as_view(),name = 'addwoofer'),
    path('modifywoofer/',ModifyWooferView.as_view(), name='modifywoofer'),
    path('deleteuser/',DeleteUserView.as_view(),name='deleteuser')

]