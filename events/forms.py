from django import forms
from events.models import Participant, Category, Event

class StyledFormMixin:
    """ Mixing to apply style to form field"""

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': "border-2 border-gray-300 w-1/2 p-3 rounded-lg shadow-sm space-y-2 bg-white text-gray-700"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })


# Django Model Form


class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time','location', 'category', 'guests']
        widgets = {
            'date': forms.SelectDateWidget,
            'guests': forms.CheckboxSelectMultiple,
            'category':forms.Select
        }

#     """ Widget using mixins """

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()



class CategoryModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

#     """ Widget using mixins """

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()


class ParticipantModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name','email']

#     """ Widget using mixins """

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()


# email validation