# UC-01: Understand Your Code

## Run the lab (no server needed)

```bash
python labs/uc01_understand/verify.py
python -m demoapp --help 2>nul || python -c "from demoapp.cmd.build import main; print('entry:', main)"
```

## RubberDuck exercise

Index this repo, then run the prompt in `docs/uc-01.md` on:

- `demoapp/cmd/build.py`
- `demoapp/application.py`

## What you should see

Call chain from `main()` → `build_main()` → `Application.build()` with file:line evidence.
