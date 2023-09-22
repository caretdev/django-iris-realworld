FROM intersystemsdc/iris-community

EXPOSE 8000

COPY ./requirements.txt /home/irisowner/django-realworld/

ENV PATH=/home/irisowner/.local/bin:${PATH}

RUN \
  cd /home/irisowner/django-realworld && \
  pip3 install -r requirements.txt

COPY ./ /home/irisowner/django-realworld/

ENTRYPOINT [ "/tini", "--", "/home/irisowner/django-realworld/entrypoint.sh" ]
