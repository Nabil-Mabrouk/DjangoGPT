# forms.py

from django import forms
from .models import ModelConfig, Step, Config, Learning

class ModelConfigForm(forms.ModelForm):
    class Meta:
        model = ModelConfig
        fields = ['name', 'description', 'version']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'version': 'Model Version',
        }

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['name', 'description']
        labels = {
            'name': 'Name',
            'description': 'Description',
        }


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ['name', 'description', 'steps']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'steps': 'Steps',
        }


class LearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = ['user', 'name', 'description','model', 'temperature', 'step_config', 'prompt', 'feedback']
        labels = {
            'user': 'User',
            'model': 'Model',
            'name':'Name',
            'description':'Description',
            'temperature': 'Temperature',
            'step_config': 'Step Config',
            'prompt': 'Prompt',
            'feedback': 'Feedback',
        }
