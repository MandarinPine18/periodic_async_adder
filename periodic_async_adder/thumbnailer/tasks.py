from celery import shared_task


@shared_task
def adding_task(x=0, y=0):
    z = x+y
    print("Now I have to add {} and {}. That equals {}".format(x, y, z))
    return z


@shared_task
def print_msg(name=None, *args, **kwargs):
    print("Celery is working!! {} is the message I have to say.".format(name))
    return None
