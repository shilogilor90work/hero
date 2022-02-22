from django.urls import path
from .views import do_job, statistics, single_task
from hero.settings_config import JOB_PATH, STATISTICS_PATH, SINGLE_TASK_PATH

urlpatterns = [
    path(JOB_PATH, do_job, name="do_job"),
    path(STATISTICS_PATH, statistics, name="statistics"),
    path(SINGLE_TASK_PATH, single_task, name="single_task")
]
