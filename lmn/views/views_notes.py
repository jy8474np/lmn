from django.shortcuts import render, redirect, get_object_or_404

from ..models import Venue, Artist, Note, Show
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def new_note(request, show_pk):

    show = get_object_or_404(Show, pk=show_pk)

    if request.method == 'POST' :
        form = NewNoteForm(request.POST, request.FILES, instance=show_pk)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.show = show
            note.save()
            messages.info(request, 'Your show notes have been updated.')
        else:
            messages.error(request, 'Something went wrong. Please review your entries.')
        
        return redirect('note_detail', show_pk=show_pk)

    else :
        form = NewNoteForm()
    return render(request, 'lmn/notes/new_note.html' , { 'form': form , 'show': show })

@login_required
def delete_note(request, show_pk):

    show = get_object_or_404(Show, pk=show_pk)

    if request.method == 'POST' :
        form = NewNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.delete(commit=False)
            note.user = request.user
            note.show = show
            note.delete()
            return redirect('note_detail', note_pk=note.pk)
        else:
            return HttpResponseForbidden()

    else :
        form = NewNoteForm()

    return render(request, 'lmn/notes/new_detail.html' , { 'form': form , 'show': show })

def latest_notes(request):
    notes = Note.objects.all().order_by('-posted_date')
    return render(request, 'lmn/notes/note_list.html', { 'notes': notes })


def notes_for_show(request, show_pk): 
    # Notes for show, most recent first
    notes = Note.objects.filter(show=show_pk).order_by('-posted_date')
    show = Show.objects.get(pk=show_pk)  
    return render(request, 'lmn/notes/note_list.html', { 'show': show, 'notes': notes })


def note_detail(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)

    if place.user !=request.user:
        return HttpResponseForbidden

    if request.method == 'POST' :
        form = NewNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():

    return render(request, 'lmn/notes/note_detail.html' , { 'note': note })
