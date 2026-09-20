# AI-Assisted Git Workflow and Python Data Parsing

Student name: Deanna Juliana K. de la Cruz 
Section: TS31

## Project purpose

This repository demonstrates how Git version control can be used to develop, review, and merge a Python data-parsing project. The parser reads XML, JSON, and YAML configuration files and produces structured summaries that are checked with automated unit tests.

## How to run

```bash
python3 parser_template.py
python3 -m unittest -v
```

## Git workflow summary


### Branches
  - main (Main branch that has the initial files and is then merged with the other branches to produce the final output of the project.)
  - feature/parsing (Branch where the parsing implementation has been created)
  - docs/ai-note (branch that was used for documentation)

### Major commits
  - 82fd492 feat: implemented parsing for each file --> This is the commit when the parsing functions are completed as well as the build_Summary
  - 5bd4d90 (origin/docs/ai-note, docs/ai-note) Validation status: AI Reviewed --> Logs were input 
  - 9b6a15a Validation status: passed --> logs of the program working is tagged
  - 062d786 (origin/feature/parsing, feature/parsing) Fix: corrected file paths --> there was a self-inflicted bug by me and I corrected it 
  - e07ffe5 merge conflict: resolved --> resolved merge conflicts between docs and main
  - 4a72e42 (HEAD -> main, origin/main) implemented: data parser | logged: readme and ai usage | exported validations --> the final commit, commit message is explanatory


## Parser results

{
  "xml": {
    "default_operation": "merge",
    "test_option": "test-then-set"
  },
  "json": {
    "site": "FEU-Tech-Lab",
    "device_count": 3,
    "enabled_devices": [
      "R1",
      "SW1"
    ],
    "roles": [
      "router",
      "switch",
      "wireless-ap"
    ]
  },
  "yaml": {
    "name": "Saturday-Lab",
    "approved": true,
    "duration_minutes": 90,
    "devices": [
      "R1",
      "SW1"
    ],
    "action": "validate-configuration"
  }
}


## AI disclosure

I used ChatGPT to help understand the parsing requirements, review the Python implementation, and clarify the unit tests. I reviewed the generated suggestions and verified the code with the supplied tests.
## Safety statement

Only the provided fictional XML, JSON, and YAML data was used in this project. No credentials, tokens, private repository data, or personal information were submitted to the AI tool.
