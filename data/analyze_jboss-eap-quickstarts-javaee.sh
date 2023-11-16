SOURCE_DIR=jboss-eap-quickstarts-javaee
OUTDIR=$PWD/example_reports/$SOURCE_DIR
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t "quarkus" -t "jakarta-ee" -t "jakarta-ee8+" -t "jakarta-ee9+" -t "cloud-readiness" -o $OUTDIR  --overwrite

