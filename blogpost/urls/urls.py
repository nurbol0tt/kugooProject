from django.urls import path

from blogpost.views import views

urlpatterns = [
    path('questions_answers_list/', views.QuestionAnswerListView.as_view()),
    path('service_center_list/', views.ServiceCenterListView.as_view()),
    path('store_point_list/', views.StorePointsListView.as_view()),
    path('blog_post_list/', views.BLogListView.as_view()),
    path('video_list/', views.VideoListView.as_view()),
    path('offer/<int:pk>/', views.OfferListView.as_view()),
]
