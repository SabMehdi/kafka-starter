from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json

# InfluxDB setup
bucket = "sensordata"
org = "myorg"
token = "mytoken"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Kafka setup
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    group_id='sensor-data-consumer-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    point = (
        Point("temperature")
        .tag("sensor_id", data["sensor_id"])
        .field("value", data["temperature"])
        .time(data["timestamp"], WritePrecision.S)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Written to InfluxDB: {data}")