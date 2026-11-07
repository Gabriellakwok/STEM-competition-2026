# start with a base that already has python yay i love doing stuff im so smart
FROM python:3.12-slim

# make a folder 
WORKDIR /app
# put agent script inside container im actually pro
COPY agent.py .

# The secret (i love secrets)
# In real life this is how credentials get leaked to a running process.
ENV API_SECRET="TOP-SECRET-API-KEY-12345"

# When the container starts, run the agent
CMD ["python", "agent.py"]
