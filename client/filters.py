import django_filters
from .models import Status

class StatusFilter(django_filters.FilterSet):
    
    class Meta:
        model = Status
        fields = ['client', 'status_type']
        
