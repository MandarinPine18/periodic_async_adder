# Periodic Asynchronous Addition Program

## Description
This is similar to my previous asynchronous adder (link: https://github.com/ethanparab/async_adder). This one, however, contains some small differences. The addition task now prints to the worker as well as returning the sum. There is a new print message task as well which prints a message at the worker. Both have corresponding scripts. Finally, there is a scheduler included which schedules the adder to run every two seconds and the printer to run every five seconds. It runs on Python 3.7.

## Installation
IMPORTANT: This installation assumes Python 3.7 and pip are already installed.


First the directory of your preferred folder, the one where this repository will be cloned. Replace "/this/is/a/path/" with the path to your preferred folder.
```console
  # cd /this/is/a/path
```

Clone the repository.
```console
  $ git clone https://github.com/ethanparab/periodic_async_adder.git
```

Enter the directory.
```console
  # cd periodic_async_adder
```

(optional) Create a virtual environment.
```console
  $ mkdir .venv
  # python3 -m venv .venv
  # source .venv/bin/activate
```

Install the dependencies.
```console
  $ python3 -m pip install Django Celery redis django-extensions
```
The last dependency is only necessary to run the script provided additionally. If that functionality not necessary, it can be omitted if async_adder/async_adder/async_adder/settings.py file is edited slightly in "INSTALLED APPS" to omit it as well. However, if it is omitted here and not in the settings file or vice versa, an error will be returned. I recommend installation for the simplicity, but it may not be needed depending on usage.

Alternatively, you can install from the requirements.txt file, although this is not preferrable.
```console
  $ python3 -m pip install -r requirements.txt
```

Refer to https://redis.io/topics/quickstart for instructions for installing Redis.

## Usage

In one terminal window, start Redis.
```console
  # redis-server
```

In another terminal window, start a celery worker inside the /this/is/a/path/periodic_async_adder/periodic_async_adder/.
```console
  # cd /this/is/a/path/periodic_async_adder/periodic_async_adder/
  # celery worker -A async_adder
```
If an error is returned here, make sure the directory is correct and django-extensions was either omitted with the correct edits or installed earlier.

Minimize both windows. In a third, final terminal window, enter the same directory as the last one.
```console
  # cd /this/is/a/path/periodic_async_adder/periodic_async_adder/
```

There are several options now. Follow only the track applicable to your intention.

### 1. Run the scheduler
The scheduler is something included which runs the adder every two seconds and the printer every five seconds. The adder adds 16 and 16 only and the message is DjangoPy. To watch it in action from the worker perspective, look at the asciinema recording (link: https://asciinema.org/a/tnhbzv4wSvRhrKMf9ehnTcksr).
```sh
  # celery -A periodic_async_adder beat
```

### 2. Run a script
This will only work with django-extensions installed. There are two scripts included which automate the usage of the tasks. Replace script with either add or print and params with the corresponding parameters (for add, two numbers; for print, either many words in quotes or one with quotes optional).
```console
  # python3 manage.py runscript script --script-args params
```
### 3. Manually run the tasks
Alternatively, if django-extensions was not installed, certain commands must be submitted to the shell of manage.py. To enter the shell, submit the following command instead.
```console
  # python3 manage.py shell
```

Submit the following commands in sequence, substituting x and y for the values you want to add. 
```pycon
>>> from thumbnailer.tasks import adding_task
>>> result = adding_task.delay(x, y)
>>> result.get()
```
To print, set "result" to "print_msg.delay(msg)". Substitute the desired message with result.


## Credits
In this repository, code from the makers of Python, Redis, Django, Django Extensions, and Celery were used. In addition, much of this was derived from a blog from Adam McQuistan (link: https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/) and a blog from Jai Singhal (link: https://djangopy.org/how-to/handle-asynchronous-tasks-with-celery-and-django#periodic-tasks).

## License
This project is licensed under AGPL v3, included in the file titled LICENSE.
