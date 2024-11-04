import os
from flask import Flask
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

app = Flask(__name__)

# Get the endpoint from environment variable (default to localhost:4317 if not set)
otel_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "localhost:4317")

# Initialize OpenTelemetry metrics
metric_exporter = OTLPMetricExporter(endpoint=otel_endpoint)
meter_provider = MeterProvider(
    metric_readers=[PeriodicExportingMetricReader(metric_exporter)]
)
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# Define a custom counter metric for sales
sales_counter = meter.create_counter(
    "number_of_sales",
    description="Counts the number of sales"
)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sales')
def track_sales():
    # Increment sales metric for each request to /sales
    sales_counter.add(1)
    return 'Sales count increased!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)