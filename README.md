# Gimbaled TVC Draft Documentation

This branch contains an experimental first draft of the StrictDoc and `syseng`
workflow for the Gimbaled TVC rocket documentation repository.

The mission records and requirements in this branch are not an approved TVC
baseline. They exist to draft candidate L0/L1 content while the documentation
workflow is still being proven.

## Contents

```text
requirements-tools.txt
syseng.toml
records/
  mission.sdoc
  requirements.sdoc
docs/
  verification/
    actuator-frequency-response-test.md
    attitude-estimate-analysis.md
```

`requirements-tools.txt` pins the `syseng-tools` release used by this
repository.

`syseng.toml` configures the project title, UID prefix, records directory, and
allowed applicability values.

`records/` contains draft StrictDoc source records.

`docs/verification/` contains placeholder evidence files so link checks and
generated views can be demonstrated.

## Workflow

Run these commands from the repository root.

### 1. Install Tools

```text
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-tools.txt
syseng --help
```

### 2. Check Records

```text
syseng check
```

This proves that StrictDoc can parse the records and that `syseng` can run the
automated record checks.

### 3. Export Documentation

```text
syseng export
```

This generates StrictDoc HTML, JSON, and Excel output under `build/strictdoc/`.
It also generates the `syseng-tools` risk register under `build/syseng/`.

### 4. Inspect The Risk Register

```text
ls build/syseng
```

Expected generated files:

```text
risk-register.csv
risk-register.json
risk-register.md
```

Open `build/syseng/risk-register.md` to inspect generated risk output when risk
records are present.

### 5. Preview The StrictDoc Site

```text
syseng serve
```

Open the printed local URL to inspect the generated StrictDoc HTML site.

## What To Look For

- Mission records and requirements render as separate StrictDoc pages.
- Requirement relations link requirements to parent mission records.
- Risk records can be added once candidate risks are ready for review.
- Generated output lives under `build/` and is not source data.
