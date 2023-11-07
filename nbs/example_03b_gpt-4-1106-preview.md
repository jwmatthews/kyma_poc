# Example #3
## Prompt:
You are an excellent enterprise architect who has an extensive
background in helping companies rewrite their legacy Java EE applications to Quarkus.

You will read a user's problem along with examples of how they have solved a problem in the past.
The past examples will be presented in format of a summary of the issue along with source code of 
that point in time along with the updated source code when the problem is fixed

You will then write Quarkus code to solve their current problem.
You will output the results in the form a diff which can be applied via 'git apply'.

Example #1 Issue: Something

Example #1 Original Source Code:
```java
package com.redhat.coolstore.service;

import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.inject.Inject;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;

import com.redhat.coolstore.model.Order;
import com.redhat.coolstore.utils.Transformers;
import weblogic.i18n.logging.NonCatalogLogger;

@MessageDriven(name = "OrderServiceMDB", activationConfig = {
	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
public class OrderServiceMDB implements MessageListener { 

	@Inject
	OrderService orderService;

	@Inject
	CatalogService catalogService;

	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());

	@Override
	public void onMessage(Message rcvMessage) {
		System.out.println("\nMessage recd !");
		TextMessage msg = null;
		try {
				if (rcvMessage instanceof TextMessage) {
						msg = (TextMessage) rcvMessage;
						String orderStr = msg.getBody(String.class);
						System.out.println("Received order: " + orderStr);
						Order order = Transformers.jsonToOrder(orderStr);
						System.out.println("Order object is " + order);
						orderService.save(order);
						order.getItemList().forEach(orderItem -> {
							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
						});
				}
		} catch (JMSException e) {
			throw new RuntimeException(e);
		}
	}

}
```

Example #1 Solved Source Code:
```java
package com.redhat.coolstore.service;

// import javax.ejb.ActivationConfigProperty;
// import javax.ejb.MessageDriven;
import jakarta.inject.Inject;
import jakarta.transaction.Transactional;

import org.eclipse.microprofile.reactive.messaging.Incoming;

import com.redhat.coolstore.model.Order;
import com.redhat.coolstore.utils.Transformers;

import io.smallrye.reactive.messaging.annotations.Blocking;
import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class OrderServiceMDB {

	@Inject
	OrderService orderService;

	@Inject
	CatalogService catalogService;

	@Incoming("orders-incoming")
	@Blocking
	@Transactional
	public void onMessage(String orderStr) {
		System.out.println("\nMessage recd !");
		System.out.println("Received order: " + orderStr);
		Order order = Transformers.jsonToOrder(orderStr);
		System.out.println("Order object is " + order);
		orderService.save(order);
		order.getItemList().forEach(orderItem -> {
			catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
		});
	}

}
```

Current Issue: 
Something

Current Issue Original Source Code: 
```java
package com.redhat.coolstore.service;

import com.redhat.coolstore.model.Order;
import com.redhat.coolstore.utils.Transformers;

import javax.inject.Inject;
import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.rmi.PortableRemoteObject;
import java.util.Hashtable;
import java.util.logging.Logger;

public class InventoryNotificationMDB implements MessageListener {

    private static final int LOW_THRESHOLD = 50;

    @Inject
    private CatalogService catalogService;

    @Inject
    private Logger log;

    private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
    private final static String JMS_FACTORY = "TCF";
    private final static String TOPIC = "topic/orders";
    private TopicConnection tcon;
    private TopicSession tsession;
    private TopicSubscriber tsubscriber;

    public void onMessage(Message rcvMessage) {
        TextMessage msg;
        {
            try {
                System.out.println("received message inventory");
                if (rcvMessage instanceof TextMessage) {
                    msg = (TextMessage) rcvMessage;
                    String orderStr = msg.getBody(String.class);
                    Order order = Transformers.jsonToOrder(orderStr);
                    order.getItemList().forEach(orderItem -> {
                        int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
                        int new_quantity = old_quantity - orderItem.getQuantity();
                        if (new_quantity < LOW_THRESHOLD) {
                            System.out.println("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
                        } else {
                            orderItem.setQuantity(new_quantity);
                        }
                    });
                }


            } catch (JMSException jmse) {
                System.err.println("An exception occurred: " + jmse.getMessage());
            }
        }
    }

    public void init() throws NamingException, JMSException {
        Context ctx = getInitialContext();
        TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
        tcon = tconFactory.createTopicConnection();
        tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
        Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
        tsubscriber = tsession.createSubscriber(topic);
        tsubscriber.setMessageListener(this);
        tcon.start();
    }

    public void close() throws JMSException {
        tsubscriber.close();
        tsession.close();
        tcon.close();
    }

    private static InitialContext getInitialContext() throws NamingException {
        Hashtable<String, String> env = new Hashtable<>();
        env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
        env.put(Context.PROVIDER_URL, "t3://localhost:7001");
        env.put("weblogic.jndi.createIntermediateContexts", "true");
        return new InitialContext(env);
    }
}
```

Your job is to look at the 'Current Issue' and the 'Current Issue Original Source Code' 
and rewrite the 'Current Issue Original Source Code' so the 'Current Issue' is solved 
in a manner similar to how 'Example #1 Original Source Code' was rewritten to 
'Example #1 Solved Source Code' 

Think through the changes you will make and explain each step of the process.
If you are unsure of what changes is needed please state you are unsure and ask 
for clarification to help you.

When you are done explaining the reasoning for each change, write the updated 
Quarkus source code in the form of a diff from the original file in the Markdown format of:

```diff
....
```
## Result:
To rewrite the `InventoryNotificationMDB` class to use Quarkus, we need to follow a similar approach as in the example provided. Here are the steps we will take:

1. Replace the JMS `MessageListener` interface with a method annotated with `@Incoming` to consume messages from a reactive messaging channel.
2. Remove the JMS and WebLogic specific code, such as the `init` and `close` methods, and the JNDI lookup configuration.
3. Use CDI (`@Inject`) to inject any required services.
4. Annotate the class with `@ApplicationScoped` to define the lifecycle of the bean.
5. Use `@Blocking` to indicate that the processing is blocking and should not be executed on the event loop (I/O thread).
6. Add `@Transactional` if the message processing involves database operations that should be transactional.
7. Replace the `Logger` injection with a Quarkus-compatible logger, such as `org.jboss.logging.Logger`.

Let's apply these changes to the `InventoryNotificationMDB` class:

```diff
package com.redhat.coolstore.service;

import com.redhat.coolstore.model.Order;
import com.redhat.coolstore.utils.Transformers;

-import javax.inject.Inject;
-import javax.jms.*;
-import javax.naming.Context;
-import javax.naming.InitialContext;
-import javax.naming.NamingException;
-import javax.rmi.PortableRemoteObject;
-import java.util.Hashtable;
-import java.util.logging.Logger;
+import jakarta.inject.Inject;
+import org.eclipse.microprofile.reactive.messaging.Incoming;
+import io.smallrye.reactive.messaging.annotations.Blocking;
+import jakarta.enterprise.context.ApplicationScoped;
+import jakarta.transaction.Transactional;
+import org.jboss.logging.Logger;

- public class InventoryNotificationMDB implements MessageListener {
+ @ApplicationScoped
+ public class InventoryNotificationMDB {

    private static final int LOW_THRESHOLD = 50;

    @Inject
    private CatalogService catalogService;

    @Inject
    private Logger log;

-   private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
-   private final static String JMS_FACTORY = "TCF";
-   private final static String TOPIC = "topic/orders";
-   private TopicConnection tcon;
-   private TopicSession tsession;
-   private TopicSubscriber tsubscriber;

-   public void onMessage(Message rcvMessage) {
+   @Incoming("orders-incoming")
+   @Blocking
+   @Transactional
+   public void onMessage(String orderStr) {
        {
            try {
                log.info("received message inventory");
-               if (rcvMessage instanceof TextMessage) {
-                   msg = (TextMessage) rcvMessage;
-                   String orderStr = msg.getBody(String.class);
                    Order order = Transformers.jsonToOrder(orderStr);
                    order.getItemList().forEach(orderItem -> {
                        int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
                        int new_quantity = old_quantity - orderItem.getQuantity();
                        if (new_quantity < LOW_THRESHOLD) {
                            log.info("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
                        } else {
                            orderItem.setQuantity(new_quantity);
                        }
                    });
-               }

            } catch (Exception e) {
                log.error("An exception occurred: " + e.getMessage(), e);
            }
        }
    }

-   public void init() throws NamingException, JMSException {
-       Context ctx = getInitialContext();
-       TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
-       tcon = tconFactory.createTopicConnection();
-       tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
-       Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
-       tsubscriber = tsession.createSubscriber(topic);
-       tsubscriber.setMessageListener(this);
-       tcon.start();
-   }

-   public void close() throws JMSException {
-       tsubscriber.close();
-       tsession.close();
-       tcon.close();
-   }

-   private static InitialContext getInitialContext() throws NamingException {
-       Hashtable<String, String> env = new Hashtable<>();
-       env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
-       env.put(Context.PROVIDER_URL, "t3://localhost:7001");
-       env.put("weblogic.jndi.createIntermediateContexts", "true");
-       return new InitialContext(env);
-   }
}
```

This diff represents the changes needed to convert the legacy Java EE MDB to a Quarkus-based service that listens to a reactive messaging channel. The `@Incoming` annotation specifies the channel name that this method will listen to. The `@Blocking` annotation indicates that the processing is blocking, and `@Transactional` ensures that the message processing is done within a transactional context. The `Logger` is now injected using Quarkus' preferred logging framework. The JMS and WebLogic specific code has been removed as it is no longer needed in a Quarkus application.
### Actual Diff:
```

package com.redhat.coolstore.service;

import com.redhat.coolstore.model.Order;
import com.redhat.coolstore.utils.Transformers;

-import javax.inject.Inject;
-import javax.jms.*;
-import javax.naming.Context;
-import javax.naming.InitialContext;
-import javax.naming.NamingException;
-import javax.rmi.PortableRemoteObject;
-import java.util.Hashtable;
-import java.util.logging.Logger;
+import jakarta.inject.Inject;
+import org.eclipse.microprofile.reactive.messaging.Incoming;
+import io.smallrye.reactive.messaging.annotations.Blocking;
+import jakarta.enterprise.context.ApplicationScoped;
+import jakarta.transaction.Transactional;
+import org.jboss.logging.Logger;

- public class InventoryNotificationMDB implements MessageListener {
+ @ApplicationScoped
+ public class InventoryNotificationMDB {

    private static final int LOW_THRESHOLD = 50;

    @Inject
    private CatalogService catalogService;

    @Inject
    private Logger log;

-   private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
-   private final static String JMS_FACTORY = "TCF";
-   private final static String TOPIC = "topic/orders";
-   private TopicConnection tcon;
-   private TopicSession tsession;
-   private TopicSubscriber tsubscriber;

-   public void onMessage(Message rcvMessage) {
+   @Incoming("orders-incoming")
+   @Blocking
+   @Transactional
+   public void onMessage(String orderStr) {
        {
            try {
                log.info("received message inventory");
-               if (rcvMessage instanceof TextMessage) {
-                   msg = (TextMessage) rcvMessage;
-                   String orderStr = msg.getBody(String.class);
                    Order order = Transformers.jsonToOrder(orderStr);
                    order.getItemList().forEach(orderItem -> {
                        int old_quantity = catalogService.getCatalogItemById(orderItem.getProductId()).getInventory().getQuantity();
                        int new_quantity = old_quantity - orderItem.getQuantity();
                        if (new_quantity < LOW_THRESHOLD) {
                            log.info("Inventory for item " + orderItem.getProductId() + " is below threshold (" + LOW_THRESHOLD + "), contact supplier!");
                        } else {
                            orderItem.setQuantity(new_quantity);
                        }
                    });
-               }

            } catch (Exception e) {
                log.error("An exception occurred: " + e.getMessage(), e);
            }
        }
    }

-   public void init() throws NamingException, JMSException {
-       Context ctx = getInitialContext();
-       TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
-       tcon = tconFactory.createTopicConnection();
-       tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
-       Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
-       tsubscriber = tsession.createSubscriber(topic);
-       tsubscriber.setMessageListener(this);
-       tcon.start();
-   }

-   public void close() throws JMSException {
-       tsubscriber.close();
-       tsession.close();
-       tcon.close();
-   }

-   private static InitialContext getInitialContext() throws NamingException {
-       Hashtable<String, String> env = new Hashtable<>();
-       env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
-       env.put(Context.PROVIDER_URL, "t3://localhost:7001");
-       env.put("weblogic.jndi.createIntermediateContexts", "true");
-       return new InitialContext(env);
-   }
}

```
### Expected Diff:
```
@@ -1,22 +1,20 @@
 package com.redhat.coolstore.service;
 
-import javax.ejb.ActivationConfigProperty;
-import javax.ejb.MessageDriven;
-import javax.inject.Inject;
-import javax.jms.JMSException;
-import javax.jms.Message;
-import javax.jms.MessageListener;
-import javax.jms.TextMessage;
+// import javax.ejb.ActivationConfigProperty;
+// import javax.ejb.MessageDriven;
+import jakarta.inject.Inject;
+import jakarta.transaction.Transactional;
+
+import org.eclipse.microprofile.reactive.messaging.Incoming;
 
 import com.redhat.coolstore.model.Order;
 import com.redhat.coolstore.utils.Transformers;
-import weblogic.i18n.logging.NonCatalogLogger;
 
-@MessageDriven(name = "OrderServiceMDB", activationConfig = {
-	@ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "topic/orders"),
-	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Topic"),
-	@ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge")})
-public class OrderServiceMDB implements MessageListener { 
+import io.smallrye.reactive.messaging.annotations.Blocking;
+import jakarta.enterprise.context.ApplicationScoped;
+
+@ApplicationScoped
+public class OrderServiceMDB {
 
 	@Inject
 	OrderService orderService;
@@ -24,27 +22,18 @@ public class OrderServiceMDB implements MessageListener {
 	@Inject
 	CatalogService catalogService;
 
-	private NonCatalogLogger log = new NonCatalogLogger(OrderServiceMDB.class.getName());
-
-	@Override
-	public void onMessage(Message rcvMessage) {
+	@Incoming("orders-incoming")
+	@Blocking
+	@Transactional
+	public void onMessage(String orderStr) {
 		System.out.println("\nMessage recd !");
-		TextMessage msg = null;
-		try {
-				if (rcvMessage instanceof TextMessage) {
-						msg = (TextMessage) rcvMessage;
-						String orderStr = msg.getBody(String.class);
-						System.out.println("Received order: " + orderStr);
-						Order order = Transformers.jsonToOrder(orderStr);
-						System.out.println("Order object is " + order);
-						orderService.save(order);
-						order.getItemList().forEach(orderItem -> {
-							catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
-						});
-				}
-		} catch (JMSException e) {
-			throw new RuntimeException(e);
-		}
+		System.out.println("Received order: " + orderStr);
+		Order order = Transformers.jsonToOrder(orderStr);
+		System.out.println("Order object is " + order);
+		orderService.save(order);
+		order.getItemList().forEach(orderItem -> {
+			catalogService.updateInventoryItems(orderItem.getProductId(), orderItem.getQuantity());
+		});
 	}
 
 }
\ No newline at end of file

```
