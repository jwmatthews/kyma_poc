# Quarkus Notes
* Random notes/links/tips to help share Quarkus related info with team

## Quarkus
* https://quarkus.io/
* Installing Quarkus via https://sdkman.io/
### Background
* https://developers.redhat.com/blog/2020/09/11/quarkus-and-jakarta-ee-together-or-not
* https://kubebyexample.com/learning-paths/developing-quarkus-kubernetes/getting-started-quarkus/introduction
### CDI
* https://quarkus.io/guides/cdi
* https://jakarta.ee/specifications/cdi/4.0/jakarta-cdi-spec-4.0.html#introduction
* EJB related
    * https://www.oracle.com/technical-resources/articles/java/cdi-javaee-bien.html

### Reactive principles
* https://quarkus.io/guides/getting-started-reactive
* https://developers.redhat.com/coderland/reactive/reactive-intro
#### Vert.x
https://vertx.io/get-started/
### Messaging
* [Messaging with Quarkus – part one: JMS Messaging](https://www.mastertheboss.com/soa-cloud/quarkus/messaging-with-quarkus-part-one/)
* [Messaging with Quarkus – part two: Reactive Messaging](https://www.mastertheboss.com/soa-cloud/quarkus/messaging-with-quarkus-part-two-reactive-messaging/)
* [Getting Started with Java Message Service (JMS)](https://www.oracle.com/technical-resources/articles/java/intro-java-message-service.html)

### Workshops
* https://github.com/RedHat-Middleware-Workshops/quarkus-workshop-m1m2/tree/ocp-4.14

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


