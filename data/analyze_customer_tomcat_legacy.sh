SOURCE_DIR=konveyor-examples/example-1
OUTDIR=$PWD/example_reports/${SOURCE_DIR}
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t "jakarta-ee" -t "cloud-readiness" -o $OUTDIR

