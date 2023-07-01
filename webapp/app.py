# app.py
# This is the main Flask application file, now serving an HTML dashboard.

from flask import Flask, jsonify, render_template # Import render_template
import os
import sys

# Get the absolute path to the directory containing 'autosys' (the AUTOSYS_PORTFOLIO_PROJECT directory).
# This ensures 'autosys' can be imported as a top-level package.
# os.path.abspath(__file__) -> /home/toshi/Downloads/AutoSys_Portfolio_Project/autosys/webapp/app.py
# os.path.dirname(...) -> /home/toshi/Downloads/AutoSys_Portfolio_Project/autosys/webapp
# os.path.dirname(...) -> /home/toshi/Downloads/AutoSys_Portfolio_Project/autosys
# os.path.dirname(...) -> /home/toshi/Downloads/AutoSys_Portfolio_Project
project_base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_base_dir) # Use insert(0) to add it at the beginning of the path

# Attempt to import the monitor module.
# Now, 'autosys' should be recognized as a package.
try:
    from autosys.modules import monitor
except ImportError as e:
    print(f"Error: Could not import the 'monitor' module. Details: {e}")
    print("Please ensure 'autosys/__init__.py' and 'autosys/modules/__init__.py' exist,")
    print("and 'autosys/modules/monitor.py' is correctly structured.")
    # Define a dummy monitor object if the import fails, to prevent app crash
    class DummyMonitor:
        def get_cpu_usage(self):
            return {"error": "Monitor module not loaded", "value": "N/A"}
        def get_memory_usage(self):
            return {"error": "Monitor module not loaded", "value": "N/A"}
        def get_disk_usage(self):
            return {"error": "Monitor module not loaded", "value": "N/A"}
        def get_network_io(self):
            return {"error": "Monitor module not loaded", "value": "N/A"}
    monitor = DummyMonitor()


app = Flask(__name__)

# Configure the templates folder. By default, Flask looks for 'templates' in the same directory as app.py.
# If your templates are elsewhere, you might need to adjust this.
# In our case, it will be `webapp/templates/dashboard.html`

@app.route('/')
@app.route('/dashboard')
def dashboard():
    """
    This route serves the HTML dashboard.
    It fetches system metrics and passes them to the dashboard.html template.
    """
    cpu_data = monitor.get_cpu_usage()
    memory_data = monitor.get_memory_usage()
    disk_data = monitor.get_disk_usage()
    network_data = monitor.get_network_io() # Get network data

    return render_template(
        'dashboard.html',
        cpu=cpu_data,
        memory=memory_data,
        disk=disk_data,
        network=network_data
    )

@app.route('/api/metrics')
def api_metrics():
    """
    This route provides a JSON API endpoint for system metrics.
    It can be used by frontend JavaScript to dynamically update the dashboard.
    """
    cpu_data = monitor.get_cpu_usage()
    memory_data = monitor.get_memory_usage()
    disk_data = monitor.get_disk_usage()
    network_data = monitor.get_network_io()
    return jsonify({
        "cpu": cpu_data,
        "memory": memory_data,
        "disk": disk_data,
        "network": network_data
    })

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Access the dashboard at: http://127.0.0.1:5000/dashboard")
    print("Access the API at: http://127.0.0.1:5000/api/metrics")
    app.run(debug=True)
