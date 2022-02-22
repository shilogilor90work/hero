# Hero
Small task for job interview.

In this task I created a django server to handle a Restful API.
I used rabbitmq to handle the queue for the job requests.
I added celery to handle the jobs, and flower to view the metrics.

To handle too many requests, I should move this all to k8s.

In order to scale up the system, we can use the help of the following link:
https://learnk8s.io/scaling-celery-rabbitmq-kubernetes
