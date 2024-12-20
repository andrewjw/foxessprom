FROM python:3.13

ARG VERSION

COPY dist/foxessprom-$VERSION.tar.gz /

RUN pip install /foxessprom-$VERSION.tar.gz --extra-index-url https://www.piwheels.org/simple

ENTRYPOINT ["foxessprom"]
CMD []
