import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Child, DaycareParent, DaycareAttendance


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['child_count'] = Child.objects.count()
    ctx['child_infant'] = Child.objects.filter(group='infant').count()
    ctx['child_toddler'] = Child.objects.filter(group='toddler').count()
    ctx['child_preschool'] = Child.objects.filter(group='preschool').count()
    ctx['daycareparent_count'] = DaycareParent.objects.count()
    ctx['daycareparent_current'] = DaycareParent.objects.filter(billing_status='current').count()
    ctx['daycareparent_overdue'] = DaycareParent.objects.filter(billing_status='overdue').count()
    ctx['daycareparent_prepaid'] = DaycareParent.objects.filter(billing_status='prepaid').count()
    ctx['daycareattendance_count'] = DaycareAttendance.objects.count()
    ctx['daycareattendance_present'] = DaycareAttendance.objects.filter(status='present').count()
    ctx['daycareattendance_absent'] = DaycareAttendance.objects.filter(status='absent').count()
    ctx['daycareattendance_late'] = DaycareAttendance.objects.filter(status='late').count()
    ctx['recent'] = Child.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def child_list(request):
    qs = Child.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(group=status_filter)
    return render(request, 'child_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def child_create(request):
    if request.method == 'POST':
        obj = Child()
        obj.name = request.POST.get('name', '')
        obj.age = request.POST.get('age') or 0
        obj.parent_name = request.POST.get('parent_name', '')
        obj.parent_phone = request.POST.get('parent_phone', '')
        obj.parent_email = request.POST.get('parent_email', '')
        obj.group = request.POST.get('group', '')
        obj.allergies = request.POST.get('allergies', '')
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/childs/')
    return render(request, 'child_form.html', {'editing': False})


@login_required
def child_edit(request, pk):
    obj = get_object_or_404(Child, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.age = request.POST.get('age') or 0
        obj.parent_name = request.POST.get('parent_name', '')
        obj.parent_phone = request.POST.get('parent_phone', '')
        obj.parent_email = request.POST.get('parent_email', '')
        obj.group = request.POST.get('group', '')
        obj.allergies = request.POST.get('allergies', '')
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/childs/')
    return render(request, 'child_form.html', {'record': obj, 'editing': True})


@login_required
def child_delete(request, pk):
    obj = get_object_or_404(Child, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/childs/')


@login_required
def daycareparent_list(request):
    qs = DaycareParent.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(billing_status=status_filter)
    return render(request, 'daycareparent_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def daycareparent_create(request):
    if request.method == 'POST':
        obj = DaycareParent()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.children_count = request.POST.get('children_count') or 0
        obj.emergency_contact = request.POST.get('emergency_contact', '')
        obj.address = request.POST.get('address', '')
        obj.billing_status = request.POST.get('billing_status', '')
        obj.save()
        return redirect('/daycareparents/')
    return render(request, 'daycareparent_form.html', {'editing': False})


@login_required
def daycareparent_edit(request, pk):
    obj = get_object_or_404(DaycareParent, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.children_count = request.POST.get('children_count') or 0
        obj.emergency_contact = request.POST.get('emergency_contact', '')
        obj.address = request.POST.get('address', '')
        obj.billing_status = request.POST.get('billing_status', '')
        obj.save()
        return redirect('/daycareparents/')
    return render(request, 'daycareparent_form.html', {'record': obj, 'editing': True})


@login_required
def daycareparent_delete(request, pk):
    obj = get_object_or_404(DaycareParent, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/daycareparents/')


@login_required
def daycareattendance_list(request):
    qs = DaycareAttendance.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(child_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'daycareattendance_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def daycareattendance_create(request):
    if request.method == 'POST':
        obj = DaycareAttendance()
        obj.child_name = request.POST.get('child_name', '')
        obj.date = request.POST.get('date') or None
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.marked_by = request.POST.get('marked_by', '')
        obj.save()
        return redirect('/daycareattendances/')
    return render(request, 'daycareattendance_form.html', {'editing': False})


@login_required
def daycareattendance_edit(request, pk):
    obj = get_object_or_404(DaycareAttendance, pk=pk)
    if request.method == 'POST':
        obj.child_name = request.POST.get('child_name', '')
        obj.date = request.POST.get('date') or None
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.marked_by = request.POST.get('marked_by', '')
        obj.save()
        return redirect('/daycareattendances/')
    return render(request, 'daycareattendance_form.html', {'record': obj, 'editing': True})


@login_required
def daycareattendance_delete(request, pk):
    obj = get_object_or_404(DaycareAttendance, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/daycareattendances/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['child_count'] = Child.objects.count()
    data['daycareparent_count'] = DaycareParent.objects.count()
    data['daycareattendance_count'] = DaycareAttendance.objects.count()
    return JsonResponse(data)
