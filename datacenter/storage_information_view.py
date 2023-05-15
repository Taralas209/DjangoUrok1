from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone



def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    local_time = timezone.localtime(timezone.now())
    non_closed_visits = []

    for visit in visits:
        duration = visit.get_duration()
        formatted_delta = Visit.format_duration(duration)
        is_strange = visit.is_visit_long()
        non_closed_visit = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': formatted_delta,
                'is_strange': is_strange,
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
