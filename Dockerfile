FROM python:3.12

ARG VERSION

RUN pip install foxessprom==$VERSION

ENTRYPOINT ["foxessprom"]
CMD []
