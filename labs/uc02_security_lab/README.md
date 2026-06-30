# UC-02: Security lab (runnable API)

## Start the vulnerable API

```bash
uvicorn demoapp.api.server:app --host 127.0.0.1 --port 8080
```

Open http://127.0.0.1:8080/docs

## Try these curls

```bash
curl -s http://127.0.0.1:8080/api/profiles
curl -s "http://127.0.0.1:8080/api/search?q=test"
```

## RubberDuck exercise

Run UC-02 prompt on `demoapp/config.py` and `demoapp/api/server.py`.

Find: exec in config load, pickle, SQL string in `/api/search`.

## Verify

```bash
python labs/uc02_security_lab/verify.py
```
