WINDUP_HOME="/Users/jmatthews/RedHat/MTA/6.2.0/bin"
SOURCE_DIR="jboss-eap-quickstarts-javaee"
time ${WINDUP_HOME}/windup-cli --input $SOURCE_DIR --target jakarta-ee quarkus quarkus3 cloud-readiness --output ./out.windup --overwrite


