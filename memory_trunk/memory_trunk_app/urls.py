from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

app_name = 'memory_trunk_app'
urlpatterns = [

    # Landing page
    url(r'^$', views.IndexView.as_view(), name='index'),


    # User registration and authentication
    url(r'^register_user', views.register_user, name='register_user'),
    url(r'^user_registration', views.UserRegistration.as_view(), name='user_registration'),
    url(r'^login_user', views.login_views.login_user, name='login_user'),
    url(r'^logout_user', views.login_views.logout_user, name='logout_user'),
    url(r'^login', views.login_views.LoginUserView.as_view(), name='login_user_view'),


    # Creation Form Views
    
        # Memory
    url(r'^hippocampus', views.hippocampus_view, name='hippocampus'),
    
        # Tip
    url(r'^tip_creation', views.tip_creation_view, name='tip_creation'),


    # List Views

        # Memory
    url(r'^memory_list/(?P<id>\d+)/$', login_required(views.MemoryListView.as_view()), name='memory_list'),
    url(r'^community_memories/', views.PublicMemoryListView.as_view(), name='public_memory_list'),

        # Tip
    url(r'^tip_list/(?P<id>\d+)/$', login_required(views.TipListView.as_view()), name='tip_list'),
    url(r'^community_tips/', views.PublicTipListView.as_view(), name='public_tip_list'),


    # Detail Views
    
        # Memory
    url(r'^memory_detail/(?P<id>\d+)/$', views.MemoryDetailView.as_view(), name='memory_detail'),
    
        # Tip
    url(r'^tip_detail/(?P<id>\d+)/$', views.TipDetailView.as_view(), name='tip_detail'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

