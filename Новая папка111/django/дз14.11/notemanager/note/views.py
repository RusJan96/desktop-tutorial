from django.shortcuts import render
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})
# Create your views here.
