from django.urls import re_path, path
from .views import RegisterView

from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)

'''
    re_path(r'^style/$', views.StyleList.as_view()),
    re_path(r'^style/([0-9]+)$', views.StyleDetail.as_view()),

    re_path(r'^user/$', views.UserList.as_view()),
    re_path(r'^user/([0-9]+)$', views.UserDetail.as_view()),

    re_path(r'^SaveFile$', views.SaveFile)'''