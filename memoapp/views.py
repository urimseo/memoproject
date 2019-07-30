from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Memo
from .forms import CommentForm
# Create your views here.

def home(request):
    memos = Memo.objects
    return render(request, 'home.html',{'memos' : memos})

def detail(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk = memo_id)
    return render(request, 'detail.html', {'memo':memo_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    memo = Memo()
    memo.title = request.GET['title']
    memo.body = request.GET['body']
    memo.pub_date = timezone.datetime.now()
    memo.save()
    return redirect('/memo/' + str(memo.id))

def delete(request, memo_id):
    memo_detail = get_object_or_404(Memo, pk = memo_id)
    memo_detail.delete()
    return redirect('home')

def edit(request, memo_id):
    if(request.method == 'POST'):
        memo_detail = get_object_or_404(Memo, pk = memo_id)
        return render(request, 'edit.html', {'memo':memo_detail})

def update(request, memo_id):
    memo = get_object_or_404(Memo, pk = memo_id)
    if (request.method == 'POST'):
        memo.title = request.POST['title']
        memo.body = request.POST['body']
        memo.save()
        return redirect('/memo/' + str(memo.id))

def add_comment(request, memo_id):
    memo = get_object_or_404(Memo, pk = memo_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.memo = memo
            comment.save()
            return redirect('/memo/' + str(memo.id))
        else:
            form = CommentForm()
        return render(request, 'add_comment.html', {'form':form})
