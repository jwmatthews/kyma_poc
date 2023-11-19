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
    
        
