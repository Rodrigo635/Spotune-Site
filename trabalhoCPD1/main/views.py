from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .music_utils import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Usamos o Bucket e o Insertion Sort! 
# Complexidades:
# Insertion Sort:
# Melhor caso: O(n) (onde n é o número de elementos)
# Pior caso: O(n^2)
# Bucket Sort:
# Melhor caso: O(n) (onde n é o número de baldes)
# Pior caso: O(n^2)

def ordenacao_spotune(songs):
    buckets = {}

    for song in songs:
        genre = song.genre
        if genre not in buckets:
            buckets[genre] = []
        buckets[genre].append(song)

    for genre, bucket in buckets.items():
        n = len(bucket)
        for i in range(1, n):
            key = bucket[i]
            j = i - 1
            while j >= 0 and (key.rating > bucket[j].rating or (key.rating == bucket[j].rating and key.title < bucket[j].title)):
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key

    sorted_songs = []
    for genre in sorted(buckets.keys()):
        sorted_songs.extend(buckets[genre])

    return sorted_songs

def home(request):
    songs = Song.generate_random_songs(1000)
    sorted_songs = ordenacao_spotune(songs)

    for song in sorted_songs:
        print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
    return render(request, 'home.html', {'songs': sorted_songs})

def saiba_mais(request):
    return render(request, 'saibamais.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'cadastro.html', {'error': 'Usuário já cadastrado'})
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('login')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})

def sair(request):
    logout(request)
    return redirect('home')        

@login_required
def playlist(request):
    return render(request, 'playlist.html')
