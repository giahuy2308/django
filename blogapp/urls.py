from django.urls import path
from .views import *


urlpatterns = [
    path('account/list', AccountListView.as_view()),
    path('account/detail/<int:pk>', AccountDetailView.as_view()),
    path('main page/<int:pk>', MainPageView.as_view()),
    path('blog/list', BlogListView.as_view()),
    path('blog/detail/<int:pk>', BlogDetailView.as_view()),
    path('comments/list', CommentListView.as_view()),
    path('comments/detail/<int:pk>', CommentDetailView.as_view()),
]