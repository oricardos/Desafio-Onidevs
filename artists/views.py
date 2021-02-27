from django.shortcuts import render, redirect
from .models import Song
# importa o SongForm de forms.py
from .forms import SongForm


def model(request):
    return render(request, 'artists/model.html')


def list(request):
    data = {}
    data['songs'] = Song.objects.all()
    # retorna template de registro de artistas
    return render(request, 'artists/list.html', data)


def new_song(request):
    data = {}
    #https://stackoverflow.com/questions/38251922/logic-behind-formrequest-post-or-none
    form = SongForm(request.POST or None)

    # validação do form
    if form.is_valid():
        form.save()
        return redirect('list')

    data['form'] = form
    return render(request, 'artists/form.html', data)


def update(request, pk):
    data = {}
    song = Song.objects.get(pk=pk)
    #https://stackoverflow.com/questions/38251922/logic-behind-formrequest-post-or-none
    form = SongForm(request.POST or None, instance=song)

    # validação do form
    if form.is_valid():
        form.save()
        return redirect('list')

    data['form'] = form
    data['song'] = song
    return render(request, 'artists/form.html', data)


def delete(request, pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    return redirect('list')
