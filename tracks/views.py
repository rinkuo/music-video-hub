from django.shortcuts import render, redirect, get_object_or_404
from .models import Track


def index(request):
    return render(request, 'index.html')


def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/music-list.html', {'tracks': tracks})

def track_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('audio_file')

        print(title, artist, album, genre, release_date, cover_image, audio_file)

        if title and artist and album and genre and release_date and cover_image and audio_file:
            Track.objects.create(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                release_date=release_date,
                cover_image=cover_image,
                audio_file=audio_file
            )
            return redirect('tracks:music_list')
    return render(request, 'tracks/music-create.html')

def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)

    if request.method == 'POST':
        track.title = request.POST.get('title')
        track.artist = request.POST.get('artist')
        track.album = request.POST.get('album')
        track.genre = request.POST.get('genre')
        track.release_date = request.POST.get('release_date')
        track.cover_image = request.FILES.get('cover_image') or track.cover_image
        track.audio_file = request.FILES.get('audio_file') or track.audio_file
        track.save()
        return redirect('tracks:music_detail', pk=track.pk)

    return render(request, 'tracks/music-create.html', {'track': track})

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'tracks/music-detail.html', {'track': track})


def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('tracks:music_list')
    return render(request, 'tracks/music-delete-confirm.html', {'track': track})
