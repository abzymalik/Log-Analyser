Identifying and Reducing Bot Traffic for a Music Media Startup

To investigate frequent downtime issues faced by a small music media startup, I analysed over 432,000 server log entries spanning four days. While the average user made between 1–50 requests, the data showed that 16 IP addresses alone generated over 36,000 requests — around 8.3% of all traffic — with clear bot-like patterns.

Key findings included automated activity during low- and high-traffic periods. For example:
	•	35.185.0.156 scraped thousands of unique endpoints during off-peak hours (5–5:30am),
	•	IPs in the 45.133.1.x range ran systematic API enumeration during working hours,
	•	The 194.168.1.x range spiked traffic at peak lunchtime,
	•	And credential stuffing attempts from 185.220.x.x targeted login endpoints in the evening.

Bots typically used limited or suspicious user-agents (e.g. python-requests, curl) and caused a high number of 404 and 429 errors, indicating brute-force endpoint scanning and existing but insufficient rate limiting.

Recommendations

To quickly and cost-effectively reduce strain on the servers and improve uptime, I propose the following:
	•	Block identified IP ranges: Removing traffic from the top 16 IPs will reduce over 36,000 unnecessary requests.
	•	Rate limiting with Nginx: Restrict IPs to 10–20 requests per minute to mitigate brute-force and scraping attempts.
	•	User-Agent filtering: Block obvious bot signatures like python-requests, scraper, or bot.
	•	Cloudflare WAF (Free or Pro Tier): Add a protective layer to detect and filter malicious traffic before it hits the origin server.

Combined, these actions will significantly reduce downtime and allow the three-person engineering team to focus on growth, not firefighting. This solution is scalable, low-maintenance, and can be implemented at little to no cost.
