
pushd .
### Java EE to Quarkus examples
#### Starting point
git clone https://github.com/deewhyweb/eap-coolstore-monolith.git coolstuff-javaee
#### Migrated example for Quarkus
git clone https://github.com/mathianasj/eap-coolstore-monolith.git coolstuff-quarkus
cd coolstuff-quarkus
git checkout quarkus-migration
cd ..

### Simpler example app
git clone https://github.com/konveyor/example-applications.git konveyor-examples


### Spring to Quarkus
#  Spring Music isn't able to be analyzed by Kantra as of today
#  See: https://github.com/konveyor/kantra/issues/116
#
#git clone https://github.com/anurag-saran/spring-music.git spring-music-quarkus
#git clone https://github.com/cloudfoundry-samples/spring-music.git spring-music-original

popd

