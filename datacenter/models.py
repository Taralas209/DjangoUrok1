from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        now = timezone.localtime(timezone.now())
        entered_at_localtime = timezone.localtime(self.entered_at)
        if self.leaved_at:
            leaved_at_localtime = timezone.localtime(self.leaved_at)
            duration = leaved_at_localtime - entered_at_localtime
        else:
            duration = now - entered_at_localtime
        return duration


    def format_duration(duration):
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f'{hours}ч {minutes}мин'


    def is_visit_long(visit, minutes=60):
        if visit.leaved_at is not None:
            duration = visit.leaved_at - visit.entered_at
        else:
            duration = timezone.now() - visit.entered_at
        duration_in_minutes = duration.total_seconds() / 60
        return duration_in_minutes > minutes