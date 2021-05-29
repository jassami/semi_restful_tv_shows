
from semi_restful_app.models import Show
from django.shortcuts import render, redirect

def index(request):
    return redirect('/shows')

def shows(request):
    context= {
        'all_shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def show_info(request, show_id):
    context={
        'show': Show.objects.get(id = show_id)
    }
    return render(request, 'show_info.html', context)

def edit(request, show_id):
    if request.method == "GET":
        context={
        'show': Show.objects.get(id = show_id)
    }
        return render(request, 'edit.html', context)
    else:
        show= Show.objects.get(id = show_id)
        show.title= request.POST['title']
        show.network= request.POST['network']
        show.release_date= request.POST['release_date']
        show.description= request.POST['description']
        show.save()
        return redirect(f"/shows/{show_id}")

def new(request):
    if request.method =="GET":
        return render(request, 'new.html')
    else:
        new_show= Show.objects.create(title= request.POST['title'], network= request.POST['network'], release_date= request.POST['release_date'], description= request.POST['description'])
        return redirect(f"/shows/{new_show.id}")

def destroy(request, show_id):
    Show.objects.get(id = show_id).delete()
    return redirect('/shows')