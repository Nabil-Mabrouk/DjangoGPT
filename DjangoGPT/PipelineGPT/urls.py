from django.urls import path

from . import views

urlpatterns = [
    # Model Configurations
    path('model-configurations/', views.ModelConfigListView.as_view(), name='model_config_list'),
    path('model-configurations/create/', views.ModelConfigCreateView.as_view(), name='create_model_config'),
    path('model-configurations/<int:pk>/', views.ModelConfigDetailView.as_view(), name='model_config_detail'),
    path('model-configurations/<int:pk>/update/', views.ModelConfigUpdateView.as_view(), name='update_model_config'),
    path('model-configurations/<int:pk>/delete/', views.ModelConfigDeleteView.as_view(), name='delete_model_config'),

    # Step Configurations
    path('step-configurations/', views.StepConfigListView.as_view(), name='step_config_list'),
    path('step-configurations/create/', views.StepConfigCreateView.as_view(), name='create_step_config'),
    path('step-configurations/<int:pk>/', views.StepConfigDetailView.as_view(), name='step_config_detail'),
    path('step-configurations/<int:pk>/update/', views.StepConfigUpdateView.as_view(), name='update_step_config'),
    path('step-configurations/<int:pk>/delete/', views.StepConfigDeleteView.as_view(), name='delete_step_config'),

    # Learning
    path('learnings/', views.LearningListView.as_view(), name='learning_list'),
    path('learnings/create/', views.LearningCreateView.as_view(), name='create_learning'),
    path('learnings/<int:pk>/', views.LearningDetailView.as_view(), name='learning_detail'),
    path('learnings/<int:pk>/execute/', views.LearningExecuteView.as_view(), name='execute_learning'),
    path('learnings/<int:pk>/download/', views.LearningDownloadView.as_view(), name='download_learning'),

    # Dashboard
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
