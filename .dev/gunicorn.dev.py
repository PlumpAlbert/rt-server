import multiprocessing

bind = "0.0.0.0:80"
workers = multiprocessing.cpu_count()
wsgi_app = "app:app"
reload = True
loglevel = 'debug'
limit_request_line = 4096
