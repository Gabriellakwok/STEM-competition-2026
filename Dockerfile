# A tiny, free base image with Python already inside it.
FROM python:3.12-slim

WORKDIR /app
COPY agent.py .

# THE "VULNERABILITY": a secret is baked straight into the environment.
# In real life this is how credentials get leaked to a running process.
ENV API_SECRET="TOP-SECRET-API-KEY-12345"

# When the container starts, run the agent probe.
CMD ["python", "agent.py"]
