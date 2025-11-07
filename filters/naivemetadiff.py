from pprint import pprint


def naive_meta_filter(diff_stream: list[str]) -> bool:
    print("==========================")
    print(f"Total diff lines: {len(diff_stream)}")

    def is_noise(line):
        """Return True if this line is just metadata/noise, not meaningful content."""
        lower = line.lower()

        noise_patterns = [
            "authenticity_token",
            "csrf",
            "request-id",
            "visitor-payload",
            "visitor-hmac",
            "html-safe-nonce",
            "data-pjax-transient",
            "data-turbo-transient",
            "timestamp",
        ]

        return any(pattern in lower for pattern in noise_patterns)

    # Filter out noise lines
    meaningful_lines = [line for line in diff_stream if not is_noise(line)]

    print(f"Meaningful lines after filter: {len(meaningful_lines)}")
    if meaningful_lines:
        pprint(meaningful_lines)

    return len(meaningful_lines) > 0
