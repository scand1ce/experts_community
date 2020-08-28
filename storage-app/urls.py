from django.urls import path

from .views import UploadFilesView, ListFilesView, DeleteFilesView


urlpatterns = [

    path('file/<int:pk>/', DeleteFilesView.as_view(), name='files_delete'),
    path('files/', ListFilesView.as_view(), name='files_list'),
    path('file/upload/', UploadFilesView.as_view(), name='files_upload'),

]


