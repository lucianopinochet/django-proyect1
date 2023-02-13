from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('candidate/<int:pk>',views.CandidateView.as_view(), name='c_info'),
    path('vote', views.vote, name='vote'),
    path('ty/<str:candidate>', views.ty, name='ty' )

]