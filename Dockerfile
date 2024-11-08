FROM python:3.12.7-bookworm
RUN pip install pytest
CMD ["tail", "-f", "/dev/null"]
