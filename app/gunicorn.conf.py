import multiprocessing

# Socket
bind = "0.0.0.0:8080"

# Debugging
reload = True

# Logging
loglevel = "debug"

# Proc Name
proc_name = "flask-app"

# Worker Process
workers = multiprocessing.cpu_count() * 2 + 1
threads = 1
worker_class = "sync"
worker_tmp_dir = "/dev/shm"
