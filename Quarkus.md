# Quarkus Notes
* Random notes/links/tips to help share Quarkus related info with team

## Quarkus
* https://quarkus.io/
* Installing Quarkus via https://sdkman.io/

### Java EE to Quarkus Modernization
#### Blogs
* https://developers.redhat.com/blog/2019/11/07/quarkus-modernize-helloworld-jboss-eap-quickstart-part-1?source=sso

## JDK
* Installing JDK via https://sdkman.io/
* Quarkus needs to build with minimal of JDK 11

## MicroProfile
* https://microprofile.io/


## JMS
* Quarkus doesn't have a MDB (Message Driven Bean) message consumption can be simulated using a CDI Bean. Below example shows a JMSConsumer Bean scheduling an event every 5 seconds that will check for incoming messages in the JMS Queue:
    * https://www.mastertheboss.com/soa-cloud/quarkus/messaging-with-quarkus-part-one/