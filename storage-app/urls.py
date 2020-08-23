from django.urls import path

from .views import UploadFilesView, ListFileView, DeleteFilesView


urlpatterns = [

    path('file/<int:pk>/delete/', DeleteFilesView.as_view(), name='files_delete'),
    path('files-list/', ListFileView.as_view(), name='files_list'),
    path('storage-app/', UploadFilesView.as_view(), name='files_upload'),

]


