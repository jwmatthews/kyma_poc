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
To rewrite the `InventoryNotificationMDB` class to use Quarkus, we need to follow a similar approach to the one used in Example #1. Here are the steps we will take:

1. Replace the JMS `MessageListener` interface with a method annotated with `@Incoming` to consume messages from a reactive messaging channel.
2. Remove the JNDI and JMS setup code, as Quarkus will manage the message consumption.
3. Use `@ApplicationScoped` to define the bean's lifecycle.
4. Use `@Blocking` to indicate that the processing is not non-blocking and should be executed on a worker thread.
5. Inject a `Logger` using CDI instead of using `java.util.logging.Logger` directly.
6. Remove the `init` and `close` methods as they are no longer needed.
7. Update the package imports to use Jakarta EE 8 APIs and Quarkus-specific annotations.

Here is the diff of the changes:

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
+import jakarta.inject.Inject;
+import org.eclipse.microprofile.reactive.messaging.Incoming;
-import java.util.Hashtable;
-import java.util.logging.Logger;
+import org.jboss.logging.Logger;
+import io.smallrye.reactive.messaging.annotations.Blocking;
+import jakarta.enterprise.context.ApplicationScoped;

-public class InventoryNotificationMDB implements MessageListener {
+@ApplicationScoped
+public class InventoryNotificationMDB {

    private static final int LOW_THRESHOLD = 50;

    @Inject
    private CatalogService catalogService;

    @Inject
    private Logger log;

-    private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
-    private final static String JMS_FACTORY = "TCF";
-    private final static String TOPIC = "topic/orders";
-    private TopicConnection tcon;
-    private TopicSession tsession;
-    private TopicSubscriber tsubscriber;

-    public void onMessage(Message rcvMessage) {
+    @Incoming("orders-incoming")
+    @Blocking
+    public void onMessage(String orderStr) {
-        TextMessage msg;
         try {
             System.out.println("received message inventory");
-            if (rcvMessage instanceof TextMessage) {
-                msg = (TextMessage) rcvMessage;
-                String orderStr = msg.getBody(String.class);
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
-            }
-        } catch (JMSException jmse) {
-            System.err.println("An exception occurred: " + jmse.getMessage());
+        } catch (Exception e) {
+            log.error("An exception occurred: ", e);
         }
     }

-    public void init() throws NamingException, JMSException {
-        Context ctx = getInitialContext();
-        TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
-        tcon = tconFactory.createTopicConnection();
-        tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
-        Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
-        tsubscriber = tsession.createSubscriber(topic);
-        tsubscriber.setMessageListener(this);
-        tcon.start();
-    }
-
-    public void close() throws JMSException {
-        tsubscriber.close();
-        tsession.close();
-        tcon.close();
-    }
-
-    private static InitialContext getInitialContext() throws NamingException {
-        Hashtable<String, String> env = new Hashtable<>();
-        env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
-        env.put(Context.PROVIDER_URL, "t3://localhost:7001");
-        env.put("weblogic.jndi.createIntermediateContexts", "true");
-        return new InitialContext(env);
-    }
}
```

Please note that the `@Incoming` annotation value `"orders-incoming"` should match the name of the channel configured in your `application.properties` file for the incoming messages. Adjust this value according to your actual configuration.

Also, the exception handling has been simplified to catch a generic `Exception` and log it using the injected `Logger`. This is because we no longer deal with `JMSException` specifically, as the Quarkus framework abstracts away the underlying messaging system details.
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
+import jakarta.inject.Inject;
+import org.eclipse.microprofile.reactive.messaging.Incoming;
-import java.util.Hashtable;
-import java.util.logging.Logger;
+import org.jboss.logging.Logger;
+import io.smallrye.reactive.messaging.annotations.Blocking;
+import jakarta.enterprise.context.ApplicationScoped;

-public class InventoryNotificationMDB implements MessageListener {
+@ApplicationScoped
+public class InventoryNotificationMDB {

    private static final int LOW_THRESHOLD = 50;

    @Inject
    private CatalogService catalogService;

    @Inject
    private Logger log;

-    private final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
-    private final static String JMS_FACTORY = "TCF";
-    private final static String TOPIC = "topic/orders";
-    private TopicConnection tcon;
-    private TopicSession tsession;
-    private TopicSubscriber tsubscriber;

-    public void onMessage(Message rcvMessage) {
+    @Incoming("orders-incoming")
+    @Blocking
+    public void onMessage(String orderStr) {
-        TextMessage msg;
         try {
             System.out.println("received message inventory");
-            if (rcvMessage instanceof TextMessage) {
-                msg = (TextMessage) rcvMessage;
-                String orderStr = msg.getBody(String.class);
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
-            }
-        } catch (JMSException jmse) {
-            System.err.println("An exception occurred: " + jmse.getMessage());
+        } catch (Exception e) {
+            log.error("An exception occurred: ", e);
         }
     }

-    public void init() throws NamingException, JMSException {
-        Context ctx = getInitialContext();
-        TopicConnectionFactory tconFactory = (TopicConnectionFactory) PortableRemoteObject.narrow(ctx.lookup(JMS_FACTORY), TopicConnectionFactory.class);
-        tcon = tconFactory.createTopicConnection();
-        tsession = tcon.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
-        Topic topic = (Topic) PortableRemoteObject.narrow(ctx.lookup(TOPIC), Topic.class);
-        tsubscriber = tsession.createSubscriber(topic);
-        tsubscriber.setMessageListener(this);
-        tcon.start();
-    }
-
-    public void close() throws JMSException {
-        tsubscriber.close();
-        tsession.close();
-        tcon.close();
-    }
-
-    private static InitialContext getInitialContext() throws NamingException {
-        Hashtable<String, String> env = new Hashtable<>();
-        env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
-        env.put(Context.PROVIDER_URL, "t3://localhost:7001");
-        env.put("weblogic.jndi.createIntermediateContexts", "true");
-        return new InitialContext(env);
-    }
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
