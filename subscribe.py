import sys
import aiohttp
import asyncio
from difflib import unified_diff

from filters.openaidiff import openai_filter
from filters.naivemetadiff import naive_meta_filter


async def subscribe_and_ping(url: str, script: str) -> None:
    previous_html = None
    ping_idx = 0

    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as response:
                new_html = await response.text()
                ping_idx += 1
                diff = []

                if previous_html is not None:
                    diff = list(
                        unified_diff(
                            previous_html.splitlines(),
                            new_html.splitlines(),
                            n=0,
                            lineterm="",
                        )
                    )

                if naive_meta_filter(diff) and previous_html is not None:
                    print("Divergence Encountered! Publishing!")
                    return

                previous_html = new_html
                await asyncio.sleep(5)


async def main(NETWORK_URL: str, TARGET_SCRIPT: str):
    await subscribe_and_ping(NETWORK_URL, TARGET_SCRIPT)


if __name__ == "__main__":
    args = sys.argv

    if len(args) != 3:
        print("Usage: python3 subscribe.py {url} {script}")

    NETWORK_URL = args[1]
    TARGET_SCRIPT = args[2]
    asyncio.run(main(NETWORK_URL, TARGET_SCRIPT))
