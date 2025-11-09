# Import necessary libraries for the Flask web framework and Google Cloud Profiler
from flask import Flask, render_template, request

# Import the Cloud Profile
import googlecloudprofiler

# Create an instance of the Flask application
app = Flask(__name__)


# Define the main route for the application
@app.route("/")
def main():
    # Create a model dictionary to pass data to the template
    model = {"title": "Hello GCP."}
    # Render the index.html template with the model data
    return render_template('index.html', model=model)

# Initialize the Cloud Profiler
try:
    googlecloudprofiler.start(
        service='gcp-logging-design-process',
        service_version='1.0.0',
        verbose=3,
    )
except (ValueError, NotImplementedError) as exc:
    # Handle exceptions that may occur during the initialization of the Cloud Profiler
    print(f'Unable to start the Cloud Profiler: {exc}')

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    # Start the Flask application on host 0.0.0.0 and port 8080 with debug mode enabled
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)