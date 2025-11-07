## A universal "subscribe to any website" primitive

The idea in mind is, given that every website / infrastructure has some sort of webhook concept, where one can subscribe to events emitted on their website. This is reductive; all are in different formats and some do not offer such features. We aim to construct a more universal method allowing for subscription to any site, with a normalized API/interface for communication.

### Polling / filtering

Just a smatter of ideas, which can be discussed further. Perhaps final use is configurable, or is a combination of polling strategies / filter strategies.

- Distributed polling? Multiple workers pinging
- Webhook detector / auto-detect? Use AI for this?
- HEAD request optimizer? Cache change detection? etc.
- Selective DOM / diff monitoring? User defined which DOM piece / diff to watch
- AI diff detection

### Output

- Query a user defined webhook
- Run a user script / lambda
- Output is normalized

```
async def smart_subscribe(url: str, callback_url: str):
	"""Intelligent polling that balances latency with respect."""
	strategies = [
	# 1. Try webhooks first (instant)
	check_webhook_support(url),

	# 2. Use HEAD requests for quick checks
	head_request_monitoring(url, interval=10),

	# 3. Fall back to selective scraping
	targeted_scraping(url, selector=".job-listing", interval=30),
]
```

how to do this?

4. Distributed Polling Pools
   How: Multiple servers polling different URLs at staggered times
   Used by: Price trackers, stock bots, social media monitors
   Scale: Distribute load so single site doesn't see aggressive traffic
   Latency: Competitive (1-5 seconds)
   Respectfulness: ✅ Spreads requests across time and IPs
5. CDN/Cache-Aware Polling
   How: Check if content is cached before polling origin
   Implementation: Use Cloudflare cache status headers
   Latency: Seconds
   Respectfulness: ✅ Less burden on origin server
