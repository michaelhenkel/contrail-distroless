FROM index.docker.io/michaelhenkel/distroless_config:debug
ADD python-contrail.tgz /usr/lib/python2.7/dist-packages
ENV PYTHONPATH=/usr/lib/python2.7:/usr/lib/python2.7/dist-packages
#COPY contrail-api /
