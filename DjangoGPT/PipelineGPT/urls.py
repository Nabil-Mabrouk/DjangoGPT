from django.urls import path

from . import views

urlpatterns = [

    path('steps/', views.step_list, name='step_list'),
    path('steps/<int:pk>/', views.step_detail, name='step_detail'),
    path('steps/create/', views.step_create, name='step_create'),
    path('steps/<int:pk>/update/', views.step_update, name='step_update'),
    path('steps/<int:pk>/delete/', views.step_delete, name='step_delete'),

    # Model Configurations
    path('model_configs/', views.model_config_list, name='model_config_list'),
    path('model_configs/<int:pk>/', views.model_config_detail, name='model_config_detail'),
    path('model_configs/create/', views.model_config_create, name='model_config_create'),
    path('model_configs/<int:pk>/edit/', views.model_config_edit, name='model_config_edit'),
    path('model_configs/<int:pk>/delete/', views.model_config_delete, name='model_config_delete'),

    # Step Configurations
    path('configs/', views.config_list, name='config_list'),
    path('configs/<int:pk>/', views.config_detail, name='config_detail'),
    path('configs/create/', views.config_create, name='config_create'),
    path('configs/<int:pk>/edit/', views.config_edit, name='config_edit'),
    path('configs/<int:pk>/delete/', views.config_delete, name='config_delete'),

    # Learning
    path('learnings/', views.learning_list, name='learning_list'),
    path('learnings/<int:pk>/', views.learning_detail, name='learning_detail'),
    path('learnings/create/', views.learning_create, name='learning_create'),
    path('learnings/<int:pk>/edit/', views.learning_edit, name='learning_edit'),
    path('learnings/<int:pk>/delete/', views.learning_delete, name='learning_delete'),

    #path('learnings/<int:pk>/execute/', views.LearningExecuteView.as_view(), name='execute_learning'),
    #path('learnings/<int:pk>/download/', views.LearningDownloadView.as_view(), name='download_learning'),

    
]
