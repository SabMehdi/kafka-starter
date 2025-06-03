# IoT Real-Time Data Pipeline with Kafka, InfluxDB & Grafana

This project demonstrates a real-time data pipeline for IoT sensor data using **Python**, **Kafka**, **InfluxDB**, and **Grafana**. It simulates temperature sensors, streams data through Kafka, stores it in InfluxDB, and visualizes it with Grafana. All services are containerized with Docker Compose for easy setup.

## 🏗️ Architecture

```
[Python Producer] --> [Kafka] --> [Python Consumer] --> [InfluxDB] --> [Grafana]
```

- **Producer**: Simulates temperature sensors and sends data to Kafka.
- **Kafka**: Message broker for reliable, scalable data streaming.
- **Consumer**: Reads data from Kafka and writes it to InfluxDB.
- **InfluxDB**: Time-series database for efficient storage and querying.
- **Grafana**: Visualizes sensor data in real time.
- **Docker Compose**: Orchestrates all services for easy deployment.

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone the Repository

```bash
git clone https://github.com/SabMehdi/kafka-starter.git
cd kafka-starter
```

### 2. Start the Services

```bash
docker-compose up -d
```

This will start Kafka, Zookeeper, InfluxDB, and Grafana.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Producer and Consumer

Open two terminals:

**Terminal 1: Start the Producer**
```bash
python producer/producer.py
```

**Terminal 2: Start the Consumer**
```bash
python consumer/consumer.py
```

### 5. Access Grafana Dashboard

- Open [http://localhost:3000](http://localhost:3000)
- Default login: `admin` / `admin`
- Add InfluxDB as a data source (URL: `http://influxdb:8086`, database: `sensordata`, token: `mytoken`, org: `myorg`)
- Create dashboards to visualize your sensor data.

## 📂 Project Structure

```
.
├── consumer/
│   └── consumer.py
├── producer/
│   └── producer.py
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

## ⚙️ Configuration

- **InfluxDB**: Configured in `docker-compose.yaml` (bucket: `sensordata`, org: `myorg`, token: `mytoken`)
- **Kafka**: Runs on `localhost:9092`
- **Python scripts**: Update connection parameters as needed in `producer.py` and `consumer.py`

## 📝 Example Data

```json
{
  "sensor_id": "sensor-1",
  "temperature": 25.34,
  "timestamp": 1712345678
}
```

![image](https://github.com/user-attachments/assets/befa83ac-bef7-43eb-8d4d-df0ae05f86c4)


---

Feel free to adjust the repository URL, credentials, or add more sections as needed! If you want a `requirements.txt` or a sample Grafana dashboard JSON, just ask.
