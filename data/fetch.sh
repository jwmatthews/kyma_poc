
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

### KitchenSink
##### https://github.com/konveyor/example-applications/issues/19
########## https://github.com/jboss-developer/jboss-eap-quickstarts/tree/7.4.x/kitchensink
git clone https://github.com/jboss-developer/jboss-eap-quickstarts.git jboss-eap-quickstarts-javaee

########## https://github.com/tqvarnst/jboss-eap-quickstarts/tree/quarkus-3.2/kitchensink
## https://github.com/tqvarnst/jboss-eap-quickstarts/tree/quarkus-3.2
git clone https://github.com/tqvarnst/jboss-eap-quickstarts.git jboss-eap-quickstarts-quarkus

# Ticket Monster
# 'master' is original Java EE
# 'quarkus' is quarkus migration
git clone https://github.com/jmle/monolith.git ticket-monster

# HelloWorld MDB
#  This started from: https://github.com/jboss-developer/jboss-eap-quickstarts/tree/7.4.x/helloworld-mdb/src/main/java/org/jboss/as/quickstarts/mdb
git clone https://github.com/savitharaghunathan/helloworld-mdb.git

### Spring to Quarkus
#  Spring Music isn't able to be analyzed by Kantra as of today
#  See: https://github.com/konveyor/kantra/issues/116
#
#git clone https://github.com/anurag-saran/spring-music.git spring-music-quarkus
#git clone https://github.com/cloudfoundry-samples/spring-music.git spring-music-original

popd

