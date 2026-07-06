from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, PlaylistCreateView, PlaylistUpdateView, PlaylistDeleteView, search_songs_api, CuratorDashboardView, SongCreateView, SongDeleteView, GenreCreateView, GenreDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('playlist/new/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('playlist/<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('playlist/<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),
    path('api/search/', search_songs_api, name='search_songs_api'),
    path('management/', CuratorDashboardView.as_view(), name='curator_dashboard'),
    path('management/song/add/', SongCreateView.as_view(), name='add_song'),
    path('management/song/<int:pk>/delete/', SongDeleteView.as_view(), name='delete_song'),
    path('management/genre/add/', GenreCreateView.as_view(), name='add_genre'),
    path('management/genre/<int:pk>/delete/', GenreDeleteView.as_view(), name='delete_genre'),
]






