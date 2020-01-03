
def run(msg=None):
    try:
        from thumbnailer.tasks import print_msg

        print_msg.delay(msg)

    except ModuleNotFoundError as moderr:
        raise moderr
