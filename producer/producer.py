import time
import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

SENSOR_IDS = ['sensor-1', 'sensor-2', 'sensor-3']

while True:
    sensor_id = random.choice(SENSOR_IDS)
    temp = round(random.uniform(20, 30), 2)
    data = {
        'sensor_id': sensor_id,
        'temperature': temp,
        'timestamp': int(time.time())
    }
    producer.send('sensor-data', value=data)
    print(f"Sent: {data}")
    time.sleep(1)