from django.http import HttpResponseRedirect, JsonResponse
from .tasks import do_something
from rest_framework.decorators import api_view
from celery.result import AsyncResult
from hero.celery import app
from hero.settings_config import FLOWER_URL, TASK_ID

@api_view(['POST'])
def do_job(request):
    # TODO add logger
    # TODO add serialize request
    res = do_something.delay()
    return JsonResponse({"job_id": res.task_id}, safe=False)

@api_view(['GET'])
def single_task(request):
    # TODO add logger
    # TODO add serialize request
    task_id = request.GET.get(TASK_ID)
    task_res = AsyncResult(task_id, app=app)
    # TODO add retrieve data with task_id from data source (s3 or other)
    return JsonResponse({"id": task_res.task_id, "state": task_res.state}, safe=False)

@api_view(['GET'])
def statistics(request):
    # TODO add logger
    return HttpResponseRedirect(FLOWER_URL)
    