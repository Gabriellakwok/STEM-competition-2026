#!/usr/bin/env python3

import socket
import datetime

SECRET = "TOP-SECRET-API-KEY-12345"
TARGET = ("1.1.1.1", 443)


def log(message):
    stamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{stamp}] {message}", flush=True)


def probe(egress_allowed):
    log(f"Agent found exposed secret: {SECRET!r}")
    if not egress_allowed:
        log("Egress policy = DENY. The agent is not even allowed to open a socket.")
        log("RESULT: CONTAINED  -  the sandbox blocked the escape")
        return
    log(f"Attempting outbound connection to {TARGET[0]}:{TARGET[1]} ...")
    try:
        conn = socket.create_connection(TARGET, timeout=4)
        conn.close()
        log("Outbound connection SUCCEEDED.")
        log(f">>> ESCAPE: the agent could now send {SECRET!r} to an attacker.")
        log("RESULT: ESCAPED  -  the sandbox did NOT contain the agent")
    except Exception as exc:
        log(f"Connection failed: {exc}")
        log("RESULT: CONTAINED")


print("=" * 60)
print("TRIAL A  -  WEAK SANDBOX  (egress allowed)")
print("=" * 60)
probe(egress_allowed=True)

print()
print("=" * 60)
print("TRIAL B  -  HARDENED SANDBOX  (egress denied)")
print("=" * 60)
probe(egress_allowed=False)

print()
print("Same script, two policies. The firewall rule is the controlled variable.")
