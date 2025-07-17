Engineering Skills Project Report

Tackling Bot Traffic for a Growing Music Startup

As part of this project, I was tasked with helping a small music media startup investigate why their website was crashing so often. After looking into the server logs, it became clear that certain pages were getting hit thousands of times — for example, /episodes/ep-42-synthesizer-history, /contact, and /about had each been accessed over 15,000 times.

What stood out even more was that a handful of IP addresses were behind a large portion of the traffic. IPs like 45.133.1.1 and 45.133.1.2 had made more than 5,000 requests each in a very short period. That’s not something a regular user would do — it pointed strongly to automated traffic, most likely bots. With such a small engineering team in place, this kind of activity was pushing the site to its limits and getting in the way of actual users.

To help fix this, I explored a few practical and budget-friendly options the team could implement:
	•	Limit how often each IP can access the site, using a technique called rate limiting
	•	Block obvious bot traffic by looking at their patterns — like suspicious user agents or repeated behaviour
	•	Use Cloudflare’s free tools to filter out harmful traffic before it even reaches the site
	•	Set up simple monitoring scripts that can catch unusual traffic spikes early on

Together, these steps would help the team take back control of their traffic, keep the site more stable, and spend less time firefighting outages — all without needing a big budget or complex setup.
