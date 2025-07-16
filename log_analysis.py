
import pandas as pd
import re
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

# Path to log file (update if needed)
log_file_path = "sample-log.log"

# Regular expression to parse log lines
log_pattern = re.compile(
    r'(?P<ip>\S+) - (?P<country>\S+) - \[(?P<datetime>[^\]]+)] '
    r'"(?P<method>\S+) (?P<url>\S+) HTTP/\d\.\d" (?P<status>\d{3}) (?P<size>\d+) "-" '
    r'"(?P<user_agent>[^"]+)" (?P<response_time>\d+)'
)

# Parse log entries
parsed_logs = []
with open(log_file_path, "r") as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            data["datetime"] = datetime.strptime(data["datetime"], "%d/%m/%Y:%H:%M:%S")
            data["status"] = int(data["status"])
            data["response_time"] = int(data["response_time"])
            parsed_logs.append(data)

df = pd.DataFrame(parsed_logs)

# Top IPs and URLs
print("\nTop IPs:")
print(df["ip"].value_counts().head(10))

print("\nTop URLs:")
print(df["url"].value_counts().head(10))

# Requests over time
requests_per_minute = df.groupby(df["datetime"].dt.strftime("%Y-%m-%d %H:%M")).size()
requests_per_minute.plot(figsize=(12, 6), title="Requests Per Minute")
plt.xlabel("Time")
plt.ylabel("Number of Requests")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Flag suspicious IPs
threshold = 1000
suspicious_ips = df["ip"].value_counts()
suspicious_ips = suspicious_ips[suspicious_ips > threshold]
print("\nSuspicious IPs (more than 1000 requests):")
print(suspicious_ips)
