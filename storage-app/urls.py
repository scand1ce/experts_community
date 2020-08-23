from django.urls import path

from .views import UploadFilesView, ListFilesView, DeleteFilesView


urlpatterns = [

    path('file/<int:pk>/delete/', DeleteFilesView.as_view(), name='files_delete'),
    path('files-list/', ListFilesView.as_view(), name='files_list'),
    path('storage-app/', UploadFilesView.as_view(), name='files_upload'),

]


