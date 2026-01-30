from __future__ import annotations

import os


def get_minimaxi_anthropic_endpoint(
    base_url: str | None = None, *, version: str = "v1"
) -> str:
    """Return the full Anthropic responses endpoint for Minimax.

    Minimax's Anthropic-compatible API expects a versioned base path (e.g.
    https://api.minimaxi.com/anthropic/v1). If callers accidentally omit the
    version segment and call .../anthropic/responses directly, the service
    returns a 404. This helper normalizes the base URL to avoid that.
    """

    resolved_base = base_url or os.getenv(
        "MINIMAXI_ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic"
    )
    normalized_base = resolved_base.rstrip("/")
    required_suffix = f"/anthropic/{version}"

    if normalized_base.endswith("/anthropic"):
        normalized_base = f"{normalized_base}/{version}"
    elif not normalized_base.endswith(required_suffix):
        normalized_base = f"{normalized_base}/anthropic/{version}"

    return f"{normalized_base}/responses"
