# Use an official Python base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y openjdk-11-jdk-headless curl \
    && apt-get clean

# Install Spark
ENV SPARK_VERSION=3.3.2
RUN curl -O https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz \
    && tar -xvf spark-$SPARK_VERSION-bin-hadoop3.tgz \
    && mv spark-$SPARK_VERSION-bin-hadoop3 /opt/spark \
    && rm spark-$SPARK_VERSION-bin-hadoop3.tgz

# Set environment variables for Spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy project files
WORKDIR /app
COPY netflix_eda.py /app/netflix_eda.py
COPY netflix_titles.csv /app/netflix_titles.csv

# Run the Python script
CMD ["python", "2021528_EDA.py"]
