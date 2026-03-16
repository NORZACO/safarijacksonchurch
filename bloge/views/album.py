from django.shortcuts import render, get_object_or_404, redirect
from ..models import Album
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def libraries(request):
    albums = Album.objects.filter(status='published')
    return render(request, 'bloge/libraries.html', {'albums': albums})


def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug)
    return render(request, 'albums/detail.html', {'album': album})


@login_required
def album_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Album.objects.create(
            title=title,
            description=description,
            image=image,
            author=request.user,
            status="published"
        )

        return redirect('album_list')

    return render(request, 'albums/create.html')


@login_required
def album_update(request, slug):
    album = get_object_or_404(Album, slug=slug)

    if request.method == "POST":
        album.title = request.POST.get('title')
        album.description = request.POST.get('description')
        album.save()

        return redirect('album_detail', slug=slug)

    return render(request, 'albums/update.html', {'album': album})


@login_required
def album_delete(request, slug):
    album = get_object_or_404(Album, slug=slug)
    album.delete()
    return redirect('album_list')
