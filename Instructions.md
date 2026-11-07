# Instructions!!
## 1 The docker method

Using docker:
1. Install it here https://www.docker.com/products/docker-desktop/
2. Open a docker container:
Go to the correct directory

``` 
cd sandbox-demo
```

Then

```
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"
```

After that we start the container:

```
docker build -t sandbox-agent-demo .
```

Then we make it permanent so we do not need to start it every time

```
echo 'export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"' >> ~/.zshrc
```

```
source ~/.zshrc
```

3. Start running

```
bash run_demo.sh
```

See the results for trial A and B.

* What if I want to delete the image? (we just need images for now)
<img width="67" height="643" alt="Screenshot 2026-11-07 at 8 31 10 PM" src="https://github.com/user-attachments/assets/4e5cc1f3-cba7-45f3-a4f1-2cf80fe428d2" />

At the slightly darkened icon in the screenshot. 

Using docker desktop, you will see all the images and a trash can icon on the very right of it.

---

## 2 The method using a **real LLM agent**

Run 

```
brew install ollama
``` 

for MacOS, or simply install ollama. (Preferred in terminal)

Then

```
ollama serve
```

to start an ollama server. (This will use a terminal so use cmd T for macOS (idk for other systems) to start another tab to use.

```
ollama pull llama3.2:3b
```
or

```
ollama pull llama3.2:1b 
``` 

if it is sluggish.

Then

```
docker build -t sandbox-agent-demo .
```

Then we run the weak sandbox:

```
docker run -d --name target-weak sandbox-agent-demo sleep infinity
```

And the hardened sandbox

```docker run -d --name target-hardened \
  --network none --cap-drop ALL --user 1000:1000 --read-only \
  sandbox-agent-demo sleep infinity
```

And let the agent try to escape each one:

```
python3 agent_llm.py --container target-weak
```

```
python3 agent_llm.py --container target-hardened
```

Clean up when done:

```
docker rm -f target-weak target-hardened
```

## 3 Emergency backup (meaningless)

INSTALL PYTHON using brew or smth

Then

```
python3 fallback_demo.py
```







