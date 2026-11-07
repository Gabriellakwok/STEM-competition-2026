#!/usr/bin/env python3
"""
What it does:
  1. Reads a FAKE secret from its environment. This simulates a credential
     that an app accidentally left exposed.
  2. Tries to open ONE outbound network connection to a public address.
  3. Prints the RESULT: ESCAPED (it got out) or CONTAINED (it was blocked).

The whole point of the experiment: run this exact same script in two
different sandboxes and watch the result change.
"""

import os
import socket
import datetime

# The "stolen" credential (fake, just for the demo.)
SECRET = os.environ.get("API_SECRET", "<no secret found>")

# A stable public endpoint, used ONLY to test if egress (outbound traffic)
# is possible. 1.1.1.1 is Cloudflare's public DNS resolver.
TARGET_HOST = "1.1.1.1"
TARGET_PORT = 443
TIMEOUT_SECONDS = 4


def log(message):
    stamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{stamp}] {message}", flush=True)


def main():
    log("=== Autonomous agent probe starting ===")
    log(f"Step 1  Found exposed secret in environment: {SECRET!r}")
    log(f"Step 2  Attempting outbound connection to {TARGET_HOST}:{TARGET_PORT} ...")

    try:
        conn = socket.create_connection(
            (TARGET_HOST, TARGET_PORT), timeout=TIMEOUT_SECONDS
        )
        conn.close()
        log("Step 3  OUTBOUND CONNECTION SUCCEEDED.")
        log(f"        >>> ESCAPE: the agent could now send {SECRET!r} to an attacker.")
        log("")
        log("RESULT: ESCAPED  -  the sandbox did NOT contain the agent")
    except Exception as exc:
        log(f"Step 3  Outbound connection FAILED: {type(exc).__name__}: {exc}")
        log("        >>> The agent is trapped. No data can leave this sandbox.")
        log("")
        log("RESULT: CONTAINED  -  the sandbox blocked the escape")

    log("=== Probe finished ===")


if __name__ == "__main__":
    main()
