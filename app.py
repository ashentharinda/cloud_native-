import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Get CPU and memory metrics using psutil
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent

    # Determine if the metrics are above a certain threshold
    cpu_high = cpu_metric > 80
    mem_high = mem_metric > 80

    # Prepare a message based on metrics
    message = "Normal"
    if cpu_high or mem_high:
        message = "High CPU or Memory Usage Detected, Please Scale Up!!!"

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
