from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.views.static import serve
from user import views
app_name='user'


router = SimpleRouter()


router.register('register',views.RegisterUserProfileView,'register')
router.register('update',views.UpdateUserProfileView,'update')


urlpatterns = [
    #path('login/',views.Login.as_view()),
    #path('login/',obtain_jwt_token),
    path('login/',views.LoginViewSet.as_view({'post': 'login'})),
    path('info/', views.UserProfilesListView.as_view()),
    re_path(r'^info/(?P<pk>\w+)/$', views.UserProfilesDetailsView.as_view()),
    re_path('media/(?P<path>.*)',serve,{"document_root":settings.MEDIA_ROOT}),
]

urlpatterns += router.urls
