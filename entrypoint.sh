#!/bin/bash

set -m

/iris-main "$@" &

/usr/irissys/dev/Cloud/ICM/waitISC.sh
iris session iris -U%SYS '##class(Security.Users).Create("django","%ALL","django")' || true

cd /home/irisowner/django-realworld
python3 manage.py migrate
gunicorn \
    --bind 0.0.0.0:8000 \
    --workers=5 \
    --threads=1 \
    --daemon \
    --log-level debug \
    --capture-output \
    --enable-stdio-inheritance \
    realworld.wsgi 

fg %1