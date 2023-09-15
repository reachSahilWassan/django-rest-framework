from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductCreateAPIView.as_view()),
    # path("", views.product_alt_view),

    # path("<int:pk>/", views.product_alt_view),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),


    path("list-view", views.ProductListAPIView.as_view()),
    path("list-and-create", views.ProductListCreateAPIView.as_view()),
    # path("add-or-get-data", views.product_alt_view),
]