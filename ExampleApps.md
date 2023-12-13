# What Examples do we have?
* For the below examples we have branches with 'Java EE' and 'Quarkus', so we can tell the differences required to migrate from Java EE to Quarkus
* We have a script at [data/fetch.sh](data/fetch.sh) which will fetch the sample apps we know about
## From JBoss EAP QuickStarts
### KitchenSink
* https://github.com/tqvarnst/jboss-eap-quickstarts/tree/quarkus-3.2/kitchensink
### HelloWorld MDB
* This example started from JBoss EAP Quickstarts: https://github.com/jboss-developer/jboss-eap-quickstarts/tree/7.4.x/helloworld-mdb/src/main/java/org/jboss/as/quickstarts/mdb
* Our team then ported 'HelloWorld MDB' to Quarkus:https://github.com/savitharaghunathan/helloworld-mdb/tree/quarkus
    * Note these blog posts from prior work of modernizing this same HelloWorld app, the difference with our latest work and the below is the change our team did to also address JMS to Reactive changes:
        * https://developers.redhat.com/blog/2019/11/07/quarkus-modernize-helloworld-jboss-eap-quickstart-part-1#let_s_modernize_helloworld
        * https://developers.redhat.com/blog/2019/11/08/quarkus-modernize-helloworld-jboss-eap-quickstart-part-2
    * We also created some new rules for JMS to Reactive here:
        * https://github.com/windup/windup-rulesets/pull/1043
    * https://github.com/jmle/rulesets/blob/jms-rule/default/generated/quarkus/05-jms-to-reactive-quarkus.windup.yaml

## CoolStuff Store
*  https://github.com/mathianasj/eap-coolstore-monolith.git
## TicketMonster
* https://github.com/jmle/monolith.git

# General
## EJBs -> CDI
A general pattern with moving away from an EJB and embracing CDI is to:
1. Replace @Stateless and @Remote with @ApplicationScoped from CDI.
2. Add @Transactional to manage transactions declaratively from JTA (if needed).
3. Remove the remote interface, as CDI doesn't require separate interfaces for bean implementation.
### Background reading
* https://quarkus.io/guides/cdi

## Servlets
* Quarkus has a compatibility module `quarkus-undertow` which allows using Servlets and JSPs

# CoolStuff Store
## What was changed from EAP to Quarkus?
* javax -> jakarata
* java.util.logging.Logger -> org.jboss.logging.Logger
* rest
    * CartEndpoint.java
        * SessionScoped -> RequestScoped
        * JMSDestinationDefinitions removed 
    * User.java was introduced (didn't exist on EAP side)
* service
    * CatalogService
        * Stateless -> ApplicationScoped
    * InventoryNotificationMDB
        * Looks like several JMS related changes
        * Removed implements MessageListener
    * OrderService
        * Stateless -> ApplicationScoped 
    * OrderServiceMDB
        * Perhaps similar pattern to InventoryNotificationMDB
    * ProductService
        * Stateless -> ApplicationScoped 
    * PromoService
        * javax -> jakarata
    * ShippingService
        * Stateless -> RequestScoped 
            * NEED to identify difference of when to go to ApplicationScoped vs RequestScoped
    * ShoppingCarOrderProcessor
        * java.util.logging.Logger -> org.jboss.logging.Logger 
        * JMS to Reactive messaging (org.eclipse.microprofile.reactive.messaging)
        * Stateless -> RequestScoped 
    * ShoppingCartService
        * javax -> jakarata 
        * Stateful -> SessionScoped
        * java.util.logging.Logger -> org.jboss.logging.Logger
* utils
    * Transformers
        * javax -> jakarata  
    * (Deleted) - Don't know why these were deleted going to Quarkus
        * DataBaseMigrationStartup
        * Producers
        * StartupListeners
* resources
    * META-INF
        * DELETED: persistence.xml
* webapp
    * DELETED: keycloak.json
* pom.xml
    * Removed: <packaging>war</packaging>
    * Various updates to move to Quarkus and remove Java EE specifics

# Helloworld-mdb App
source code: https://github.com/savitharaghunathan/helloworld-mdb/compare/main...quarkus
## What was changed from EAP to Quarkus?
* javax -> jakarata
* java.util.logging.Logger -> org.jboss.logging.Logger
* mdb
     * HelloWorldQueueMDB.java
          * javax -> jakarta
          * java logging -> jboss logging
          * javax jms changes -> eclipse microprofile smallrye changes
          * removed mdb config
          * Added @ApplicationScoped annotation
     * HelloWorldTopicMDB.java
          * same as above

* servlet
     * HelloWorldMDBServletClient.java
          * javax -> jakarta import changes
          * webservlet annotation -> path
          * removed jms destination config
          * replaced @Resource(lookup = "java:/queue/HELLOWORLDMDBQueue") -> Incoming and Channel annotation with the queue name
          * refactored doGet function
               * logic change for obtaining the url paramater
               * rewrote templating using string builder
               * Added a function that generates messages, prints them on console, sends them to the queue/topic
         * removed doPost func (I wasnt sure if it did anything and removing it, did not alter the application behavior)
* Moved index.html to /src/main/resources/META-INF
* application.properties
     * Added config for AMQP
* pom.xml
    * Removed <packaging>war</packaging>
    * JMS dependency changes
    * java ee -> quarkus lib changes

    

            
