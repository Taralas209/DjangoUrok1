from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone



def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        duration = visit.get_duration()
        formatted_delta = Visit.format_duration(duration)
        is_strange = visit.is_visit_long()
        this_visit = {
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': formatted_delta,
            'is_strange': is_strange,
        }
        this_passcard_visits.append(this_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
