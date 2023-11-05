SOURCE_DIR=coolstuff-javaee
OUTDIR=$PWD/example_reports/${SOURCE_DIR}
mkdir -p $OUTDIR
time ./kantra analyze -i $PWD/$SOURCE_DIR -t "quarkus" -o $OUTDIR

