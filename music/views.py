from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Song, Playlist, Genre
from .forms import PlaylistForm
from django.http import JsonResponse
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recently_played'] = Song.objects.order_by('?')[:6]
        context['new_releases'] = Song.objects.order_by('?')[:6]
        context['playlists'] = Playlist.objects.order_by('?')[:4]

        user = self.request.user
        if user.is_authenticated:
            canzoni_salvate = Song.objects.filter(playlist__user=user)
            generi_preferiti = Genre.objects.filter(song__in=canzoni_salvate).distinct()
            raccomandazioni = Song.objects.filter(genre__in=generi_preferiti).exclude(id__in=canzoni_salvate).distinct().order_by('?')[:6]
            if not raccomandazioni.exists():
                raccomandazioni = Song.objects.order_by('?')[:6]
        else:
            raccomandazioni = Song.objects.order_by('?')[:6]
        context['raccomandazioni'] = raccomandazioni        
        
        return context
    
def search_songs_api(request):
        query = request.GET.get('q', '').strip()
        genre_name = request.GET.get('genre', '').strip()
        results = []
        songs = Song.objects.all()
        if genre_name:
            songs = songs.filter(genre__name__iexact=genre_name)
        if query:
            songs = songs.filter(
                Q(title__icontains=query) | 
                Q(artist__icontains=query)
            )
        if query or genre_name:
            songs = songs.distinct()[:10]
            for song in songs:
                results.append({
                    'id': song.id,
                    'title': song.title,
                    'artist': song.artist,
                })
        return JsonResponse({'results': results})

class PlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generi'] = Genre.objects.all()
        return context


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        playlist = self.get_object()
        return self.request.user == playlist.user
    
    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("You can't edit this playlist.")

class PlaylistUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist_form.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generi'] = Genre.objects.all()
        return context

class PlaylistDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'playlist_confirm_delete.html'
    success_url = reverse_lazy('home')



class CuratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.username == 'curatorDemo' or self.request.user.is_superuser)


class CuratorDashboardView(CuratorRequiredMixin, TemplateView):
    template_name = 'curator_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all().order_by('title')
        context['genres'] = Genre.objects.all().order_by('name')
        return context


class SongCreateView(CuratorRequiredMixin, CreateView):
    model = Song
    fields = ['title', 'artist', 'genre'] 
    template_name = 'song_form.html'
    success_url = reverse_lazy('curator_dashboard')


class SongDeleteView(CuratorRequiredMixin, DeleteView):
    model = Song
    template_name = 'song_confirm_delete.html'
    success_url = reverse_lazy('curator_dashboard')


class GenreCreateView(CuratorRequiredMixin, CreateView):
    model = Genre
    fields = ['name']
    template_name = 'genre_form.html'
    success_url = reverse_lazy('curator_dashboard')


class GenreDeleteView(CuratorRequiredMixin, DeleteView):
    model = Genre
    template_name = 'genre_confirm_delete.html'
    success_url = reverse_lazy('curator_dashboard')


# Create your views here.
