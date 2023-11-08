SOURCE_DIR=coolstuff-javaee
OUTDIR=$PWD/example_reports/${SOURCE_DIR}
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t "quarkus" -t "jakarta-ee" -t "cloud-readiness" -o $OUTDIR

