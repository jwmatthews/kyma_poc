SOURCE_DIR=helloworld-mdb
OUTDIR=$PWD/example_reports/${SOURCE_DIR}_custom_rules
#TARGETS="-t 'quarkus' -t 'jakarta-ee' -t 'jakarta-ee8+' -t 'jakarta-ee9+' -t 'cloud-readiness'"
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR --rules ./custom_rules -o $OUTDIR --overwrite
