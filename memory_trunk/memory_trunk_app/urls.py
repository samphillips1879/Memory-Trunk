from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'memory_trunk_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^register_user', views.RegisterUser, name='register_user'),
    url(r'^register_user', views.register_user, name='register_user'),
    url(r'^user_registration', views.UserRegistration.as_view(), name='user_registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

