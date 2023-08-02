
from django.shortcuts import render, redirect, get_object_or_404
from .models import ModelConfig, Step, Config, Learning
from .forms import ModelConfigForm, StepForm, ConfigForm, LearningForm
from django.contrib.auth.decorators import login_required
import os, io
import zipfile
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

@login_required
def learning_list(request):
    # Retrieve all Learning objects for the authenticated user
    learnings = Learning.objects.filter(user=request.user)
    return render(request, 'PipelineGPT/learning_list.html', {'learnings': learnings})

@login_required
def learning_detail(request, pk):
    # Retrieve the specific Learning object for the authenticated user
    learning = get_object_or_404(Learning, pk=pk, user=request.user)
    return render(request, 'PipelineGPT/learning_detail.html', {'learning': learning})

@login_required
def learning_create(request):
    if request.method == 'POST':
        form = LearningForm(request.POST)
        if form.is_valid():
            learning = form.save(commit=False)
            learning.user = request.user
            learning.save()
            return redirect('learning_detail', pk=learning.pk)
    else:
        form = LearningForm()
    return render(request, 'PipelineGPT/learning_form.html', {'form': form})

@login_required
def learning_edit(request, pk):
    learning = get_object_or_404(Learning, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LearningForm(request.POST, instance=learning)
        if form.is_valid():
            form.save()
            return redirect('learning_detail', pk=learning.pk)
    else:
        form = LearningForm(instance=learning)
    return render(request, 'PipelineGPT/learning_form.html', {'form': form})

@login_required
def learning_delete(request, pk):
    learning = get_object_or_404(Learning, pk=pk, user=request.user)
    if request.method == 'POST':
        learning.delete()
        return redirect('learning_list')
    return render(request, 'PipelineGPT/learning_confirm_delete.html', {'learning': learning})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def config_create(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuration created successfully.')
            return redirect('config_list')
    else:
        form = ConfigForm()
    return render(request, 'PipelineGPT/config_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def config_edit(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'POST':
        form = ConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuration updated successfully.')
            return redirect('config_detail', pk=config.pk)
    else:
        form = ConfigForm(instance=config)
    return render(request, 'PipelineGPT/config_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def config_delete(request, pk):
    config = get_object_or_404(Config, pk=pk)
    if request.method == 'POST':
        config.delete()
        messages.success(request, 'Configuration deleted successfully.')
        return redirect('config_list')
    return render(request, 'PipelineGPT/config_confirm_delete.html', {'config': config})

@login_required
def config_list(request):
    configs = Config.objects.all()
    return render(request, 'PipelineGPT/config_list.html', {'configs': configs})

@login_required
def config_detail(request, pk):
    config = get_object_or_404(Config, pk=pk)
    return render(request, 'PipelineGPT/config_detail.html', {'config': config})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def model_config_create(request):
    if request.method == 'POST':
        form = ModelConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Model Configuration created successfully.')
            return redirect('model_config_list')
    else:
        form = ModelConfigForm()
    return render(request, 'PipelineGPT/model_config_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def model_config_edit(request, pk):
    model_config = get_object_or_404(ModelConfig, pk=pk)
    if request.method == 'POST':
        form = ModelConfigForm(request.POST, instance=model_config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Model Configuration updated successfully.')
            return redirect('model_config_detail', pk=model_config.pk)
    else:
        form = ModelConfigForm(instance=model_config)
    return render(request, 'PipelineGPT/model_config_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def model_config_delete(request, pk):
    model_config = get_object_or_404(ModelConfig, pk=pk)
    if request.method == 'POST':
        model_config.delete()
        messages.success(request, 'Model Configuration deleted successfully.')
        return redirect('model_config_list')
    return render(request, 'PipelineGPT/model_config_confirm_delete.html', {'model_config': model_config})

@login_required
def model_config_list(request):
    model_configs = ModelConfig.objects.all()
    return render(request, 'PipelineGPT/model_config_list.html', {'model_configs': model_configs})

@login_required
def model_config_detail(request, pk):
    model_config = get_object_or_404(ModelConfig, pk=pk)
    return render(request, 'PipelineGPT/model_config_detail.html', {'model_config': model_config})

@login_required
def step_list(request):
    steps = Step.objects.all()
    return render(request, 'PipelineGPT/step_list.html', {'steps': steps})

@login_required
def step_detail(request, pk):
    step = get_object_or_404(Step, pk=pk)
    return render(request, 'PipelineGPT/step_detail.html', {'step': step})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def step_create(request):
    if request.method == 'POST':
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Step created successfully.')
            return redirect('step_list')
    else:
        form = StepForm()
    return render(request, 'PipelineGPT/step_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def step_update(request, pk):
    step = get_object_or_404(Step, pk=pk)
    if request.method == 'POST':
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            messages.success(request, 'Step updated successfully.')
            return redirect('step_list')
    else:
        form = StepForm(instance=step)
    return render(request, 'PipelineGPT/step_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def step_delete(request, pk):
    step = get_object_or_404(Step, pk=pk)
    if request.method == 'POST':
        step.delete()
        messages.success(request, 'Step deleted successfully.')
        return redirect('step_list')
    return render(request, 'PipelineGPT/step_confirm_delete.html', {'step': step})


@login_required
def execute_learning(request, pk):
    learning = get_object_or_404(Learning, pk=pk, user=request.user)
    # Perform execution logic here (execute the learning and produce code)

    print(f'Executing learning : {learning.name}')

    # Redirect back to the dashboard after execution
    return redirect('learning_list')


@login_required
def download_code(request, pk):
    learning = get_object_or_404(Learning, pk=pk, user=request.user)

    try:
        # Create an in-memory zip file
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zip_file:
            for file_path in learning.file_names:
                zip_file.write(file_path, os.path.basename(file_path))

        # Create a downloadable response
        response = HttpResponse(buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{learning.session}.zip"'
        return response

    except Exception as e:
        # Handle any exceptions here (e.g., file not found, zip creation error)
        raise Http404("Error occurred while creating the zip file: " + str(e))




