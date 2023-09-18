from django.urls import path
from . import views

urlpatterns = [
    # Add task
    path('addTask/', views.addTask, name='addTask'),

    # Mark as done feature
    path('markComplete/<int:id>/', views.markComplete, name='markComplete'),

    # Mark as undone feature
    path('markUndone/<int:id>/', views.markUndone, name='markUndone'),

    # Edit task feature
    path('editTask/<int:id>', views.editTask, name='editTask')
]