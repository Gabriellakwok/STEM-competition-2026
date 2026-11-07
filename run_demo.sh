#!/usr/bin/env bash
# run_demo.sh - Runs the whole A/B experiment with one command.
# Usage:  bash run_demo.sh
set -u

IMAGE="sandbox-agent-demo"

echo "############################################################"
echo "# Building the test image (first run takes ~30 sec) ..."
echo "############################################################"
docker build -t "$IMAGE" . || {
  echo
  echo "Build failed. Is Docker Desktop open and running?"
  exit 1
}

echo
echo "############################################################"
echo "# TRIAL A  -  WEAK SANDBOX  (default settings, full network)"
echo "#   command:  docker run --rm $IMAGE"
echo "############################################################"
docker run --rm "$IMAGE"

echo
echo "############################################################"
echo "# TRIAL B  -  HARDENED SANDBOX  (locked down)"
echo "#   --network none    : the container gets NO network at all"
echo "#   --cap-drop ALL    : strip every Linux privilege"
echo "#   --user 1000:1000  : run as an unprivileged user, not root"
echo "#   --read-only       : the filesystem cannot be written to"
echo "############################################################"
docker run --rm \
  --network none \
  --cap-drop ALL \
  --user 1000:1000 \
  --read-only \
  "$IMAGE"

echo
echo "############################################################"
echo "# DONE."
echo "#   Trial A should print:  RESULT: ESCAPED"
echo "#   Trial B should print:  RESULT: CONTAINED"
echo "#"
echo "# Same script. Same image. ONLY the isolation settings changed."
echo "# That is the proof: correct sandbox configuration stops the escape."
echo "############################################################"
