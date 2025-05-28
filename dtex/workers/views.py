from django.shortcuts import render, get_object_or_404, redirect
from .models import Worker, WorkerActivity
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect

# WORKER VIEWS
def worker_list_old(request):
    workers = Worker.objects.all()
    return render(request, 'workers/worker_list.html', {'workers': workers})

def worker_list(request):
    workers = Worker.objects.all()

    # Get filter parameters
    name_query = request.GET.get('name')
    activity_type = request.GET.get('activity_type')
    risk_level = request.GET.get('risk_level')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if name_query:
        workers = workers.filter(name__icontains=name_query)

    if activity_type or risk_level or start_date or end_date:
        activities = WorkerActivity.objects.all()

        if activity_type:
            activities = activities.filter(name__icontains=activity_type)
        if risk_level:
            activities = activities.filter(risk_level=risk_level)
        if start_date:
            activities = activities.filter(timestamp__gte=parse_date(start_date))
        if end_date:
            activities = activities.filter(timestamp__lte=parse_date(end_date))

        # Filter workers who have those activities
        worker_ids = activities.values_list('worker_id', flat=True).distinct()
        workers = workers.filter(id__in=worker_ids)
        # Annotate high risk activity presence
        for worker in workers:
            worker.has_high_risk = any(
                activity.risk_level == 'high' for activity in worker.activities.all()
            )



    return render(request, 'workers/worker_list.html', {
        'workers': workers,
        'filters': {
            'name': name_query or '',
            'activity_type': activity_type or '',
            'risk_level': risk_level or '',
            'start_date': start_date or '',
            'end_date': end_date or ''
        }
    })

def worker_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        type = request.POST['type']
        Worker.objects.create(name=name, type=type)
        return redirect('worker_list')
    return render(request, 'workers/worker_form.html')


def worker_update(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        worker.name = request.POST['name']
        worker.type = request.POST['type']
        worker.save()
        return redirect('worker_list')
    return render(request, 'workers/worker_form.html', {'worker': worker})


def worker_delete(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'workers/worker_confirm_delete.html', {'worker': worker})


# ACTIVITY VIEWS
def activity_list(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    activities = worker.activities.all()
    return render(request, 'workers/activity_list.html', {
        'worker': worker,
        'activities': activities
    })


def activity_create(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    if request.method == 'POST':
        activity_type = request.POST['activity_type']
        risk_level = request.POST['risk_level']
        datetime = request.POST['datetime'] or timezone.now()
        WorkerActivity.objects.create(
            worker=worker,
            activity_type=activity_type,
            risk_level=risk_level,
            datetime=datetime
        )
        return redirect('activity_list', worker_id=worker.id)
    return render(request, 'workers/activity_form.html', {'worker_id': worker_id})



def activity_update(request, worker_id, pk):
    activity = get_object_or_404(WorkerActivity, pk=pk, worker_id=worker_id)
    if request.method == 'POST':
        activity.name = request.POST.get('name')
        activity.risk_level = request.POST.get('risk_level')
        activity.save()
        return redirect('activity_list', worker_id=worker_id)
    return render(request, 'workers/activity_form.html', {'activity': activity, 'worker_id': worker_id})



def activity_delete(request, worker_id, activity_id):
    activity = get_object_or_404(WorkerActivity, pk=activity_id, worker_id=worker_id)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list', worker_id=worker_id)
    return render(request, 'workers/activity_confirm_delete.html', {'activity': activity})
