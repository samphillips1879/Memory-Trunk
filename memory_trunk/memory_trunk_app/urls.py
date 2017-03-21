from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

app_name = 'memory_trunk_app'
urlpatterns = [

    # LANDING PAGE

    url(r'^$', views.IndexView.as_view(), name='index'),


    # AUTHENTICATION
    
    url(r'^register_user', views.register_user, name='register_user'),
    url(r'^user_registration', views.UserRegistration.as_view(), name='user_registration'),
    url(r'^login_user', views.login_views.login_user, name='login_user'),
    url(r'^logout_user', views.login_views.logout_user, name='logout_user'),
    url(r'^login', views.login_views.LoginUserView.as_view(), name='login_user_view'),


    # CREATION FORM VIEWS
    
        # Memory
    url(r'^hippocampus', views.hippocampus_view, name='hippocampus'),
    
        # Tip
    url(r'^tip_creation', views.tip_creation_view, name='tip_creation'),

        # Perspective
    url(r'^perspective_creation', views.perspective_creation_view, name='perspective_creation'),


    # LIST VIEWS

        # Memory
    url(r'^memory_list/(?P<id>\d+)/$', login_required(views.MemoryListView.as_view()), name='memory_list'),
    url(r'^community_memories/', views.PublicMemoryListView.as_view(), name='public_memory_list'),

        # Tip
    url(r'^tip_list/(?P<id>\d+)/$', login_required(views.TipListView.as_view()), name='tip_list'),
    url(r'^community_tips/', views.PublicTipListView.as_view(), name='public_tip_list'),

        # Perspective
    url(r'^perspective_list/(?P<id>\d+)/$', login_required(views.PerspectiveListView.as_view()), name='perspective_list'),
    url(r'^community_perspectives/', views.PublicPerspectiveListView.as_view(), name='public_perspective_list'),


    # DETAIL VIEWS
    
        # Memory
    url(r'^memory_detail/(?P<id>\d+)/$', views.MemoryDetailView.as_view(), name='memory_detail'),
    
        # Tip
    url(r'^tip_detail/(?P<id>\d+)/$', views.TipDetailView.as_view(), name='tip_detail'),
    
        # Perspective
    url(r'^perspective_detail/(?P<id>\d+)/$', views.PerspectiveDetailView.as_view(), name='perspective_detail'),


    # OBJECT DELETION VIEWS

        # Memory
    url(r'^delete_memory/(?P<id>\d+)/$', views.delete_memory, name='delete_memory'),
    
        # Tip
    url(r'^delete_tip/(?P<id>\d+)/$', views.delete_tip, name='delete_tip'),
    
        # Perspective
    url(r'^delete_perspective/(?P<id>\d+)/$', views.delete_perspective, name='delete_perspective'),


    # UPDATE VIEWS

        # Memory
    url(r'^update_memory/(?P<id>\d+)/$', views.update_memory, name='update_memory'),

        # Tip
    url(r'^update_tip/(?P<id>\d+)/$', views.update_tip, name='update_tip'),

        # Perspective
    url(r'^update_perspective/(?P<id>\d+)/$', views.update_perspective, name='update_perspective'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)














