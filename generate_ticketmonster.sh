#!/bin/bash

#./kyma.py generate ./data/example_reports/ticket-monster/output.yaml \
#    ./data/ticket-monster master quarkus \
#    ./example_output/ticket-monster \
#    -m 'gpt-3.5-turbo-16k' \
#    -r 'quarkus/springboot' \
#    -v 'cdi-to-quarkus-00040' -v 'cdi-to-quarkus-00050'

./kyma.py generate ./data/example_reports/ticket-monster/output.yaml \
    ./data/ticket-monster master quarkus \
    ./example_output/ticket-monster \
    -m 'gpt-4-1106-preview' \
    -r 'quarkus/springboot' \
    -v 'cdi-to-quarkus-00050'

#####
# To run against all violations
#####
#./kyma.py generate ./data/example_reports/ticket-monster/output.yaml \
#    ./data/ticket-monster master quarkus \
#    ./example_output/ticket-monster \
#    -m 'gpt-3.5-turbo-16k'  

## Models
# gpt-3.5-turbo-16k
# gpt-4-1106-preview
