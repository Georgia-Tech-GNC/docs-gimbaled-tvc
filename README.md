# Gimbaled TVC Documentation Demo

This repository currently contains a thin demonstration of the StrictDoc and
`syseng` workflow for the Gimbaled TVC rocket documentation repository.

The mission records, requirements, risks, and evidence files in this demo are
not an approved TVC baseline. They exist to prove the documentation tooling
workflow before the real L0 mission objectives, constraints, requirements, and
risks are authored.

## Demo Contents

```text
requirements-tools.txt
syseng.toml
records/
  mission.sdoc
  requirements.sdoc
  risks.sdoc
docs/
  verification/
    actuator-frequency-response-test.md
    attitude-estimate-analysis.md
```

`requirements-tools.txt` pins the `syseng-tools` release used by this
repository.

`syseng.toml` configures the project title, UID prefix, records directory, and
allowed applicability values.

`records/` contains demo StrictDoc source records.

`docs/verification/` contains placeholder evidence files so link checks and
generated views can be demonstrated.

## Demo Flow

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

Open `build/syseng/risk-register.md` to confirm that `syseng` calculated risk
scores and generated a readable risk statement from the risk condition and
consequence.

### 5. Preview The StrictDoc Site

```text
syseng serve
```

Open the printed local URL to inspect the generated StrictDoc HTML site.

## What To Look For

- Mission records, requirements, and risks render as separate StrictDoc pages.
- Requirement relations link requirements to parent mission records.
- Risk relations link risks to affected requirements.
- Risk condition and consequence render as the large risk claim fields.
- The generated risk register calculates initial and current risk levels.
- Generated output lives under `build/` and is not source data.
