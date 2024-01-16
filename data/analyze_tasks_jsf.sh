SOURCE_DIR=jboss-eap-quickstarts-javaee/tasks-jsf
OUTDIR=$PWD/example_reports/tasks-jsf
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t "quarkus" -t "jakarta-ee" -t "jakarta-ee8+" -t "jakarta-ee9+" -t "cloud-readiness" -o $OUTDIR  --overwrite

