from django import forms

from leads.models import Lead
from team.models import Team


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "name",
            "email",
            "description",
            "priority",
            "status",
            # "team",
        )
    
    
