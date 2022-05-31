import multiprocessing

bind = "127.0.0.1:80"
workers = multiprocessing.cpu_count()
wsgi_app = "app:app"
reload = True
loglevel = 'debug'
limit_request_line = 4096
