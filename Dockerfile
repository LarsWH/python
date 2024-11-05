FROM python:3
RUN pip install pytest
CMD ["tail", "-f", "/dev/null"]
