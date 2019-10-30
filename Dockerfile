FROM index.docker.io/michaelhenkel/distroless_config:debug
#ADD site-packages.tgz /usr/local/lib/python2.7
ADD python-contrail.tgz /usr/lib/python2.7/dist-packages
#ADD site-packages64.tgz /usr/local/lib/python2.7
#ENV PYTHONPATH=/usr/lib/python2.7:/usr/lib/python2.7/dist-packages
COPY contrail-api /
