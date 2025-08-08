This project is to support a small music media startup in identifying and managing suspicious website traffic that was overwhelming their servers and causing frequent downtime. The goal was to analyse server logs, detect non-human activity (e.g. bots), and recommend a cost-effective, technically sound solution.


Log Parsing: Analyzes server logs using regular expressions to extract IP addresses, timestamps, endpoints, and user agents

Traffic Analysis: Identifies top IPs and most frequently accessed URLs

Suspicious Activity Detection: Flags IPs making unusually high request volumes

Visualisation: Plots request frequency over time using Matplotlib

Dockerized: Fully containerised with a Dockerfile for easy setup and platform-agnostic execution
