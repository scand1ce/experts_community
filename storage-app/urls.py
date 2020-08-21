from django.urls import path


from .views import UploadFilesView


urlpatterns = [

    path('storage-app/', UploadFilesView.as_view(), name='files_upload'),

]

