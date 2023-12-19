# ruleset
## Description
temp ruleset
* Source of rules: https://github.com/konveyor/rulesets/tree/main/default/generated
## Violations
Number of Violations: 4
### #0 - jms-to-reactive-quarkus-00010
* Category: mandatory
* Effort: 1
* Description: @MessageDriven - EJBs are not supported in Quarkus
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides
* Incidents
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 15
      * Message: 'Enterprise Java Beans (EJBs) are not supported in Quarkus. CDI must be used.
 Please replace the `@MessageDriven` annotation with a CDI scope annotation like `@ApplicationScoped`.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
### #1 - jms-to-reactive-quarkus-00020
* Category: mandatory
* Effort: 1
* Description: Configure message listener method with @Incoming
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides
* Incidents
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 16
      * Message: 'The `destinationLookup` property can be migrated by annotating a message handler method (potentially `onMessage`) with the
 `org.eclipse.microprofile.reactive.messaging.Incoming` annotation, indicating the name of the queue as a value:
 
 Before:
 ```
 @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = 
 public class MessageListenerImpl implements MessageListener 
 }}
 ```
 
 After:
 ```
 public class MessageListenerImpl implements MessageListener 
 }}
 ```'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 17
      * Message: 'The `destinationLookup` property can be migrated by annotating a message handler method (potentially `onMessage`) with the
 `org.eclipse.microprofile.reactive.messaging.Incoming` annotation, indicating the name of the queue as a value:
 
 Before:
 ```
 @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = 
 public class MessageListenerImpl implements MessageListener 
 }}
 ```
 
 After:
 ```
 public class MessageListenerImpl implements MessageListener 
 }}
 ```'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 18
      * Message: 'The `destinationLookup` property can be migrated by annotating a message handler method (potentially `onMessage`) with the
 `org.eclipse.microprofile.reactive.messaging.Incoming` annotation, indicating the name of the queue as a value:
 
 Before:
 ```
 @MessageDriven(name = "HelloWorldQueueMDB", activationConfig = 
 public class MessageListenerImpl implements MessageListener 
 }}
 ```
 
 After:
 ```
 public class MessageListenerImpl implements MessageListener 
 }}
 ```'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
### #2 - jms-to-reactive-quarkus-00030-01
* Category: mandatory
* Effort: 1
* Description: javax.jms.Topic must be replaced with an Emitter
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Emitter (Microprofile Reactive Streams Messaging): https://smallrye.io/smallrye-reactive-messaging/2.0.2/apidocs/org/eclipse/microprofile/reactive/messaging/Emitter.html
  * Quarkus - Guide: https://quarkus.io/guides
* Incidents
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/InventoryNotificationMDB.java
      * Line Number: 64
      * Message: 'JMS `Topic`s should be replaced with Micrometer `Emitter`s feeding a Channel. See the following example of migrating
 a Topic to an Emitter:
 
 Before:
 ```
 @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 private Topic topic;
 ```
 
 After:
 ```
 @Inject
 @Channel("HELLOWORLDMDBTopic")
 Emitter<String> topicEmitter;
 ```'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import com.redhat.coolstore.utils.Transformers;
  5  
  6  import javax.inject.Inject;
  7  import javax.jms.*;
  8  import javax.naming.Context;
  9  import javax.naming.InitialContext;
 10  import javax.naming.NamingException;
 11  import javax.rmi.PortableRemoteObject;
 12  import java.util.Hashtable;
 13  import java.util.logging.Logger;
 14  
 15  public class InventoryNotificationMDB implements MessageListener {
 16  
 17      private static final int LOW_THRESHOLD = 50;
 18  
 19      @Inject
 20      private CatalogService catalogService;
 21  
 22      @Inject
 23      private Logger log;
 24  
 25      private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
 26      private final static String JMS_FACTORY = "TCF";
 27      private final static String TOPIC = "topic/orders";
 28      private TopicConnection tcon;
 29      private TopicSession tsession;
 30      private TopicSubscriber tsubscriber;
 31  
 32      public void onMessage(Message rcvMessage) {
 33          TextMessage msg;
 34          {
 35              try {
 36                  System.out.println("received message inventory");
 37                  if (rcvMessage instanceof TextMessage) {
 38                      msg = (TextMessage) rcvMessage;
 39                      String orderStr = msg.getBody(String.class);
 40                      Order order = Transformers.jsonToOrder(orderStr);
 41                      order.getItemList().forEach(orderItem -> {
 42                          int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
 43                          int new_quantity = old_quantity - orderItem.getQuantity();
 44                          if (new_quantity < LOW_THRESHOLD) {
 45                              System.out.println("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
 46                          } else {
 47                              orderItem.setQuantity(new_quantity);
 48                          }
 49                      });
 50                  }
 51  
 52  
 53              } catch (JMSException jmse) {
 54                  System.err.println("An exception occurred: " + jmse.getMessage());
 55              }
 56          }
 57      }
 58  
 59      public void init() throws NamingException, JMSException {
 60          Context ctx = getInitialContext();
 61          TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
 62          tcon = tconFactory.createTopicConnection();
 63          tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
 64          Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
 65          tsubscriber = tsession.createSubscriber(topic);
 66          tsubscriber.setMessageListener(this);
 67          tcon.start();
 68      }
 69  
 70      public void close() throws JMSException {
 71          tsubscriber.close();
 72          tsession.close();
 73          tcon.close();
 74      }
 75  
 76      private static InitialContext getInitialContext() throws NamingException {
 77          Hashtable<String, String> env = new Hashtable<>();
 78          env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
 79          env.put(Context.PROVIDER_URL, "t3://localhost:7001");
 80          env.put("weblogic.jndi.createIntermediateContexts", "true");
 81          return new InitialContext(env);
 82      }
 83  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Line Number: 8
      * Message: 'JMS `Topic`s should be replaced with Micrometer `Emitter`s feeding a Channel. See the following example of migrating
 a Topic to an Emitter:
 
 Before:
 ```
 @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 private Topic topic;
 ```
 
 After:
 ```
 @Inject
 @Channel("HELLOWORLDMDBTopic")
 Emitter<String> topicEmitter;
 ```'
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
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Line Number: 24
      * Message: 'JMS `Topic`s should be replaced with Micrometer `Emitter`s feeding a Channel. See the following example of migrating
 a Topic to an Emitter:
 
 Before:
 ```
 @Resource(lookup = "java:/topic/HELLOWORLDMDBTopic")
 private Topic topic;
 ```
 
 After:
 ```
 @Inject
 @Channel("HELLOWORLDMDBTopic")
 Emitter<String> topicEmitter;
 ```'
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
### #3 - jms-to-reactive-quarkus-00050
* Category: mandatory
* Effort: 1
* Description: JMS is not supported in Quarkus
* Labels: konveyor.io/source=java-ee, konveyor.io/target=quarkus
* Links
  * Quarkus - Guide: https://quarkus.io/guides
* Incidents
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Line Number: 11
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/rest/CartEndpoint.java
      * Line Number: 12
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.rest;
  2  
  3  import java.io.Serializable;
  4  import java.util.ArrayList;
  5  import java.util.HashMap;
  6  import java.util.List;
  7  import java.util.Map;
  8  
  9  import javax.enterprise.context.SessionScoped;
 10  import javax.inject.Inject;
 11  import javax.jms.JMSDestinationDefinition;
 12  import javax.jms.JMSDestinationDefinitions;
 13  import javax.ws.rs.DELETE;
 14  import javax.ws.rs.GET;
 15  import javax.ws.rs.POST;
 16  import javax.ws.rs.Path;
 17  import javax.ws.rs.PathParam;
 18  import javax.ws.rs.Produces;
 19  import javax.ws.rs.core.MediaType;
 20  
 21  import com.redhat.coolstore.model.Product;
 22  import com.redhat.coolstore.model.ShoppingCart;
 23  import com.redhat.coolstore.model.ShoppingCartItem;
 24  import com.redhat.coolstore.service.ShoppingCartService;
 25  
 26  @SessionScoped
 27  @Path("/cart")
 28  @JMSDestinationDefinitions(
 29  	value = {
 30  		@JMSDestinationDefinition(
 31  			name = "java:/jms/queue/orders",
 32  			interfaceName = "javax.jms.Queue",
 33  			destinationName = "ordersQueue"
 34  		)
 35  	}
 36  )
 37  public class CartEndpoint implements Serializable {
 38  
 39  	private static final long serialVersionUID = -7227732980791688773L;
 40  
 41  	@Inject
 42  	private ShoppingCartService shoppingCartService;
 43  
 44  	@GET
 45  	@Path("/{cartId}")
 46  	@Produces(MediaType.APPLICATION_JSON)
 47  	public ShoppingCart getCart(@PathParam("cartId") String cartId) {
 48  		return shoppingCartService.getShoppingCart(cartId);
 49  	}
 50  
 51  	@POST
 52  	@Path("/checkout/{cartId}")
 53  	@Produces(MediaType.APPLICATION_JSON)
 54  	public ShoppingCart checkout(@PathParam("cartId") String cartId) {
 55  		return shoppingCartService.checkOutShoppingCart(cartId);
 56  	}
 57  
 58  	@POST
 59  	@Path("/{cartId}/{itemId}/{quantity}")
 60  	@Produces(MediaType.APPLICATION_JSON)
 61  	public ShoppingCart add(@PathParam("cartId") String cartId,
 62  							@PathParam("itemId") String itemId,
 63  							@PathParam("quantity") int quantity) throws Exception {
 64  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 65  
 66  		Product product = shoppingCartService.getProduct(itemId);
 67  
 68  		ShoppingCartItem sci = new ShoppingCartItem();
 69  		sci.setProduct(product);
 70  		sci.setQuantity(quantity);
 71  		sci.setPrice(product.getPrice());
 72  		cart.addShoppingCartItem(sci);
 73  
 74  		try {
 75  			shoppingCartService.priceShoppingCart(cart);
 76  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
 77  		} catch (Exception ex) {
 78  			cart.removeShoppingCartItem(sci);
 79  			throw ex;
 80  		}
 81  
 82  		return cart;
 83  	}
 84  
 85  	@POST
 86  	@Path("/{cartId}/{tmpId}")
 87  	@Produces(MediaType.APPLICATION_JSON)
 88  	public ShoppingCart set(@PathParam("cartId") String cartId,
 89  							@PathParam("tmpId") String tmpId) throws Exception {
 90  
 91  		ShoppingCart cart = shoppingCartService.getShoppingCart(cartId);
 92  		ShoppingCart tmpCart = shoppingCartService.getShoppingCart(tmpId);
 93  
 94  		if (tmpCart != null) {
 95  			cart.resetShoppingCartItemList();
 96  			cart.setShoppingCartItemList(tmpCart.getShoppingCartItemList());
 97  		}
 98  
 99  		try {
100  			shoppingCartService.priceShoppingCart(cart);
101  			cart.setShoppingCartItemList(dedupeCartItems(cart.getShoppingCartItemList()));
102  		} catch (Exception ex) {
103  			throw ex;
104  		}
105  
106  		return cart;
107  	}
108  
109  	@DELETE
110  	@Path("/{cartId}/{itemId}/{quantity}")
111  	@Produces(MediaType.APPLICATION_JSON)
112  	public ShoppingCart delete(@PathParam("cartId") String cartId,
```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/InventoryNotificationMDB.java
      * Line Number: 7
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import com.redhat.coolstore.model.Order;
  4  import com.redhat.coolstore.utils.Transformers;
  5  
  6  import javax.inject.Inject;
  7  import javax.jms.*;
  8  import javax.naming.Context;
  9  import javax.naming.InitialContext;
 10  import javax.naming.NamingException;
 11  import javax.rmi.PortableRemoteObject;
 12  import java.util.Hashtable;
 13  import java.util.logging.Logger;
 14  
 15  public class InventoryNotificationMDB implements MessageListener {
 16  
 17      private static final int LOW_THRESHOLD = 50;
 18  
 19      @Inject
 20      private CatalogService catalogService;
 21  
 22      @Inject
 23      private Logger log;
 24  
 25      private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
 26      private final static String JMS_FACTORY = "TCF";
 27      private final static String TOPIC = "topic/orders";
 28      private TopicConnection tcon;
 29      private TopicSession tsession;
 30      private TopicSubscriber tsubscriber;
 31  
 32      public void onMessage(Message rcvMessage) {
 33          TextMessage msg;
 34          {
 35              try {
 36                  System.out.println("received message inventory");
 37                  if (rcvMessage instanceof TextMessage) {
 38                      msg = (TextMessage) rcvMessage;
 39                      String orderStr = msg.getBody(String.class);
 40                      Order order = Transformers.jsonToOrder(orderStr);
 41                      order.getItemList().forEach(orderItem -> {
 42                          int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
 43                          int new_quantity = old_quantity - orderItem.getQuantity();
 44                          if (new_quantity < LOW_THRESHOLD) {
 45                              System.out.println("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
 46                          } else {
 47                              orderItem.setQuantity(new_quantity);
 48                          }
 49                      });
 50                  }
 51  
 52  
 53              } catch (JMSException jmse) {
 54                  System.err.println("An exception occurred: " + jmse.getMessage());
 55              }
 56          }
 57      }
 58  
 59      public void init() throws NamingException, JMSException {
 60          Context ctx = getInitialContext();
 61          TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
 62          tcon = tconFactory.createTopicConnection();
 63          tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
 64          Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
 65          tsubscriber = tsession.createSubscriber(topic);
 66          tsubscriber.setMessageListener(this);
 67          tcon.start();
 68      }
 69  
 70      public void close() throws JMSException {
 71          tsubscriber.close();
 72          tsession.close();
 73          tcon.close();
 74      }
 75  
 76      private static InitialContext getInitialContext() throws NamingException {
 77          Hashtable<String, String> env = new Hashtable<>();
 78          env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
 79          env.put(Context.PROVIDER_URL, "t3://localhost:7001");
 80          env.put("weblogic.jndi.createIntermediateContexts", "true");
 81          return new InitialContext(env);
 82      }
 83  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 6
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 7
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 8
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/OrderServiceMDB.java
      * Line Number: 9
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
      * Code Snippet:
```java
  1  package com.redhat.coolstore.service;
  2  
  3  import javax.ejb.ActivationConfigProperty;
  4  import javax.ejb.MessageDriven;
  5  import javax.inject.Inject;
  6  import javax.jms.JMSException;
  7  import javax.jms.Message;
  8  import javax.jms.MessageListener;
  9  import javax.jms.TextMessage;
 10  
 11  import com.redhat.coolstore.model.Order;
 12  import com.redhat.coolstore.utils.Transformers;
 13  import weblogic.i18n.logging.NonCatalogLogger;
 14  
 15  @MessageDriven(name = "OrderServiceMDB", activationConfig = {
 16  	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
 17  	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
 18  	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
 19  public class OrderServiceMDB implements MessageListener { 
 20  
 21  	@Inject
 22  	OrderService orderService;
 23  
 24  	@Inject
 25  	CatalogService catalogService;
 26  
 27  	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
 28  
 29  	@Override
 30  	public void onMessage(Message rcvMessage) {
 31  		System.out.println("\nMessage recd !");
 32  		TextMessage msg = null;
 33  		try {
 34  				if (rcvMessage instanceof TextMessage) {
 35  						msg = (TextMessage) rcvMessage;
 36  						String orderStr = msg.getBody(String.class);
 37  						System.out.println("Received order: " + orderStr);
 38  						Order order = Transformers.jsonToOrder(orderStr);
 39  						System.out.println("Order object is " + order);
 40  						orderService.save(order);
 41  						order.getItemList().forEach(orderItem -> {
 42  							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
 43  						});
 44  				}
 45  		} catch (JMSException e) {
 46  			throw new RuntimeException(e);
 47  		}
 48  	}
 49  
 50  }

```
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Line Number: 7
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
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
  * file:///tmp/source-code/src/main/java/com/redhat/coolstore/service/ShoppingCartOrderProcessor.java
      * Line Number: 8
      * Message: 'References to JavaEE/JakartaEE JMS elements should be removed and replaced with their Quarkus SmallRye/Microprofile equivalents.'
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
