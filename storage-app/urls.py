from django.urls import path


from .views import UploadFilesView, ListFileView


urlpatterns = [


    path('files/', ListFileView.as_view(), name='files_list'),
    path('storage-app/', UploadFilesView.as_view(), name='files_upload'),

]

