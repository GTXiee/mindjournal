from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import JournalForm
from .models import JournalEntry
from django.contrib.auth import get_user_model
@login_required
def journal_home(request):
    entries = JournalEntry.objects.filter(author=request.user.pk).order_by('actual_date').reverse()
    return render(request, "journal/journal_home.html", {'entries': entries})

@login_required
def journal_quotes(request):
    entries = JournalEntry.objects.filter(author=request.user.pk).order_by('actual_date').reverse()
    return render(request, "journal/journal_quotes.html", {'entries': entries})

@login_required
def journal_new(request):
    if request.method == "POST":
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            entry = JournalEntry()
            entry.author = request.user
            entry.actual_date = form.cleaned_data['actual_date']
            entry.content = form.cleaned_data['content']
            try:
                val = int(form.cleaned_data['posture_changes'])
            except TypeError:
                val = None
            entry.posture_changes = val
            if request.FILES:
                entry.image = request.FILES['image']
            entry.save()
            return redirect('journal_home')
        else:
            return HttpResponse('Form Error')

    else:
        form = JournalForm()

    return render(request, 'journal/journal_new.html', {'form': form})

@login_required
def journal_edit(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.user != entry.author:  # check the entry is of the user
        return redirect(journal_home)
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            entry.actual_date = form.cleaned_data['actual_date']
            entry.content = form.cleaned_data['content']
            try:
                val = int(form.cleaned_data['posture_changes'])
            except TypeError:
                val = None
            entry.posture_changes = val
            if request.FILES:
                entry.image = request.FILES['image']
            entry.save()
            return redirect('journal_home')
        else:
            return HttpResponse('Form Error')
    else:
        form = JournalForm(instance=entry)
        # return HttpResponse('Good')
        return render(request, 'journal/journal_new.html', {'form': form})

@login_required
def journal_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    # if request.user == get_object_or_404(get_user_model(), pk=entry.author_id):
    if request.user == entry.author:
        return render(request, 'journal/entry_detail.html', {'entry': entry})
    else:
        return redirect(journal_home)


