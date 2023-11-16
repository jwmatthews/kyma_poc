# kyma_poc

KymaML (greek for Wave, https://www.howtopronounce.com/kyma) is a proof of concept demonstration using Generative AI inside of Konveyor.io to help with code modernization efforts.

## Overview
* KymaML is focused on leveraging data that Konveyor already collects via [Migration Waves](https://github.com/konveyor/enhancements/tree/master/enhancements/migration-waves) and it's view of an organizations Application Portfolio.
* KymaML will look at a given application's analysis report and will generate potential patches for each incident.
    * This is done by looking at similar incidents that were solved in other applications and grabbing the code diff that fixed that incident and working with a LLM to leverage how the organization solved the problem in the past for this specific application and incident.
* The approach leverages prompt engineering with Few Shots examples and a series of agents to work with the LLM to improve the generated patch.
* Note:  Model Training and Fine Tuning is not required in this phase.  We have plans for fine-tuning in conjuction with [Open Data Hub](https://opendatahub.io/) in the future, leveraging open source foundation models from [huggingface.co](https://huggingface.co/), yet that is out scope for this current phase.

## Setup
1. `python -m venv env`
2. `source env/bin/activate`
3. `pip install -r ./requirements.txt`
4. Install [podman](https://podman.io/) so you can run [Kantra](https://github.com/konveyor/kantra) for static code analysis

## Running
### Run an analysis of a sample app (example for MacOS)
1. `cd data`
2. `./fetch.sh` # this will git clone some sample source code apps
3. `./darwin_restart_podman_machine.sh` # setups the podman VM on MacOS so it will mount the host filesystem into the VM
4. `./darwin_get_latest_kantra_cli.sh` # fetches 'kantra' our analyzer tool
5. `./analyzer_coolstuff.sh` # Analyzes 'coolstuff-javaee' directory and writes an analysis output to [example_reports/coolstuff-javaee/output.yaml](/data/example_reports/coolstuff-javaee/output.yaml)

### Generate a Markdown version of a given analysis report


$ time ./kyma.py report data/example_reports/kitchensink/output.yaml ./testjwm
We have results from 3 RuleSet(s) in data/example_reports/kitchensink/output.yaml