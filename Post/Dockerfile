# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY Posts/requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app code to the container
COPY Posts/ .

# Run the Flask app
CMD ["python", "app.py"]
