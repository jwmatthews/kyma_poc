# quarkus/springboot
## Description
This ruleset gives hints to migrate from Spring Scheduled to Quarkus spring-scheduled extension
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated/quarkus
* Sample application: https://github.com/deewhyweb/eap-coolstore-monolith
## Violations
Number of Violations: 13
### #0 - cdi-to-quarkus-00030
* Category: potential
* Effort: 3
* Description: `beans.xml` descriptor content is ignored
`beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Incidents
  * file:///opt/input/source/src/main/webapp/WEB-INF/beans.xml
      * `beans.xml` descriptor content is ignored and it could be removed from the application.. Refer to the guide referenced below to check the supported CDI feature in Quarkus.
### #1 - cdi-to-quarkus-00040
* Category: potential
* Effort: 1
* Description: Producer annotation no longer required
In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus Simplified Producer Method Declaration: https://quarkus.io/guides/cdi-reference#simplified-producer-method-declaration
* Incidents
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/utils/Producers.java
      * In Quarkus, you can skip the @Produces annotation completely if the producer method is annotated with a scope annotation, a stereotype or a qualifier... This field could be accessed using a `@Named` getter method instead.
      * Code Snippet:
```java
  1  package com.redhat.coolstore.utils;
  2  
  3  import javax.enterprise.inject.Produces;
  4  import javax.enterprise.inject.spi.InjectionPoint;
  5  import java.util.logging.Logger;
  6  
  7  
  8  public class Producers {
  9  
 10      Logger log = Logger.getLogger(Producers.class.getName());
 11  
 12      @Produces
 13      public Logger produceLog(InjectionPoint injectionPoint) {
 14          return Logger.getLogger(injectionPoint.getMember().getDeclaringClass().getName());
 15      }
 16  
 17  }

```
### #2 - cdi-to-quarkus-00050
* Category: potential
* Effort: 1
* Description: Stateless annotation can be replaced with scope
Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus CDI reference: https://quarkus.io/guides/cdi-reference
* Incidents
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/CatalogService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.List;
  4  import java.util.logging.Logger;
  5  
  6  import javax.inject.Inject;
  7  
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  import javax.ejb.Stateless;
 13  import javax.persistence.EntityManager;
 14  import javax.persistence.PersistenceContext;
 15  
 16  import com.redhat.coolstore.model.*;
 17  
 18  @Stateless
 19  public class CatalogService {
 20  
 21      @Inject
 22      Logger log;
 23  
 24      @PersistenceContext
 25      private EntityManager em;
 26  
 27      public CatalogService() {
 28      }
 29  
 30      public List<CatalogItemEntity> getCatalogItems() {
 31          CriteriaBuilder cb = em.getCriteriaBuilder();
 32          CriteriaQuery<CatalogItemEntity> criteria = cb.createQuery(CatalogItemEntity.class);
 33          Root<CatalogItemEntity> member = criteria.from(CatalogItemEntity.class);
 34          criteria.select(member);
 35          return em.createQuery(criteria).getResultList();
 36      }
 37  
 38      public CatalogItemEntity getCatalogItemById(String itemId) {
 39          return em.find(CatalogItemEntity.class, itemId);
 40      }
 41  
 42      public void updateInventoryItems(String itemId, int deducts) {
 43          InventoryEntity inventoryEntity = getCatalogItemById(itemId).getInventory();
 44          int currentQuantity = inventoryEntity.getQuantity();
 45          inventoryEntity.setQuantity(currentQuantity-deducts);
 46          em.merge(inventoryEntity);
 47      }
 48  
 49  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/OrderService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import java.util.List;
  5  import javax.ejb.Stateless;
  6  import javax.persistence.EntityManager;
  7  import javax.persistence.PersistenceContext;
  8  import javax.persistence.criteria.CriteriaBuilder;
  9  import javax.persistence.criteria.CriteriaQuery;
 10  import javax.persistence.criteria.Root;
 11  
 12  @Stateless
 13  public class OrderService {
 14  
 15    @PersistenceContext
 16    private EntityManager em;
 17  
 18    public void save(Order order) {
 19      em.persist(order);
 20    }
 21  
 22    public List<Order> getOrders() {
 23      CriteriaBuilder cb = em.getCriteriaBuilder();
 24      CriteriaQuery<Order> criteria = cb.createQuery(Order.class);
 25      Root<Order> member = criteria.from(Order.class);
 26      criteria.select(member);
 27      return em.createQuery(criteria).getResultList();
 28    }
 29  
 30    public Order getOrderById(long id) {
 31      return em.find(Order.class, id);
 32    }
 33  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ProductService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.CatalogItemEntity;
  4  import com.redhat.coolstore.model.Product;
  5  import com.redhat.coolstore.utils.Transformers;
  6  
  7  import javax.ejb.Stateless;
  8  import javax.inject.Inject;
  9  import java.util.List;
 10  import java.util.stream.Collectors;
 11  
 12  import static com.redhat.coolstore.utils.Transformers.toProduct;
 13  
 14  @Stateless
 15  public class ProductService {
 16  
 17      @Inject
 18      CatalogService cm;
 19  
 20      public ProductService() {
 21      }
 22  
 23      public List<Product> getProducts() {
 24          return cm.getCatalogItems().stream().map(entity -> toProduct(entity)).collect(Collectors.toList());
 25      }
 26  
 27      public Product getProductByItemId(String itemId) {
 28          CatalogItemEntity entity = cm.getCatalogItemById(itemId);
 29          if (entity == null)
 30              return null;
 31  
 32          // Return the entity
 33          return Transformers.toProduct(entity);
 34      }
 35  
 36  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShippingService.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.Stateless;
  4  
  5  import com.redhat.coolstore.model.ShoppingCart;
  6  
  7  @Stateless
  8  public class ShippingService {
  9  
 10      public void calculateShipping(ShoppingCart sc) {
 11  
 12          if (sc != null) {
 13  
 14              if (sc.getCartItemTotal() >= 0 && sc.getCartItemTotal() < 25) {
 15  
 16                  sc.setShippingTotal(2.99);
 17  
 18              } else if (sc.getCartItemTotal() >= 25 && sc.getCartItemTotal() < 50) {
 19  
 20                  sc.setShippingTotal(4.99);
 21  
 22              } else if (sc.getCartItemTotal() >= 50 && sc.getCartItemTotal() < 75) {
 23  
 24                  sc.setShippingTotal(6.99);
 25  
 26              } else if (sc.getCartItemTotal() >= 75 && sc.getCartItemTotal() < 100) {
 27  
 28                  sc.setShippingTotal(8.99);
 29  
 30              } else if (sc.getCartItemTotal() >= 100 && sc.getCartItemTotal() < 10000) {
 31  
 32                  sc.setShippingTotal(10.99);
 33  
 34              }
 35  
 36          }
 37  
 38      }
 39  
 40  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import java.util.logging.Logger;
  4  import javax.ejb.Stateless;
  5  import javax.annotation.Resource;
  6  import javax.inject.Inject;
  7  import javax.jms.JMSContext;
  8  import javax.jms.Topic;
  9  
 10  import com.redhat.coolstore.model.ShoppingCart;
 11  import com.redhat.coolstore.utils.Transformers;
 12  
 13  @Stateless
 14  public class ShoppingCartOrderProcessor  {
 15  
 16      @Inject
 17      Logger log;
 18  
 19  
 20      @Inject
 21      private transient JMSContext context;
 22  
 23      @Resource(lookup = "java:/topic/orders")
 24      private Topic ordersTopic;
 25  
 26      
 27    
 28      public void  process(ShoppingCart cart) {
 29          log.info("Sending order from processor: ");
 30          context.createProducer().send(ordersTopic, Transformers.shoppingCartToJson(cart));
 31      }
 32  
 33  
 34  
 35  }

```
### #3 - javaee-pom-to-quarkus-00000
* Category: mandatory
* Effort: 1
* Description: The expected project artifact's extension is `jar`

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * The project artifact's current extension (i.e. `<packaging>` tag value) is `` but the expected value should be `jar`
### #4 - javaee-pom-to-quarkus-00010
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus BOM

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
  * Quarkus - Releases: https://quarkus.io/blog/tag/release/
* Incidents
  * file:///opt/input/source/pom.xml
      * Use the Quarkus BOM to omit the version of the different Quarkus dependencies.. Add the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <dependencyManagement>. <dependencies>. <dependency>. <groupId>$</groupId>. <artifactId>$</artifactId>. <version>$</version>. <type>pom</type>. <scope>import</scope>. </dependency>. </dependencies>. </dependencyManagement>. ```. Check the latest Quarkus version available from the `Quarkus - Releases` link below.
### #5 - javaee-pom-to-quarkus-00020
* Category: mandatory
* Effort: 1
* Description: Adopt Quarkus Maven plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * Use the Quarkus Maven plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>. <quarkus.platform.version>3.1.0.Final</quarkus.platform.version>. </properties>. <build>. <plugins>. <plugin>. <groupId>$</groupId>. <artifactId>quarkus-maven-plugin</artifactId>. <version>$</version>. <extensions>true</extensions>. <executions>. <execution>. <goals>. <goal>build</goal>. <goal>generate-code</goal>. <goal>generate-code-tests</goal>. </goals>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
### #6 - javaee-pom-to-quarkus-00030
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Compiler plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * Use the Maven Compiler plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <compiler-plugin.version>3.10.1</compiler-plugin.version>. <maven.compiler.release>11</maven.compiler.release>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-compiler-plugin</artifactId>. <version>$</version>. <configuration>. <compilerArgs>. <arg>-parameters</arg>. </compilerArgs>. </configuration>. </plugin>. </plugins>. </build>. ```
### #7 - javaee-pom-to-quarkus-00040
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Surefire plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * Use the Maven Surefire plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-surefire-plugin</artifactId>. <version>$</version>. <configuration>. <systemPropertyVariables>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </plugin>. </plugins>. </build>. ```
### #8 - javaee-pom-to-quarkus-00050
* Category: mandatory
* Effort: 1
* Description: Adopt Maven Failsafe plugin

* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * Use the Maven Failsafe plugin adding the following sections to the `pom.xml` file:. ```xml. <properties>. <surefire-plugin.version>3.0.0</compiler-plugin.version>. </properties>. <build>. <plugins>. <plugin>. <artifactId>maven-failsafe-plugin</artifactId>. <version>$</version>. <executions>. <execution>. <goals>. <goals>integration-test</goal>. <goals>verify</goal>. </goals>. <configuration>. <systemPropertyVariables>. <native.image.path>$/$-runner</native.image.path>. <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>. <maven.home>$</maven.home>. </systemPropertyVariables>. </configuration>. </execution>. </executions>. </plugin>. </plugins>. </build>. ```
### #9 - javaee-pom-to-quarkus-00060
* Category: mandatory
* Effort: 1
* Description: Add Maven profile to run the Quarkus native build
Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/maven-tooling#build-tool-maven
* Incidents
  * file:///opt/input/source/pom.xml
      * Leverage a Maven profile to run the Quarkus native build adding the following section to the `pom.xml` file:. ```xml. <profiles>. <profile>. <id>native</id>. <activation>. <property>. <name>native</name>. </property>. </activation>. <properties>. <skipITs>false</skipITs>. <quarkus.package.type>native</quarkus.package.type>. </properties>. </profile>. </profiles>. ```
### #10 - jaxrs-to-quarkus-00020
* Category: optional
* Effort: 1
* Description: JAX-RS activation is no longer necessary
JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/resteasy-reactive#declaring-endpoints-uri-mapping
* Incidents
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/RestApplication.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  
  7  @ApplicationPath("/services")
  8  public class RestApplication extends Application {
  9  
 10  }

```
  * file:///opt/input/source/src/main/java/com/redhat/coolstore/rest/RestApplication.java
      * JAX-RS activation is no longer necessary. You can set a root path like this but you don't have to.
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import javax.ws.rs.ApplicationPath;
  4  import javax.ws.rs.core.Application;
  5  
  6  
  7  @ApplicationPath("/services")
  8  public class RestApplication extends Application {
  9  
 10  }

```
### #11 - quarkus-flyway-00000
* Category: mandatory
* Effort: 1
* Description: Replace the 'flyway-core' dependency with Quarkus 'quarkus-flyway' extension
Replace the `org.flywaydb:flyway-core` dependency with the Quarkus dependency `io.quarkus:quarkus-flyway`. Further information in the link below.
* Labels: konveyor.io/source=flyway, konveyor.io/target=quarkus
* Incidents
  * file:///opt/input/source/pom.xml
      * Replace the `org.flywaydb:flyway-core` dependency with the Quarkus dependency `io.quarkus:quarkus-flyway`. Further information in the link below.
### #12 - quarkus-flyway-00010
* Category: mandatory
* Effort: 1
* Description: Replace the 'flyway-core' dependency with Quarkus 'quarkus-flyway' extension
Replace the `org.flywaydb:flyway-core` dependency with the Quarkus dependency `io.quarkus:quarkus-flyway`. Further information in the link below.
* Labels: konveyor.io/source=flyway, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides/flyway
* Incidents
  * file:///opt/input/source/pom.xml
      * Replace the `org.flywaydb:flyway-core` dependency with the Quarkus dependency `io.quarkus:quarkus-flyway`. Further information in the link below.
