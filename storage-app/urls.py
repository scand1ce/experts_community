from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UploadFilesView, ListFileView, DeleteFilesView


urlpatterns = [

    path('file/<int:pk>/delete/', DeleteFilesView.as_view(), name='files_delete'),
    path('files-list/', ListFileView.as_view(), name='files_list'),
    path('storage-app/', UploadFilesView.as_view(), name='files_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
