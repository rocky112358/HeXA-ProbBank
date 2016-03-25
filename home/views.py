from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from account.models import Account
from gameboard.models import Categories, Entries, LogEntries, SolverListModel
from noticeboard.models import NoticeEntries

def home(request):

    if request.user.is_superuser:
        categories = Categories.objects.all()
        solver_list = SolverListModel.objects.all()
        log_entries = LogEntries.objects.all().order_by('-id')[:50]
        notice_entries = NoticeEntries.objects.all()
        problem_entries = Entries.objects.all().order_by('category', 'point')
        context = {
            'solver_list': solver_list,
            'categories': categories,
            'problem_entries': problem_entries,
            'notice_entries': notice_entries,
            'log_entries': log_entries,
        }
        return render(request, "admin/home.html", context)

    else:  
        template = "home.html"
        return render(request, "home.html")

