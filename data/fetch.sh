
pushd .
# Starting point
git clone https://github.com/deewhyweb/eap-coolstore-monolith.git coolstuff-javaee
# Migrated example for Quarkus
git clone https://github.com/mathianasj/eap-coolstore-monolith.git coolstuff-quarkus
cd coolstuff-quarkus
git checkout quarkus-migration
popd

