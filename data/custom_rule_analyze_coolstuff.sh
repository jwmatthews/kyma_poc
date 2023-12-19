SOURCE_DIR=coolstuff-javaee
OUTDIR=$PWD/example_reports/${SOURCE_DIR}_custom_rules
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t 'quarkus' -t 'jakarta-ee' -t 'jakarta-ee8+' -t 'jakarta-ee9+' -t 'cloud-readiness' --rules ./custom_rules/05-jms-to-reactive-quarkus.windup.yaml -o $OUTDIR --overwrite
