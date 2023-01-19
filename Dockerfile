# Python image to use.
FROM python:3.10-slim

# allow statements and log messages to appear
ENV PYTHONUNBUFFERED True

# copy local code to container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# install requirements
RUN pip install -r requirements.txt

# expose
EXPOSE 80

# run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
