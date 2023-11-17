# kyma_poc

Kyma (greek for Wave, https://www.howtopronounce.com/kyma) is a proof of concept demonstration using Generative AI inside of Konveyor.io to help with code modernization efforts.

Slides: [Konveyor KymaML: GenAI Code Migration](https://docs.google.com/presentation/d/1_HNyHyiM12CF0MOSMOhSp12_9ghUh5tDSFTHLnqN1tE/edit#slide=id.g28c0e0d2936_0_621)

## Overview
* Kyma is focused on leveraging data that Konveyor already collects via [Migration Waves](https://github.com/konveyor/enhancements/tree/master/enhancements/migration-waves) and it's view of an organizations Application Portfolio.
* Kyma will look at a given application's analysis report and will generate potential patches for each incident.
    * This is done by looking at similar incidents that were solved in other applications and grabbing the code diff that fixed that incident and working with a LLM to leverage how the organization solved the problem in the past for this specific application and incident.
        * For the POC this will involve looking at applications that have both javaee and quarkus solutions, we will simulate what the experience would be like in Konveyor where we have access to a larger application portfolio and can find similar applications which were already migrated and use them as examples.
* The approach leverages prompt engineering with Few Shots examples and a series of agents to work with the LLM to improve the generated patch.
    * Note:  Model Training and Fine Tuning is not required in this phase.  We have plans for fine-tuning in conjuction with [Open Data Hub](https://opendatahub.io/) in the future, leveraging open source foundation models from [huggingface.co](https://huggingface.co/), yet that is out scope for this current phase.
* We are assuming that Kyma will work with various models, our focus is on the tooling/prompt engineering and expect to treat the model coordinates as an interchangeable entity.  This is to allow us to experiment with evolving models.

## What is our criteria for success of Proof of Concept
* We want to assess what level of quality can we get from prompt engineering, i.e. no fine-tuning.
    * Future phases may leverage fine-tuning, but this phase is about a simpler approach of building tooling to collect useful data in Konveyor and use prompt-engineering to help Migrators with code changes
* This POC is intended to be a small python project to work with a few sample applications and analysis reports to gauage the usefulness of generated patches in the domain of modernizing Java EE applications to Quarkus
* Success for us is being able to generate patches that save time from the Migrator working on modernizing an application.  
    * We assume the patches will not be 100% functional all the time and will involve some user intervention.  Success will be related to how much intervention is required and if the patches yield enough help to save time.

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
    * Follow that example to analyze other sample applications

### Generate a Markdown version of a given analysis report
1. Start in the project root and execute
    * `./kyma.py report data/example_reports/coolstuff-javaee/output.yaml ./data/markdown_reports  `
        * This is assuming that a Kantra analyis report in YAML exists at [data/example_reports/coolstuff-javaee/output.yaml](data/example_reports/coolstuff-javaee/output.yaml)
        * Sample output run:

                We have results from 4 RuleSet(s) in data/example_reports/coolstuff-javaee/output.yaml

                Writing eap7/websphere to ./data/markdown_reports/eap7_websphere.md
                Writing eap8/eap7 to ./data/markdown_reports/eap8_eap7.md
                Writing openshift to ./data/markdown_reports/openshift.md
                Writing quarkus/springboot to ./data/markdown_reports/quarkus_springboot.md
                ./kyma.py report data/example_reports/coolstuff-javaee/output.yaml   0.33s user 0.02s system 93% cpu 0.376 total
        * Example outputs can be viewed from github for [data/example_reports/coolstuff-javaee/output.yaml](data/example_reports/coolstuff-javaee/output.yaml)
            * [data/markdown_reports/eap7_websphere.md](data/markdown_reports/eap7_websphere.md)
            * [data/markdown_reports/eap8_eap7.md](data/markdown_reports/eap8_eap7.md)
            * [data/markdown_reports/openshift.md](data/markdown_reports/openshift.md)
            * [data/markdown_reports/quarkus_springboot.md](data/markdown_reports/quarkus_springboot.md)

### Generate result from LLM interaction
1. `export OPENAI_API_KEY="mysecretkey"`
    * See https://platform.openai.com/api-keys to create an API Key
2.  `./generate_coolstuff.sh`
    * See [generate_coolstuff.sh](generate_coolstuff.sh) as an example of how to invoke