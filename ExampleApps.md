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

    

            
