# Python image to use.
FROM python:3.10

# set the working directory to /app
WORKDIR /app

# copy the requirements file
COPY ./requirements.txt /app/requirements.txt

#RUN pip install --upgrade pip

# install requirements
RUN pip install -r requirements.txt

# copy source code to /app
COPY . /app

# run server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# expose
EXPOSE 80