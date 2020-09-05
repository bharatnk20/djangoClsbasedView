from django.urls import path
from . import views
from . views import MyView, FinnCreate, FinnList, FinnDetail, FinnUpdate, FinnDelete, FinnFormContact

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', MyView.as_view()),
    path('create/', FinnCreate.as_view()),
    path('list/', FinnList.as_view()),
    path('<pk>/',FinnDetail.as_view()),
    path('<pk>/update',FinnUpdate.as_view()),
    path('<pk>/delete',FinnDelete.as_view()),
    path('contact/', FinnFormContact.as_view()),
    # path('get',views.getdata,),


]

