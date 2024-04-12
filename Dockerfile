FROM python:3.11

ARG VERSION

RUN pip install foxessprom==$VERSION

ENTRYPOINT ["foxessprom"]
CMD []
