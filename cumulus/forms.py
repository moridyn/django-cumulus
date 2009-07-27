from django import forms

class CDNForm(forms.Form):
    """
    Allows a user to set container access via Limelight CDN.
    """
    public = forms.BooleanField(label="Public?", required=False)


class CreateContainerForm(forms.Form):
    """
    Allows a user to supply a name for creating a new container.
    """
    name = forms.CharField()