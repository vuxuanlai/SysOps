import time
from datetime import datetime
from influxdb import InfluxDBClient

def influx_api(db, host_name, title, log, action, type_name, time_stamp, note):
    json_body = [
        {
        "measurement": type_name,
        "tags": {
            "host_name": host_name,
        },
        "time": time_stamp,
        "fields": {
                "action" : action,
                "note": note,
                "log" : log,
                "value": 1
            }
        }]
    client = InfluxDBClient('107.113.53.104', 8086, 'admin', 'verysecret', db)
    client.write_points(json_body)
