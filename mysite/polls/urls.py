from django.urls import path
from . import views


app_name = 'polls'
# urlpatterns = [
#     # e.g. /polls/
#     path('', views.index, name='index'),
#     # e.g. /polls/5
#     path('<int:question_id>/', views.detail, name='detail'),
#     # e.g. /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # e.g. /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    # e.g. /polls/
    path('', views.IndexView.as_view(), name='index'),
    # e.g. /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # e.g. /polls/5/results/
    path('<int:pk>/results/',
         views.ResultsView.as_view(), name='results'),
    # e.g. /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
