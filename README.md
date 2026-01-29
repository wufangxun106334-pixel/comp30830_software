# comp30380_software

modified by ykw
modified by alex on 1.29

## Minimax Anthropic endpoint configuration

If you see a 404 from `https://api.minimaxi.com/anthropic/responses`, the
environment is likely missing the versioned Anthropic base path. Configure a
versioned base URL and build the endpoint from it:

```bash
export MINIMAXI_ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic/v1"
```

Then use the helper in `minimaxi_config.py` to build the final endpoint URL.
