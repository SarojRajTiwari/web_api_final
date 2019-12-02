from django.urls import path

from apis.news.views \
    import (CreateNewsAPIView,
    UpdateNewsAPIView, 
    ListNewsAPIView, 
    RetrieveNewsAPIView,
    DestroyNewsAPIView, 
    category_news, 
    politics_news_list,
    technologies_news_list,
    sports_news_list,
    fashions_news_list,
    # request_user_created_news,
    RequestUserNewsAPIView)

urlpatterns = [
    path("create/", CreateNewsAPIView.as_view(), name="create_news"),
    path("update/<int:pk>/", UpdateNewsAPIView.as_view(), name="update_news"),
    path("retrieve/<int:pk>/", RetrieveNewsAPIView.as_view(), name="retrieve_news"),
    path("destroy/<int:pk>/", DestroyNewsAPIView.as_view(), name="destroy_news"),
    path("list/", ListNewsAPIView.as_view(), name="list_news"),
    path("categories/", category_news, name="category"),
    path("categories/politics/", politics_news_list, name="politics_news_list"),
    path("categories/technologies/", technologies_news_list, name="technologies_news_list"),
    path("categories/sports/", sports_news_list, name="sports_news_list"),
    path("categories/fashions/", fashions_news_list, name="fashions_news_list"),
    # path("", request_user_created_news, name="request_user_created_news"),
    path("user/list/", RequestUserNewsAPIView.as_view(), name="request_user_news"),
]
