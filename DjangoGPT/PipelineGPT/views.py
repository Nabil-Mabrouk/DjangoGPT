
from django.shortcuts import render, redirect, get_object_or_404
from .models import ModelConfig, Step, Config, Learning
from .forms import ModelConfigForm, StepForm, ConfigForm, LearningForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    # get the current logged user
    user = request.user

    # Get all the learnings created by the user
    user_learnings = Learning.objects.filter(user=user)

    return render(request, 'dashboard.html', {
        'user_learnings': user_learnings,
    })

@login_required
def create_learning(request):
    if request.method == 'POST':
        form = LearningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pipelineGPT-dashboard')
    else:
        form = LearningForm()
    return render(request, 'create_learning.html', {'form': form})





def execute_learning(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    # Perform execution logic here (execute the learning and produce code)

    # Redirect back to the dashboard after execution
    return redirect('dashboard')

def download_code(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    # Get the code produced by the learning (assuming it's stored somewhere)

    # Return a file download response
    response = HttpResponse(code_content, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{learning.session}.zip"'
    return response










def create_model_config(request):
    if request.method == 'POST':
        form = ModelConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_config_list')
    else:
        form = ModelConfigForm()
    return render(request, 'create_model_config.html', {'form': form})

def model_config_list(request):
    model_configs = ModelConfig.objects.all()
    return render(request, 'model_config_list.html', {'model_configs': model_configs})

def edit_model_config(request, pk):
    model_config = get_object_or_404(ModelConfig, pk=pk)
    if request.method == 'POST':
        form = ModelConfigForm(request.POST, instance=model_config)
        if form.is_valid():
            form.save()
            return redirect('model_config_list')
    else:
        form = ModelConfigForm(instance=model_config)
    return render(request, 'edit_model_config.html', {'form': form})

def delete_model_config(request, pk):
    model_config = get_object_or_404(ModelConfig, pk=pk)
    if request.method == 'POST':
        model_config.delete()
        return redirect('model_config_list')
    return render(request, 'delete_model_config.html', {'model_config': model_config})

##################

def create_config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config_list')
    else:
        form = ConfigForm()
    return render(request, 'create_model_config.html', {'form': form})

def config_list(request):
    configs = Config.objects.all()
    return render(request, 'config_list.html', {'configs': configs})

def edit_config(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'POST':
        form = ConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return redirect('config_list')
    else:
        form = ConfigForm(instance=config)
    return render(request, 'edit_config.html', {'form': form})

def delete_config(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'POST':
        config.delete()
        return redirect('config_list')
    return render(request, 'delete_config.html', {'config': config})

################

def create_step(request):
    if request.method == 'POST':
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('step_list')
    else:
        form = StepForm()
    return render(request, 'create_step.html', {'form': form})

def step_list(request):
    steps = Step.objects.all()
    return render(request, 'step_list.html', {'steps': steps})

def edit_step(request, pk):
    step = get_object_or_404(Step, pk=pk)
    if request.method == 'POST':
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            return redirect('step_list')
    else:
        form = StepForm(instance=step)
    return render(request, 'edit_step.html', {'form': form})

def delete_step(request, pk):
    step = get_object_or_404(Step, pk=pk)
    if request.method == 'POST':
        step.delete()
        return redirect('step_list')
    return render(request, 'delete_step.html', {'step': step})

#######



def learning_list(request):
    learnings = Learning.objects.all()
    return render(request, 'learning_list.html', {'learnings': learnings})

def edit_learning(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    if request.method == 'POST':
        form = LearningForm(request.POST, instance=learning)
        if form.is_valid():
            form.save()
            return redirect('learning_list')
    else:
        form = LearningForm(instance=learning)
    return render(request, 'edit_learning.html', {'form': form})

def delete_learnng(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    if request.method == 'POST':
        learning.delete()
        return redirect('learnng_list')
    return render(request, 'delete_learning.html', {'learning': learning})


@login_required
def dashboard(request):

    # get the current logged user
    user = request.user

    # Get all the learnings created by the user
    user_learnings = Learning.objects.filter(user=user)

    # Get all the model configs, steps, and step configs (optional: if needed for the dashboard)
    model_configs = ModelConfig.objects.all()
    steps = Step.objects.all()
    step_configs = Config.objects.all()

    # Handle new learning creation form submission
    if request.method == 'POST':
        form = LearningForm(request.POST)
        if form.is_valid():
            learning = form.save(commit=False)
            learning.user = user
            learning.save()
            return redirect('dashboard')

    else:
        form = LearningForm()

    return render(request, 'dashboard.html', {
        'user_learnings': user_learnings,
        'form': form,
        'model_configs': model_configs,
        'steps': steps,
        'step_configs': step_configs,
    })

def execute_learning(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    # Perform execution logic here (execute the learning and produce code)

    # Redirect back to the dashboard after execution
    return redirect('dashboard')

def download_code(request, pk):
    learning = get_object_or_404(Learning, pk=pk)
    # Get the code produced by the learning (assuming it's stored somewhere)

    # Return a file download response
    response = HttpResponse(code_content, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{learning.session}.zip"'
    return response




