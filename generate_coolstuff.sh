#!/bin/bash

./kyma.py generate ./data/example_reports/coolstuff-javaee/output.yaml \
    ./data/coolstuff-quarkus main quarkus-migration \
    ./example_output/coolstuff-quarkus -r 'quarkus/springboot' \
    -v 'cdi-to-quarkus-00040' -v 'cdi-to-quarkus-00050'

