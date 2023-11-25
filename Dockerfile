# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app code to the container
COPY . .

# Run both Flask apps using Gunicorn (adjust as needed)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app1:app", "-w", "4", "-b", "0.0.0.0:5001", "app2:app"]
