from django.db import models
from users.models import CustomUser

class ModelConfig(models.Model):
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Step(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Config(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    steps = models.ManyToManyField(Step)

    def __str__(self):
        return self.name
    
class Learning(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Foreign key to User model
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    model = models.ForeignKey(ModelConfig, on_delete=models.CASCADE)
    temperature = models.FloatField()
    step_config = models.ForeignKey(Config, on_delete=models.CASCADE)
    prompt = models.TextField()
    logs = models.TextField()
    workspace = models.TextField()
    feedback = models.TextField(blank=True, null=True)
    session = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=10, default="0.3")

    def __str__(self):
        return f"{self.model} - {self.session}"