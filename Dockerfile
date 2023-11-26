# Use the official Python 3.10 image as the base image
FROM python:3.10.11

# Set environment variables
SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim



RUN useradd -rms /bin/bash yt && chmod 777 /opt /run

WORKDIR /yt

RUN mkdir /yt/static && mkdir /yt/media && chown -R yt:yt /yt && chmod 755 /yt

COPY --chown=yt:yt . .

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN python manage.py collectstatic

USER yt


# Command to run the Django development server
CMD ["python" "manage.py" "collectstatic" "--noinput"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
