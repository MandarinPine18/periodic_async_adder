
def run(x=0, y=0):
    try:
        from thumbnailer.tasks import adding_task

        task = adding_task.delay(int(x), int(y))
        print(task.get())

    except ValueError:
        err1 = "Invalid arguments to the script. Place at most two numeric values after --script-args separated by a "
        err2 = "space or no values, the default is 0."
        errstr = err1 + err2
        print(errstr)

    except ModuleNotFoundError as moderr:
        raise moderr
