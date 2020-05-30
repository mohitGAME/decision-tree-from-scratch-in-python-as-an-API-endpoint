

from django.urls import path
from django.conf import urls
from .views import FileView, getAlgorithms, predictPurchase

urlpatterns = [
    path('upload', FileView.as_view()),
    path('predict', predictPurchase),
    path('algo/', getAlgorithms),

]
